def continue_exit_return_to_main():
    while True:
        try:
            continue_or_break = int(input('\n\nPlease Specify your next action\n1- Exit\n2- Return to main menu '))
        except Exception as e:
            print('Error e , please enter either 1 or 2')
            continue
        
        if continue_or_break == 1:
            return "exit"
        elif continue_or_break == 2:
            return "continue"
        else:
            print(f"Invalid choice '{continue_or_break}'. Please enter 1 or 2.")
            continue 
        

def print_selection_list():
    print('Welcome to the library management system')
    print('Below are the options you have')
    print('1- Add Book')
    print('2- Add User')
    print('3- Find Book')
    print("4- Borrow Book")
    print("5- Return Book")
    print("6- Borrowed Books")
    print('7- Exit')