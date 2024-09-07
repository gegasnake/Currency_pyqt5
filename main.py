import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QLabel, QPushButton, QLineEdit
from PyQt6 import uic
from PyQt6.QtGui import QFont
import warnings

# I ignore DeprecationWarnings because it's a problem of the version, not my code
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin"

# Currency exchange rates for GEL, EURO, and USD
exchange_rates = {
    "USD": {"EUR": 0.93, "GEL": 2.85},
    "EUR": {"USD": 1.08, "GEL": 3.07},
    "GEL": {"USD": 0.35, "EUR": 0.33}
}


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)  # Load the login UI design
        self.setWindowTitle("Login - Currency Converter")

        # Style the login window background
        self.setStyleSheet("""
            background-color: #2E3440;
            color: #D8DEE9;
            font-family: Arial, sans-serif;
        """)

        # Set up the login button
        self.LoginButton.setStyleSheet("""
            QPushButton {
                background-color: #88C0D0;
                color: #2E3440;
                font-size: 14px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #5E81AC;
            }
        """)

        # When the login button is clicked, call the handle_login function
        self.LoginButton.clicked.connect(self.handle_login)

    def handle_login(self):
        """ This function handles the login by checking credentials """
        username = self.usernameInput.text()
        password = self.passwordInput.text()

        if username == USERNAME and password == PASSWORD:
            self.open_converter_page()
        else:
            QMessageBox.warning(self, 'Error', 'Incorrect Username or Password')

    def open_converter_page(self):
        self.currency_converter_window = CurrencyConverterWindow()
        self.currency_converter_window.show()
        self.close()


class CurrencyConverterWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('currency_converter.ui', self)  # Load the converter UI design
        self.setWindowTitle("Currency Converter")

        # Set the stylesheet for the background image
        self.setStyleSheet("""
               QMainWindow {
                   background-position: center;
                   background-repeat: no-repeat;
               }
               QLabel {
                   color: black;
                   font-size: 14px;
               }
           """)

        # Style the combo boxes (frombox, tobox)
        self.frombox.setStyleSheet("""
               QComboBox {
                   background-color: #4C566A;
                   color: black;
                   border: 1px solid #81A1C1;
                   padding: 5px;
                   border-radius: 5px;
                   font-size: 14px;
               }
           """)
        self.tobox.setStyleSheet("""
               QComboBox {
                   background-color: #4C566A;
                   color: black;
                   border: 1px solid #81A1C1;
                   padding: 5px;
                   border-radius: 5px;
                   font-size: 14px;
               }
           """)



        # Style the buttons (convert, clear, and logout)
        self.convertButton.setStyleSheet("""
               QPushButton {
                   background-color: #A3BE8C;
                   color: #2E3440;
                   font-size: 16px;
                   border-radius: 10px;
                
               }
               QPushButton:hover {
                   background-color: #8FBCBB;
               }
           """)

        self.clearButton.setStyleSheet("""
               QPushButton {
                   background-color: #BF616A;
                   color: black;
                   font-size: 16px;
                   border-radius: 10px;
            
               }
               QPushButton:hover {
                   background-color: #D08770;
               }
           """)

        self.logoutButton.setStyleSheet("""
               QPushButton {
                   background-color: #81A1C1;
                   color: #2E3440;
                   font-size: 16px;
                   border-radius: 10px;
                 
               }
               QPushButton:hover {
                   background-color: #5E81AC;
               }
           """)

        # Set the font for the result label
        self.resultLabel.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.resultLabel.setStyleSheet("color: #88C0D0;")

        # Populate combo boxes with available currencies
        currencies = list(exchange_rates.keys())

        # Clear existing items to prevent duplicates
        self.frombox.clear()
        self.tobox.clear()

        # Add items to combo boxes
        self.frombox.addItems(currencies)
        self.tobox.addItems(currencies)

        # Connect buttons to their respective functions
        self.convertButton.clicked.connect(self.convert_currency)
        self.clearButton.clicked.connect(self.clear)
        self.logoutButton.clicked.connect(self.handle_logout)

        self.frombox.setCurrentText("GEL")
        self.tobox.setCurrentText("EUR")

    def convert_currency(self):
        """ This function converts from one currency to another based on exchange rates """
        try:
            from_currency = self.frombox.currentText()
            to_currency = self.tobox.currentText()
            amount = float(self.amountInput.text())

            if from_currency == to_currency:
                converted_amount = amount
            else:
                converted_amount = amount * exchange_rates[from_currency][to_currency]

            self.resultLabel.setText(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter a valid amount')

    def clear(self):
        """ This function clears the input fields and resets the selection """
        self.frombox.setCurrentText("GEL")
        self.tobox.setCurrentText("EUR")
        self.amountInput.clear()
        self.resultLabel.clear()

    def handle_logout(self):
        """ This function logs out the user and returns to the login page """
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


# Entry point for the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
