# 📚 Library Management System

A comprehensive Python-based library management system featuring database integration, intelligent search capabilities, and a user-friendly command-line interface. This system leverages modern technologies including AI-powered natural language queries and robust MySQL database management.

## ✨ Key Features

### Core Library Operations

- **📖 Book Management**: Add new books to the library catalog with automatic duplicate handling
- **👤 User Registration**: Register new library members with unique user identification
- **🔍 Book Search**: Find books by title with real-time availability information
- **📋 Loan Tracking**: Monitor all currently borrowed books with detailed statistics

### Advanced Borrowing System

- **📚 Book Borrowing**: Intelligent borrowing system with availability verification
- **🔄 Book Returns**: Streamlined return process with automatic loan status updates
- **⏰ Loan Management**: 14-day automatic loan periods with date tracking
- **📊 Availability Tracking**: Real-time inventory management with copy counting

### AI-Powered Features

- **🤖 Smart Search**: Natural language query interface powered by Ollama LLM
- **🧠 Intelligent SQL Generation**: Convert plain English questions into database queries
- **📈 Advanced Analytics**: Ask complex questions about library usage patterns

### Technical Highlights

- **🔄 Singleton Pattern**: Ensures consistent library instance across the application
- **✅ Input Validation**: Comprehensive validation for all user inputs
- **🛡️ Error Handling**: Robust error management with user-friendly messaging
- **🔒 Security**: SQL injection protection and read-only query enforcement

## 🛠️ Technology Stack

- **Backend**: Python 3.13+
- **Database**: MySQL with mysql-connector-python
- **AI/ML**: Ollama (Local LLM integration)
- **Configuration**: Pydantic Settings with environment file management
- **Package Management**: UV (modern Python package manager)
- **Testing**: Pytest framework

## 🚀 Quick Start

### Prerequisites

- **Python 3.13+** installed on your system
- **MySQL Server** running locally or remotely
- **Ollama** installed for AI features (optional)
- **UV package manager** (recommended) or pip

### Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:mahmoudmoe84/Library_Management_system_w_db.git
   cd Library_Management_system_w_db
   ```

2. **Install Dependencies**

   ```bash
   # Using UV (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Database Setup**

   ```bash
   # Copy environment template
   cp db/example.env db/setting.env
   
   # Edit the configuration file with your database credentials
   nano db/setting.env
   ```

4. **Configure Environment Variables**

   ```env
   DB_HOST=localhost
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_DATABASE=library_db
   DB_PORT=3306
   ```

5. **Create Database Schema**

   ```sql
   -- Create the database
   CREATE DATABASE library_db;
   
   -- Create tables (run the SQL scripts provided)
   USE library_db;
   -- [Include your table creation scripts here]
   ```

6. **Launch the Application**

   ```bash
   python src/main.py
   ```

## 📁 Project Architecture

```text
Library_Management_system_w_db/
├── 📂 src/                          # Application source code
│   ├── main.py                      # Main application entry point
│   ├── classes_lib_system.py        # Core Library class with singleton pattern
│   ├── functions.py                 # Utility functions and UI helpers
│   └── llm_service.py              # AI/LLM integration service
├── 📂 db/                           # Database layer
│   ├── __init__.py                  # Package initialization
│   ├── config.py                    # Pydantic settings configuration
│   ├── db_connection.py             # MySQL connection management
│   ├── test_connection.py           # Database connectivity tests
│   ├── example.env                  # Environment template
│   └── setting.env                  # Your database credentials (create this)
├── 📂 __pycache__/                  # Python bytecode cache
├── Makefile                         # Build and development commands
├── pyproject.toml                   # Project configuration and dependencies
├── uv.lock                          # Dependency lock file
└── README.md                        # This documentation
```

## 🎯 Usage Guide

### Main Menu Options

When you run the application, you'll see an interactive menu:

```text
Welcome to the library management system
Below are the options you have
1- Add Book
2- Add User
3- Find Book
4- Borrow Book
5- Return Book
6- Borrowed Books
7- Use Smart Search via LLM
8- Exit
```

### Feature Walkthrough

#### 📖 Adding Books

- Enter book title, author name, and number of copies
- System automatically handles duplicate titles by updating copy counts
- Validates all inputs for completeness and correctness

#### 👤 User Management

- Register new users with unique names
- System prevents duplicate user registrations
- Automatic user ID generation

#### 🔍 Book Search & Availability

- Search for books by exact title match
- View real-time availability (total copies vs. loaned copies)
- Get instant feedback on book existence

#### 📚 Borrowing System

- Borrow books with automatic availability checking
- 14-day loan period with automatic due date calculation
- Comprehensive validation (user exists, book available, etc.)

#### 🤖 Smart Search (AI-Powered)

Ask natural language questions like:

- "Who has borrowed books?"
- "Which books are overdue?"
- "How many copies of each book do we have?"
- "Show me all users who haven't returned books"

## 🔧 Configuration

### Database Settings

The system uses Pydantic Settings for configuration management:

```python
class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_PORT: int
```

### Environment File

Create `db/setting.env` with your database credentials:

```env
DB_HOST=localhost
DB_USER=library_admin
DB_PASSWORD=secure_password
DB_DATABASE=library_management
DB_PORT=3306
```

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Test database connectivity
python db/test_connection.py

# Run full test suite (if available)
pytest
```

## 🚀 Advanced Features

### AI Integration

The system integrates with Ollama for natural language processing:

- Converts user questions to SQL queries
- Provides intelligent search capabilities
- Handles complex database relationships

### Security Features

- Input validation and sanitization
- SQL injection protection
- Read-only query enforcement for AI features
- Comprehensive error handling

### Performance Optimizations

- Singleton pattern for consistent state management
- Efficient database connection handling
- Optimized SQL queries with proper indexing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section below
2. Review the error messages for specific guidance
3. Ensure your database connection is properly configured
4. Verify all dependencies are installed correctly

## 🔧 Troubleshooting

### Common Issues

#### Database Connection Errors

- Verify MySQL server is running
- Check credentials in `setting.env`
- Ensure database exists

#### Missing Dependencies

```bash
uv sync  # Reinstall all dependencies
```

#### AI Features Not Working

- Install Ollama: `curl -fsSL https://ollama.ai/install.sh | sh`
- Pull the required model: `ollama pull llama3`

---

Built with ❤️ using Python, MySQL, and modern development practices

## Usage

Run the program and follow the menu options:

1. Add books with title, author, and quantity
2. Register new users (gets auto-generated ID)
3. Search for books and check availability  
4. Borrow books (validates user and availability)
5. Return books
6. View borrowed books

## Technologies

- **Python 3** - Core programming language
- **MySQL** - Database storage
- **Pydantic Settings** - Configuration management
- **mysql-connector-python** - Database connectivity

## Contributing

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is for educational purposes.