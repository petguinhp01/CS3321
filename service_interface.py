"""
File: service_interface.py
Description: Displays services for all roles. Admins can manage services, while others can only view them.
Authors: Nhan Nguyen (Revised), Abel Thomas
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox
from service_backend import add_service, edit_service, delete_service, get_services


def service_interface(role):
    """
    Displays the service interface based on the user's role.

    Parameters:
        role (str): The role of the user (e.g., "Admin", "Customer", "Staff").
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
            duration = entry_duration.get()
            price = entry_price.get()

            if not all([name, category, duration, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            add_service(name, category, duration, float(price))
            refresh_service_list()
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
            duration = entry_duration.get()
            price = entry_price.get()

            if not all([name, category, duration, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            edit_service(selected_service[0], name, category, duration, float(price))  # Edit by service name
            refresh_service_list()
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

    # Create the window
    window = tk.Tk()
    window.title("Service Interface")

    # Services label
    tk.Label(window, text="Services", font=("Arial", 14)).pack(pady=10)

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

    if role == "Admin":
        # Admin-specific functionality
        tk.Label(window, text="Add/Edit Service", font=("Arial", 12)).pack(pady=10)
        tk.Label(window, text="Name").pack()
        entry_name = tk.Entry(window)
        entry_name.pack()
        tk.Label(window, text="Category").pack()
        entry_category = tk.Entry(window)
        entry_category.pack()
        tk.Label(window, text="Duration").pack()
        entry_duration = tk.Entry(window)
        entry_duration.pack()
        tk.Label(window, text="Price").pack()
        entry_price = tk.Entry(window)
        entry_price.pack()

        tk.Button(window, text="Add Service", command=add_new_service, font=("Arial", 12)).pack(pady=5)
        tk.Button(window, text="Edit Service", command=edit_selected_service, font=("Arial", 12)).pack(pady=5)
        tk.Button(window, text="Delete Service", command=delete_selected_service, font=("Arial", 12)).pack(pady=5)

    elif role == "Customer":
        # Customer-specific functionality
        tk.Label(window, text="Select a service and proceed to booking.", font=("Arial", 12)).pack(pady=10)

    elif role == "Staff":
        # Staff-specific functionality
        tk.Label(window, text="View available services to assist customers.", font=("Arial", 12)).pack(pady=10)

    window.mainloop()
