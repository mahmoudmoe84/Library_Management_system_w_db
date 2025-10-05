import random
from classes_lib_system import Library
from functions import continue_exit_return_to_main , print_selection_list

from llm_service import generate_sql_from_question
from db.db_connection import execute_read_query , get_db_schema
import json


def handle_smart_search():
    """
    Manager the workflow for the natural lanuage search feature
    """
    question = input("\n Ask anything about the library (e.g/, 'who has borrowed books?'):\n")
    
    print('Fetching databse schema for the llm....')
    db_schema = get_db_schema()
    if not db_schema:
        print("could not fetch databse shcema. Aborting")
        return
    sql_query = generate_sql_from_question(question,db_schema)
    
    if not sql_query:
        print('could not generate sql query please try another question')
        return
    
    print(f"\n Generated SQL: {sql_query}")
    results = execute_read_query(sql_query)
    
    print("\n Query Results:")
    if results:
        for row in results:
            print(json.dumps(row,indent=2,default=str))
    elif results == []:
        print("No Records found that match your question")




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
        if choice == 7:
            handle_smart_search()
            user_choice = continue_exit_return_to_main()
            if user_choice =="exit":
                break
            elif user_choice =="continue":
                print_selection_list()
        
        if choice ==8:
            break

if __name__ == "__main__":
    main()
        
        