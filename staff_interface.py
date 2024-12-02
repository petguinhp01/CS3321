"""
File: staff_interface.py
Description: Staff interface for managing bookings, availability, and logout.
Authors: Nhan Nguyen (Enhanced), Michael M.
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from staff_backend import get_staff_bookings, get_staff_availability, set_staff_availability, delete_staff_availability


def staff_interface(staff_name):
    """
    Displays the staff dashboard for managing bookings, availability, and logging out.

    Parameters:
        staff_name (str): The name of the staff member.
    """

    def refresh_booking_list():
        """
        Refreshes the list of bookings assigned to the staff.
        """
        try:
            bookings = get_staff_bookings(staff_name)
            for item in booking_tree.get_children():
                booking_tree.delete(item)
            for booking in bookings:
                booking_tree.insert("", "end", values=booking)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh bookings: {e}")

    def refresh_availability_list():
        """
        Refreshes the list of the staff's availability.
        """
        try:
            availability = get_staff_availability(staff_name)
            for item in availability_tree.get_children():
                availability_tree.delete(item)
            for avail in availability:
                availability_tree.insert("", "end", values=avail)  # Properly add rows
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh availability: {e}")

    def add_availability():
        """
        Adds a new availability slot for the staff member.
        """
        day = calendar.get_date()
        time_slot = time_var.get()
        if not day or not time_slot:
            messagebox.showerror("Error", "Day and Time Slot cannot be blank!")
            return
        try:
            set_staff_availability(staff_name, day, time_slot)
            refresh_availability_list()
            time_var.set("")  # Clear time slot entry
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add availability: {e}")

    def delete_availability():
        """
        Deletes the selected availability slot.
        """
        selected_item = availability_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No availability slot selected!")
            return
        try:
            selected_availability = availability_tree.item(selected_item, "values")
            delete_staff_availability(staff_name, selected_availability[1], selected_availability[2])
            refresh_availability_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete availability: {e}")

    def logout():
        """
        Logs the staff member out and returns to the login interface.
        """
        try:
            window.destroy()
            from login_interface import main_interface
            main_interface()
        except Exception as e:
            print(f"Error during logout: {e}")

    # Create the window
    window = tk.Tk()
    window.title(f"Staff Dashboard - {staff_name}")
    window.geometry("900x650")

    # Booking section
    tk.Label(window, text="Bookings", font=("Arial", 14, "bold")).pack(pady=5)
    booking_tree = ttk.Treeview(
        window, columns=("ID", "Service", "Date", "Time", "Status"), show="headings", height=5
    )
    for col in ("ID", "Service", "Date", "Time", "Status"):
        booking_tree.heading(col, text=col)
    booking_tree.pack(fill=tk.X, pady=5)
    refresh_booking_list()

    # Availability section
    tk.Label(window, text="Availability", font=("Arial", 14, "bold")).pack(pady=5)
    availability_tree = ttk.Treeview(
        window, columns=("Staff Name", "Day", "Time Slot"), show="headings", height=5
    )
    for col in ("Staff Name", "Day", "Time Slot"):
        availability_tree.heading(col, text=col)
    availability_tree.pack(fill=tk.X, pady=5)
    refresh_availability_list()

    # Add availability form
    tk.Label(window, text="Add Availability", font=("Arial", 12, "bold")).pack(pady=10)
    form_frame = tk.Frame(window)
    form_frame.pack(pady=5)

    # Calendar and Time Entry
    tk.Label(form_frame, text="Day:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
    calendar = Calendar(form_frame, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Time Slot (e.g., 10:00-14:00):", font=("Arial", 12)).grid(
        row=1, column=0, padx=5, pady=5, sticky="e"
    )
    time_var = tk.StringVar()
    time_entry = ttk.Combobox(
        form_frame,
        textvariable=time_var,
        values=["09:00-12:00", "12:00-15:00", "15:00-18:00"],
    )
    time_entry.grid(row=1, column=1, padx=5, pady=5)

    # Buttons
    button_frame = tk.Frame(form_frame)
    button_frame.grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(button_frame, text="Add Availability", command=add_availability).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Delete Selected Availability", command=delete_availability).grid(row=0, column=1, padx=5)
    tk.Button(window, text="Logout", command=logout).pack(pady=10)

    window.mainloop()
