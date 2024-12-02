"""
File: create_account.py
Description: Allows new users to create accounts in the unified database.
Authors: Nhan Nguyen (Revised)
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import messagebox
from utils import save_user


def create_account_interface():
    """
    Displays the Create Account interface for registering a new user.
    """
    def register():
        username = entry_username.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()
        role = entry_role.get().strip().capitalize()

        # Validation
        if not username or not password or not confirm_password or not role:
            messagebox.showerror("Error", "All fields are required!")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long!")
            return
        if role not in ["Admin", "Staff", "Customer"]:
            messagebox.showerror("Error", "Role must be Admin, Staff, or Customer!")
            return

        try:
            # Save user details in the 'User' sheet of the unified data file
            save_user(username, password, role)
            messagebox.showinfo("Success", "Account created successfully!")
            account_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create account: {e}")

    # Create Account window
    account_window = tk.Tk()
    account_window.title("Create Account - Beauty Service Booking System")
    account_window.geometry("400x350")  # Adjusted size for better layout
    account_window.resizable(False, False)

    # Frame for layout alignment
    frame = tk.Frame(account_window, padx=20, pady=20)
    frame.pack(expand=True)

    # Create Account Form
    tk.Label(frame, text="Username:", font=("Arial", 12)).grid(row=0, column=0, pady=10, sticky="e")
    entry_username = tk.Entry(frame, width=25)
    entry_username.grid(row=0, column=1, pady=10)

    tk.Label(frame, text="Password:", font=("Arial", 12)).grid(row=1, column=0, pady=10, sticky="e")
    entry_password = tk.Entry(frame, show="*", width=25)
    entry_password.grid(row=1, column=1, pady=10)

    tk.Label(frame, text="Confirm Password:", font=("Arial", 12)).grid(row=2, column=0, pady=10, sticky="e")
    entry_confirm_password = tk.Entry(frame, show="*", width=25)
    entry_confirm_password.grid(row=2, column=1, pady=10)

    tk.Label(frame, text="Role:", font=("Arial", 12)).grid(row=3, column=0, pady=10, sticky="e")
    entry_role = tk.Entry(frame, width=25)
    entry_role.grid(row=3, column=1, pady=10)

    # Register Button
    tk.Button(frame, text="Register", command=register, width=15, font=("Arial", 12)).grid(row=4, column=1, pady=20)

    account_window.mainloop()
