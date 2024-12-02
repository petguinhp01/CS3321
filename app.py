"""
File: app.py
Description: Main entry point for the Beauty Service Booking System.
Authors: Nhan Nguyen (Revised)
Date: 12/01/2024
"""

from login_interface import main_interface
from data_manager import initialize_data_file

if __name__ == "__main__":
    try:
        # Ensure the unified database file is initialized
        initialize_data_file()
        # Launch the main login interface
        main_interface()
    except Exception as e:
        print(f"An error occurred while running the application: {e}")
