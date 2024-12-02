"""
File: customer_service_interface.py
Description: Customer interface for viewing and selecting services.
Authors: Quan, Samira
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox
from service_backend import get_services


def customer_service_interface(on_selection_done):
    """
    Displays the customer service selection interface.

    Parameters:
        on_selection_done (function): A callback function to handle the selected services.
    """
    selected_services = []

    def add_selected_service():
        """
        Adds the selected service to the list.
        """
        try:
            selected_item = service_tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No service selected!")
                return
            selected_service = service_tree.item(selected_item, "values")
            selected_services.append(selected_service[0])  # Add service name
            selected_label.config(text=f"Selected Services: {', '.join(selected_services)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add service: {e}")

    def done_selection():
        """
        Finalizes the selection and closes the interface.
        """
        try:
            if not selected_services:
                messagebox.showerror("Error", "No services selected!")
                return
            on_selection_done(selected_services)  # Pass selected services back to the caller
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to finalize selection: {e}")

    # Create the window
    window = tk.Tk()
    window.title("Select Services")

    tk.Label(window, text="Available Services", font=("Arial", 14)).pack(pady=10)

    # Treeview for services
    service_tree = ttk.Treeview(
        window,
        columns=("Name", "Category", "Duration", "Price"),
        show="headings"
    )
    for col in ("Name", "Category", "Duration", "Price"):
        service_tree.heading(col, text=col)
    service_tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # Load services
    try:
        services = get_services()
        for service in services:
            service_tree.insert("", "end", values=service)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load services: {e}")

    # Selected services label
    selected_label = tk.Label(window, text="Selected Services: None", font=("Arial", 12))
    selected_label.pack(pady=5)

    # Action buttons
    tk.Button(window, text="Add Selected Service", command=add_selected_service, font=("Arial", 12)).pack(pady=5)
    tk.Button(window, text="Done", command=done_selection, font=("Arial", 12)).pack(pady=5)

    window.mainloop()
