import random
import sys
import os

# # Add the parent directory to the Python path to find the db module
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)

from db import get_connection

class Library:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize attributes only once
            cls._instance.books = {}
            cls._instance.users = {}
        return cls._instance
    
    def _validate_input(self, value, name):
        """Validate that input is not empty or None"""
        if not value or not str(value).strip():
            raise ValueError(f"{name} cannot be empty")
        return str(value).strip()

    def _validate_positive_number(self, value, name):
        """Validate that number is positive"""
        try:
            num = int(value)
            if num <= 0:
                raise ValueError(f"{name} must be a positive number")
            return num
        except (ValueError, TypeError):
            raise ValueError(f"{name} must be a valid positive number")
    
    def add_books(self, book_title, book_author, num_copies):
        # Validate inputs
        book_title = self._validate_input(book_title, "Book title")
        book_author = self._validate_input(book_author, "Book author")
        num_copies = self._validate_positive_number(num_copies, "Number of copies")
        
        conn = None
        
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("select book_id,num_copies from book where title=%s",(book_title,))
            row = cur.fetchone()
            if row:
                book_id,existing_copies = row
                new_total = existing_copies + num_copies
                cur.execute("update book set num_copies=%s where book_id=%s",(new_total,book_id))
                print(f"update new number of book {book_title} to be new total of {new_total}")
            else: 
                cur.execute(
                    "insert into book (title, author , num_copies,on_loan) \
                    values(%s,%s,%s,%s)",(book_title,book_author,num_copies,0))
                print(f"Added new book {book_title} with total number of copies of {num_copies}")
            conn.commit()
        
        except Exception as e:
            print(f"DB Erro {e}")
            return
        finally:
            if conn:
                conn.close()

    def generate_random_id(self):
        conn = get_connection()
        cur = conn.cursor()
        user_id = f'{random.randint(0,999999):06d}'
        cur.execute('select user_id from user where user_id=%s',(user_id,))
        row = cur.fetchone()
        if row is None:
            conn.close()
            return user_id
        
    def register_new_user(self, user_name):
        # Validate input
        user_name = self._validate_input(user_name, "User name")
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('select user_id from user where user_id=%s',(user_id,))
        row = cur.fetchone()
        
        if row:
            print(f"User {user_name} already exists in the system with user_id ={row[0]}")
            conn.close()
            
        user_id = self.generate_random_id()
        cur.execute('insert into user (name,user_id) values (%s,%s)',(user_name,user_id))
        conn.commit()
        conn.close()
    
    def find_book(self, book_title):
        # Validate input
        book_title = self._validate_input(book_title, "Book title")
        
        try:
            available_copies = self.books[book_title][1] - self.books[book_title][2]
            print(f"book {book_title} is authored by {self.books[book_title][0]} and has {available_copies} copies available")
        except KeyError:
            print(f"Book title doesn't exist, returns Error")
    
    def borrow_book(self, book_title, user_name):
        # Validate inputs
        book_title = self._validate_input(book_title, "Book title")
        user_name = self._validate_input(user_name, "User name")
        
        #Open Connections with DB
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("select book_id,num_copies,on_loan from book where title=%s",(book_title,))
        book_row = cur.fetchone()
        if book_row is None:
            print(f"Book Title {book_title} doesn't exist in our book system")
            conn.close()
            return
        book_id,num_copies,on_loan = book_row
        cur.execute('select user_id from user where name=%s',(user_name,))
        user_row = cur.fetchone()
        if user_row is None:
            print(f'There is no User {user_name} in the system pls create user first')
            conn.close()
            return
        user_id = user_row[0]
        if on_loan >= num_copies:
            print(f'all copies of {book_title} are on loan')
            conn.close()
            return
        # all checks done now loan the book
        cur.execute('insert into loan (book_id,user_id,loan_date,return_date,returned) values(%s,%s,curdate(),\
                    date_add(curdate(), interval 14 day),false)',(book_id,user_id))
        cur.execute("update book set on_loan = on_loan+1 where book_id=%s",(book_id,))
        print(f"book {book_title} has been loaned sucessfully to {user_name}")
        conn.commit()
        conn.close()

        
    def books_on_loan(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""select b.title , count(l.loan_id) as borrowed_count
                    from loan l 
                    join book b on l.book_id =b.book_id
                    where l.returned = False
                    group by b.title;""")
        loaned_books = cur.fetchall()
        conn.close()
        if not loaned_books:
            print('No books currently on loan')
            return
        result = [(title,count) for title , count in loaned_books]
        print(result)
        return result
        
    
    def return_book(self, book_title, user_name):
        # Validate inputs
        book_title = self._validate_input(book_title, "Book title")
        user_name = self._validate_input(user_name, "User name")
        
        if user_name not in self.users:
            print(f"User {user_name} not in the system")
            return
        if book_title not in self.books:
            print(f"Book {book_title} not in the system")
            return
        if book_title not in self.users[user_name][1]:
            print(f'User {user_name} doesn\'t have the book')
            return
        
        self.books[book_title][2] -= 1
        self.users[user_name][1].remove(book_title)
        print(f"User {user_name} returned book {book_title} successfully")
        
                            