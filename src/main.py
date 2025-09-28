import random
from classes_lib_system import Library
from functions import continue_exit_return_to_main , print_selection_list

def main():
    library = Library()  # This will always return the same instance
    print_selection_list()
    while True:
        try:
            choice = int(input('Enter your choise from the above list: '))
        except Exception as e:
            print('enter value choice pls')
            continue
        
        if choice ==1:
            try:
                book_title = input('Enter Book Title:')
                book_author = input('Author Name:')
                num_copies_input = input('Enter num of Copies: ')
                library.add_books(book_title=book_title, book_author=book_author, num_copies=num_copies_input)
            except ValueError as e:
                print(f'Error: {e}')
            user_choice = continue_exit_return_to_main()
            if user_choice =="exit":
                break
            elif user_choice =="continue":
                print_selection_list()
    
        if choice ==2:
            try:
                user_name = input("Enter User Name: ")
                library.register_new_user(user_name=user_name)
            except ValueError as e:
                print(f'Error: {e}')
            user_choice = continue_exit_return_to_main()
            if user_choice =="exit":
                break
            elif user_choice =="continue":
                print_selection_list()

        if choice ==3:
            try:
                book_name = input("Enter Book Name:")
                library.find_book(book_title=book_name)
            except ValueError as e:
                print(f'Error: {e}')
            user_choice = continue_exit_return_to_main()
            if user_choice =="exit":
                break
            elif user_choice =="continue":
                print_selection_list()
          

        if choice ==4:
            try:
                user_name = input('Enter User Name: ')
                book_title = input("Enter Book Title: ")
                library.borrow_book(book_title=book_title, user_name=user_name)
            except ValueError as e:
                print(f'Error: {e}')
            user_choice = continue_exit_return_to_main()
            if user_choice =="exit":
                break
            elif user_choice =="continue":
                print_selection_list()

        if choice==5:
            try:
                user_name = input('Enter User Name: ')
                book_title = input("Enter Book Title: ")
                library.return_book(book_title=book_title, user_name=user_name)
            except ValueError as e:
                print(f'Error: {e}')
            user_choice = continue_exit_return_to_main()
            if user_choice =="exit":
                break
            elif user_choice =="continue":
                print_selection_list()
 
        if choice ==6:
            library.books_on_loan()
            user_choice = continue_exit_return_to_main()
            if user_choice =="exit":
                break
            elif user_choice =="continue":
                print_selection_list()
                
        if choice ==7:
            break

if __name__ == "__main__":
    main()
        
        