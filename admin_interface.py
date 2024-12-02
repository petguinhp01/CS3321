"""
File: admin_interface.py
Description: Admin interface for managing the system (services, staff, and bookings).
Authors: Nhan Nguyen (Enhanced)
Date: 12/01/2024
"""

import tkinter as tk
from admin_service_manage import manage_services
from admin_staff_manage import manage_staff
from admin_booking_manage import manage_bookings


def admin_interface(admin_name):
    """
    Displays the admin dashboard, providing access to manage services, staff, and bookings.

    Parameters:
        admin_name (str): The username of the admin.
    """
    def logout():
        """
        Logs the admin out and returns to the main interface.
        """
        try:
            window.destroy()
            from login_interface import main_interface
            main_interface()
        except Exception as e:
            print(f"Error during logout: {e}")

    # Create the admin interface window
    window = tk.Tk()
    window.title(f"Admin Dashboard - {admin_name}")
    window.geometry("600x400")  # Wider window for a better layout

    # Dashboard title
    tk.Label(window, text="Admin Dashboard", font=("Arial", 20, "bold")).pack(pady=20)

    # Management buttons
    tk.Button(window, text="Manage Services", command=manage_services, font=("Arial", 14), width=25).pack(pady=10)
    tk.Button(window, text="Manage Staff", command=manage_staff, font=("Arial", 14), width=25).pack(pady=10)
    tk.Button(window, text="Manage Bookings", command=manage_bookings, font=("Arial", 14), width=25).pack(pady=10)

    # Logout button
    tk.Button(window, text="Logout", command=logout, font=("Arial", 14), width=25).pack(pady=20)

    window.mainloop()
