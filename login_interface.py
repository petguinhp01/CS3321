"""
File: login_interface.py
Description: Login interface and role-based routing.
Authors: Nhan Nguyen (Revised)
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import messagebox
from login_backend import authenticate_user
from admin_interface import admin_interface
from staff_interface import staff_interface
from customer_interface import customer_interface



def main_interface():
    def login():
        username = entry_username.get()
        password = entry_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Username or password cannot be blank!")
            return

        try:
            role = authenticate_user(username, password)
            if role == "Admin":
                main_window.destroy()
                admin_interface(username)
            elif role == "Staff":
                main_window.destroy()
                staff_interface(username)
            elif role == "Customer":
                main_window.destroy()
                customer_interface(username)
            else:
                messagebox.showerror("Error", "Invalid username or password!")
        except Exception as e:
            messagebox.showerror("Error", f"Authentication failed: {e}")

    def open_create_account():
        from create_account import create_account_interface
        create_account_interface()

    main_window = tk.Tk()
    main_window.title("Login - Beauty Service Booking System")
    main_window.geometry("400x300")
    main_window.resizable(False, False)

    frame = tk.Frame(main_window, padx=20, pady=20)
    frame.pack(expand=True)

    tk.Label(frame, text="Username:", font=("Arial", 12)).grid(row=0, column=0, pady=10, sticky="e")
    entry_username = tk.Entry(frame, width=25)
    entry_username.grid(row=0, column=1, pady=10)

    tk.Label(frame, text="Password:", font=("Arial", 12)).grid(row=1, column=0, pady=10, sticky="e")
    entry_password = tk.Entry(frame, show="*", width=25)
    entry_password.grid(row=1, column=1, pady=10)

    tk.Button(frame, text="Login", command=login, width=15, font=("Arial", 12)).grid(row=2, column=1, pady=20)
    tk.Label(frame, text="Don't have an account?", font=("Arial", 10)).grid(row=3, column=0, pady=5, sticky="e")
    create_account_link = tk.Label(frame, text="Create Account", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    create_account_link.grid(row=3, column=1, pady=5, sticky="w")
    create_account_link.bind("<Button-1>", lambda e: open_create_account())

    main_window.mainloop()
