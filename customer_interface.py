"""
File: customer_interface.py
Description: Customer interface for booking services with improved layout and logout functionality.
Authors: Quan, Samira
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from booking_backend import save_booking, get_customer_bookings
from customer_service_interface import customer_service_interface  # Import the service selection interface


def customer_interface(customer_name):
    """
    Displays the customer dashboard for booking services and viewing booking history.

    Parameters:
        customer_name (str): The name of the customer.
    """
    selected_services = []

    def book_service():
        """
        Books a new service for the customer.
        """
        try:
            date = calendar.get_date()
            time = time_var.get()
            staff = staff_var.get()

            if not selected_services:
                messagebox.showerror("Error", "No services selected!")
                return
            if not date or not time:
                messagebox.showerror("Error", "Date and Time are required!")
                return

            # Save booking for each selected service
            for service in selected_services:
                save_booking(customer_name, service, date, time, staff)
            messagebox.showinfo("Success", "Service(s) booked successfully!")
            refresh_history()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to book service(s): {e}")

    def refresh_history():
        """
        Refreshes the booking history displayed in the interface.
        """
        try:
            history = get_customer_bookings(customer_name)
            for item in history_tree.get_children():
                history_tree.delete(item)
            for record in history:
                history_tree.insert("", "end", values=record)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh booking history: {e}")

    def open_service_selection():
        """
        Opens the service selection interface.
        """
        def handle_service_selection(services):
            nonlocal selected_services
            selected_services = services
            service_label.config(text=f"Selected Services: {', '.join(selected_services)}")

        customer_service_interface(on_selection_done=handle_service_selection)

    def logout():
        """
        Logs the customer out and returns to the main interface.
        """
        try:
            window.destroy()
            from login_interface import main_interface
            main_interface()
        except Exception as e:
            print(f"Error during logout: {e}")

    # Create the window
    window = tk.Tk()
    window.title(f"Customer Dashboard - {customer_name}")
    window.geometry("900x650")

    # Dashboard title
    tk.Label(window, text="Customer Dashboard", font=("Arial", 16, "bold")).pack(pady=10)

    # Booking form
    form_frame = tk.Frame(window)
    form_frame.pack(pady=10, fill=tk.X)

    tk.Label(form_frame, text="Selected Services:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    service_label = tk.Label(form_frame, text="None", font=("Arial", 12), width=40, anchor="w")
    service_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    tk.Button(form_frame, text="Select Services", command=open_service_selection, font=("Arial", 12), width=15).grid(row=0, column=2, padx=10)

    # Calendar and Time Selection
    tk.Label(form_frame, text="Date:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    calendar = Calendar(form_frame, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(form_frame, text="Time Slot:", font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=5, sticky="e")
    time_var = tk.StringVar()
    time_dropdown = ttk.Combobox(
        form_frame,
        textvariable=time_var,
        values=["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
    )
    time_dropdown.set("Select Time")
    time_dropdown.grid(row=1, column=3, padx=5, pady=5)

    # Optional staff selection
    tk.Label(form_frame, text="Staff (Optional):", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    staff_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=staff_var, width=30).grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Buttons horizontally aligned
    button_frame = tk.Frame(form_frame)
    button_frame.grid(row=3, column=0, columnspan=4, pady=10)

    tk.Button(button_frame, text="Book Service", command=book_service, font=("Arial", 12), width=15).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Logout", command=logout, font=("Arial", 12), width=15).grid(row=0, column=1, padx=10)

    # Booking history section
    tk.Label(window, text="Booking History", font=("Arial", 14, "bold")).pack(pady=10)
    history_tree = ttk.Treeview(
        window,
        columns=("Booking ID", "Service", "Date", "Time", "Staff", "Status"),
        show="headings"
    )
    for col in ("Booking ID", "Service", "Date", "Time", "Staff", "Status"):
        history_tree.heading(col, text=col)
    history_tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # Refresh the booking history on load
    refresh_history()

    window.mainloop()
