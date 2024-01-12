# main.py
import tkinter as tk
from database import setup_database
from login import create_login_screen

def main():
    # Initialize the database
    setup_database()

    # Start the login screen
    create_login_screen()

if __name__ == "__main__":
    main()
