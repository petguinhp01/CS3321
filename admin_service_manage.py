"""
File: admin_service_manage.py
Description: Admin functionality for managing services.
Authors: Nhan Nguyen (Revised)
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox
from service_backend import add_service, edit_service, delete_service, get_services


def manage_services():
    """
    Displays the admin interface for managing services.
    """
    def refresh_service_list():
        """
        Refreshes the list of services displayed in the interface.
        """
        try:
            services = get_services()
            for item in service_tree.get_children():
                service_tree.delete(item)
            for service in services:
                service_tree.insert("", "end", values=service)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh services: {e}")

    def add_new_service():
        """
        Adds a new service to the system.
        """
        try:
            name = entry_name.get()
            category = entry_category.get()
            hours = entry_hours.get()
            minutes = entry_minutes.get()
            price = entry_price.get()

            if not all([name, category, hours, minutes, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            # Validate duration
            try:
                hours = int(hours)
                minutes = int(minutes)
                if hours < 0 or minutes < 0 or minutes >= 60:
                    raise ValueError("Invalid duration values!")
            except ValueError:
                messagebox.showerror("Error", "Duration must be valid integers (hours >= 0, 0 <= minutes < 60)!")
                return

            duration = f"{hours}h {minutes}m"

            # Validate price
            try:
                price = float(price)
                if price < 0:
                    raise ValueError("Price cannot be negative!")
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid positive number!")
                return

            add_service(name, category, duration, price)
            refresh_service_list()
            clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add service: {e}")

    def edit_selected_service():
        """
        Edits the selected service in the system.
        """
        try:
            selected_item = service_tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No service selected!")
                return
            selected_service = service_tree.item(selected_item, "values")

            name = entry_name.get()
            category = entry_category.get()
            hours = entry_hours.get()
            minutes = entry_minutes.get()
            price = entry_price.get()

            if not all([name, category, hours, minutes, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            # Validate duration
            try:
                hours = int(hours)
                minutes = int(minutes)
                if hours < 0 or minutes < 0 or minutes >= 60:
                    raise ValueError("Invalid duration values!")
            except ValueError:
                messagebox.showerror("Error", "Duration must be valid integers (hours >= 0, 0 <= minutes < 60)!")
                return

            duration = f"{hours}h {minutes}m"

            # Validate price
            try:
                price = float(price)
                if price < 0:
                    raise ValueError("Price cannot be negative!")
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid positive number!")
                return

            edit_service(selected_service[0], name, category, duration, price)
            refresh_service_list()
            clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to edit service: {e}")

    def delete_selected_service():
        """
        Deletes the selected service from the system.
        """
        try:
            selected_item = service_tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No service selected!")
                return
            selected_service = service_tree.item(selected_item, "values")
            delete_service(selected_service[0])  # Delete by service name
            refresh_service_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete service: {e}")

    def clear_entries():
        """
        Clears the input fields for adding or editing services.
        """
        entry_name.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_hours.delete(0, tk.END)
        entry_minutes.delete(0, tk.END)
        entry_price.delete(0, tk.END)

    # Create the window
    window = tk.Tk()
    window.title("Manage Services")
    window.geometry("700x500")

    # Services label
    tk.Label(window, text="Services", font=("Arial", 16, "bold")).pack(pady=10)

    # Treeview for services
    service_tree = ttk.Treeview(
        window,
        columns=("Name", "Category", "Duration", "Price"),
        show="headings"
    )
    for col in ("Name", "Category", "Duration", "Price"):
        service_tree.heading(col, text=col)
    service_tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # Refresh the service list on load
    refresh_service_list()

    # Add/Edit service form
    form_frame = tk.Frame(window)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = tk.Entry(form_frame, width=25)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Category:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_category = tk.Entry(form_frame, width=25)
    entry_category.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Duration (Hours):", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_hours = tk.Entry(form_frame, width=5)
    entry_hours.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(form_frame, text="Minutes:", font=("Arial", 12)).grid(row=2, column=2, padx=5, pady=5, sticky="e")
    entry_minutes = tk.Entry(form_frame, width=5)
    entry_minutes.grid(row=2, column=3, padx=5, pady=5, sticky="w")

    tk.Label(form_frame, text="Price:", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_price = tk.Entry(form_frame, width=15)
    entry_price.grid(row=3, column=1, padx=5, pady=5)

    # Buttons for actions
    action_frame = tk.Frame(window)
    action_frame.pack(pady=10)

    tk.Button(action_frame, text="Add Service", command=add_new_service, font=("Arial", 12), width=15).grid(row=0, column=0, padx=10)
    tk.Button(action_frame, text="Edit Service", command=edit_selected_service, font=("Arial", 12), width=15).grid(row=0, column=1, padx=10)
    tk.Button(action_frame, text="Delete Service", command=delete_selected_service, font=("Arial", 12), width=15).grid(row=0, column=2, padx=10)

    window.mainloop()
