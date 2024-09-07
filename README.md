# Currency Converter Application

This project is a Currency Converter application built using PyQt6 for the graphical user interface. It includes a login system, a currency converter with various features, and a standalone executable created with PyInstaller.

## Features

- **Login System:** Secure login with hardcoded credentials.
- **Currency Converter:** Convert between GEL, USD, and EUR with a graphical interface.
- **Styling:** Modern look with custom styling and background images.
- **Standalone Executable:** Built using PyInstaller for easy distribution.

## Requirements

- Python 3.10 or later
- PyQt6 (or PyQt5, but not both)
- PyInstaller (for creating standalone executable)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. **Set up an environment:**
   python -m venv .venv
   source .venv/bin/activate
3. **Install requirements**
   pip install -r requirements.txt
4. **Run the application**
   python main.py

Login:

  Use the credentials:
  Username: admin
  Password: admin
  Click the Login button to access the currency converter.

Currency Conversion:

  Select the "From Currency" and "To Currency" from the dropdown menus.
  Enter the amount you want to convert.
  Click the Convert button to see the result.
  Clear Fields:

  Click the Clear button to reset the input fields and selection.
Logout:

  Click the Logout button to return to the login page.


Project Structure
  The project consists of the following main components:

  main.py: The main Python script for the application.
  login.ui: UI file for the login window.
  currency_converter.ui: UI file for the currency converter window.
  background.jpg: Background image used in the currency converter window.
  requirements.txt: File listing the project dependencies.
  dist/: Directory containing the standalone executable after building with PyInstaller.


Code Explanation
  file: main.py
  LoginWindow Class: Handles user authentication and navigation to the currency converter.
  CurrencyConverterWindow Class: Manages currency conversion and UI interactions.













  
