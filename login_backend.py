"""
File: login_backend.py
Description: Backend logic for user authentication and role assignment.
Authors: Nhan Nguyen (Revised)
Date: 12/01/2024
"""

from data_manager import read_all_rows


def authenticate_user(username, password):
    """
    Authenticates a user by their username and password.

    Parameters:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        str: The role of the user ("Admin", "Staff", "Customer") if authenticated; None otherwise.
    """
    try:
        users = read_all_rows("User")
        for user in users:
            if user[0] == username and user[1] == password:  # Match username and password
                return user[2]  # Return role (e.g., "Admin", "Staff", "Customer")
        return None
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None
