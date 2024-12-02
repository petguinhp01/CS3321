"""
File: admin_booking_manage.py
Description: Admin functionality for managing bookings.
Authors: Nhan Nguyen (Revised)
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox
from booking_backend import get_all_bookings, cancel_booking


def manage_bookings():
    """
    Displays the admin interface for managing bookings.
    """
    def refresh_booking_list():
        """
        Refreshes the list of bookings displayed in the interface.
        """
        try:
            bookings = get_all_bookings()
            for item in booking_tree.get_children():
                booking_tree.delete(item)
            for booking in bookings:
                booking_tree.insert("", "end", values=booking)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh bookings: {e}")

    def cancel_selected_booking():
        """
        Cancels the selected booking.
        """
        try:
            selected_item = booking_tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No booking selected!")
                return
            booking_id = booking_tree.item(selected_item[0], "values")[0]
            cancel_booking(booking_id)
            refresh_booking_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to cancel booking: {e}")

    # Create the window
    window = tk.Tk()
    window.title("Manage Bookings")

    # Bookings label
    tk.Label(window, text="Bookings", font=("Arial", 14)).pack(pady=10)

    # Treeview for bookings
    booking_tree = ttk.Treeview(
        window,
        columns=("ID", "Customer", "Service", "Date", "Time", "Staff", "Status"),
        show="headings"
    )
    for col in ("ID", "Customer", "Service", "Date", "Time", "Staff", "Status"):
        booking_tree.heading(col, text=col)
    booking_tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # Refresh the booking list on load
    refresh_booking_list()

    # Cancel booking button
    tk.Button(window, text="Cancel Booking", command=cancel_selected_booking, font=("Arial", 12)).pack(pady=10)

    window.mainloop()
