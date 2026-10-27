# 📁 FileNova - File & Folder Manager

A simple, terminal-based file and folder management system built with Python. FileNova allows users to create, read, update, rename, and delete files and folders through an interactive command-line interface.

## 🎯 Problem Statement

Managing files and folders is a common task in everyday computing. FileNova aims to simplify these operations by providing a menu-driven terminal application where users can organize and manage their files efficiently.

## ✨ Features

- 📄 Create new files
- 📖 Read file contents
- ✏️ Update existing file contents
- 🗑️ Delete files
- 📂 Create folders
- 🔄 Rename files and folders
- 🧹 Delete folders
- 📋 View files and folders
- ⚠️ Handle errors and invalid operations
- 🚪 Exit the application safely

## 🛠️ Technologies Used

- **Language:** Python
- **Concepts:** File Handling, Functions, Loops, Conditional Statements, Exception Handling
- **Modules:** `pathlib` / `os`

## 📂 Project Structure

```text
FileNova/
│
├── main.py          # Main application
├── README.md        # Project documentation
└── workspace/       # Directory for file operations
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- A terminal or command prompt

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd FileNova
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## 💻 Usage

After running the application, a menu will appear in the terminal. Enter the number corresponding to the operation you want to perform and follow the instructions.

Example:

```text
================================
       FileNova Manager
================================
1. Create File
2. Read File
3. Update File
4. Delete File
5. Create Folder
6. Rename File/Folder
7. Delete Folder
8. View Directory
9. Exit
================================
Enter your choice:
```

## 📚 Learning Objectives

This project helps practice:

- Python file handling and directory management
- Writing reusable functions
- Implementing menu-driven programs
- Handling exceptions and invalid inputs
- Understanding basic CRUD operations
- Building practical command-line applications
