# Library Management System

A robust Python project for managing books and users in a library. This project demonstrates advanced object-oriented programming concepts including the **Singleton pattern**, comprehensive **input validation**, and **error handling**.

## What This Does

This is a professional-grade library system where you can add books, register users, and let people borrow and return books. It's a command-line program that uses Python classes and functions with advanced design patterns to ensure data integrity and user-friendly operation.

## Key Features & Improvements

The program has these main features with **enhanced robustness**:

### Core Functionality
- Add books to the library (with author and number of copies)
- Register new users (gives them a random 6-digit ID number)
- Search for books with detailed availability information
- Let users borrow books (with comprehensive validation)
- Let users return books (with proper ownership verification)
- Show which books are currently borrowed

### **🆕 Advanced Features**
- **Singleton Pattern**: Single library instance ensures data persistence across the application
- **Input Validation**: Comprehensive validation prevents empty inputs, invalid numbers, and system crashes
- **Robust Error Handling**: User-friendly error messages instead of program crashes
- **Business Logic Validation**: 
  - Can't borrow the same book twice
  - Can't return books you don't have
  - Prevents negative quantities
  - Validates user existence before operations

## Things to Note
- **Singleton Design**: Only one Library instance exists throughout the program lifecycle
- Users get a random 6-digit ID when they register
- **Enhanced Validation**: All inputs are validated before processing
- **Error Recovery**: Program continues running even with invalid inputs
- Tracks available vs borrowed copies accurately
- **Comprehensive Error Messages**: Clear feedback for all error conditions

## How the Code is Organized

The code is organized into separate files with **advanced design patterns**:

### `classes_lib_system.py`
This contains the main Library class with **Singleton pattern** implementation and comprehensive methods:

**Core Methods:**
- `add_books()` - adds books or updates quantities (with validation)
- `register_new_user()` - creates new users (with input validation)
- `find_book()` - searches for books (with error handling)
- `borrow_book()` - handles borrowing (with comprehensive business logic validation)
- `return_book()` - handles returns (with ownership verification)
- `books_on_loan()` - shows borrowed books
- `generate_random_id()` - creates unique user IDs

**🆕 Advanced Features:**
- **Singleton Pattern**: `__new__()` method ensures single instance
- **Input Validation**: `_validate_input()` and `_validate_positive_number()` helper methods
- **Robust Error Handling**: Early returns and clear error messages

### `functions.py`
Helper functions for the menu and user interaction

### `main.py`
The main program with **enhanced error handling**:
- **Try-catch blocks** around all user operations
- **Graceful error recovery** - program continues even with invalid inputs
- **User-friendly error messages** instead of crashes
- Singleton Library instance usage

## How to Run It

### What You Need
- Python 3 (any recent version should work)

### Setup
1. Download all the files and put them in the same folder
2. Make sure you have these files:
   - `main.py`
   - `classes_lib_system.py`
   - `functions.py` 
   - `__init__.py`

### Running
Just run this in your terminal:
```bash
python main.py
```

## How to Use It

When you run the program, you'll see a menu with 7 options. Just type the number and press enter.

### The Menu Options

**1. Add Book**
- Type in the book title, author, and how many copies you have
- If the book already exists, it adds more copies
- If it's new, it creates a new entry

**2. Add User** 
- Just enter someone's name
- The system gives them a random ID number
- If they're already registered, it tells you their ID

**3. Find Book**
- Enter a book title to search for it
- Shows the author and how many copies are available
- Says "doesn't exist" if it's not in the system

**4. Borrow Book**
- Enter the user name and book title
- Only works if:
  - The user is registered
  - The book exists
  - There are copies available
  - The user doesn't already have that book

**5. Return Book**
- Enter user name and book title
- Updates everything when they return it

**6. Borrowed Books**
- Shows all the books that are currently borrowed

**7. Exit**
- Quits the program

After each action, you can either go back to the main menu or exit.

## How the Data is Stored

The program keeps everything in memory using Python dictionaries (it doesn't save to files).

Books are stored like this:
```python
books = {
    "book_title": [author, total_copies, copies_currently_borrowed]
}
```

Users are stored like this:
```python
users = {
    "user_name": [user_id, [list_of_books_they_borrowed]]
}
```

## Example of Using It

**Adding a book:**
```
Enter Book Title: Harry Potter
Author Name: J.K. Rowling  
Enter num of Copies: 3
```
Output: `Added new book Harry Potter with total number of copies of 3`

**Registering someone:**
```
Enter User Name: Alice
```
Output: `Registered new user: Alice with user_id 123456`

**Borrowing a book:**
```
Enter User Name: Alice
Enter Book Title: Harry Potter
```
Output: `User Alice successfully borrowed book Harry Potter`

## 🛡️ Robust Error Handling & Validation

The program has **comprehensive error handling** that prevents crashes and provides clear feedback:

### **Input Validation**
- **Empty inputs**: `Error: Book title cannot be empty`
- **Whitespace-only inputs**: `Error: User name cannot be empty`
- **Invalid numbers**: `Error: Number of copies must be a valid positive number`
- **Negative quantities**: `Error: Number of copies must be a positive number`

### **Business Logic Validation**
- **Unregistered users**: `There is no User Alice in the system pls create user first`
- **Non-existent books**: `Book Title Python doesn't exist in our book system`
- **Duplicate borrowing**: `User Already has a loan copy of Python Programming`
- **Invalid returns**: `User Alice doesn't have Python Programming to return`
- **Out of stock**: `Book Python Programming is out of stock all copies are on loan`

### **System Robustness**
- **Menu input errors**: Program continues and asks again instead of crashing
- **Graceful recovery**: All operations wrapped in try-catch blocks
- **Clear error messages**: Users understand exactly what went wrong
- **Data integrity**: Invalid data never enters the system

## What You Need to Run It

- Just Python 3 (no special libraries needed)
- All the project files in the same folder

The files are:
```
project-oop-library-management-system/
├── __init__.py
├── main.py  
├── classes_lib_system.py
├── functions.py
└── README.md
```

## Future Enhancement Ideas

Some ideas for further improvements:
- **Data Persistence**: Save data to JSON/database files
- **Due Dates**: Add borrowing periods and overdue tracking  
- **Advanced Search**: Search by author, category, or keywords
- **User Limits**: Maximum books per user policies
- **GUI Interface**: Web or desktop interface
- **Categories & Genres**: Book classification system
- **Admin Features**: User management and reporting
- **API Integration**: Connect to external book databases

## Technical Learning Outcomes

This project demonstrates **advanced Python concepts**:

### **Design Patterns**
- ✅ **Singleton Pattern**: Ensures single Library instance
- ✅ **Defensive Programming**: Comprehensive input validation
- ✅ **Error Handling**: Graceful failure and recovery

### **Object-Oriented Programming**
- ✅ **Class Design**: Well-structured Library class
- ✅ **Method Organization**: Logical separation of concerns  
- ✅ **Data Encapsulation**: Private helper methods (`_validate_input`)

### **Software Engineering Practices**
- ✅ **Input Validation**: Prevents invalid data entry
- ✅ **Error Recovery**: Program continues despite errors
- ✅ **User Experience**: Clear, helpful error messages
- ✅ **Code Organization**: Modular file structure

---

**This project showcases production-ready code patterns and robust software engineering practices, going far beyond basic Python programming to demonstrate professional development techniques.**