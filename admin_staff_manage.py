"""
File: admin_staff_manage.py
Description: Admin functionality for managing staff.
Authors: Nhan Nguyen (Fixed)
Date: 12/01/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox
from staff_backend import add_staff, get_staff, delete_row


def manage_staff():
    """
    Displays the admin interface for managing staff.
    """
    def refresh_staff_list():
        """
        Refreshes the list of staff displayed in the interface.
        """
        try:
            staff = get_staff()  # Retrieve the updated staff list
            for item in staff_tree.get_children():
                staff_tree.delete(item)  # Clear the treeview
            for staff_member in staff:
                staff_tree.insert("", "end", values=staff_member)  # Add each staff member
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh staff list: {e}")

    def add_new_staff():
        """
        Adds a new staff member to the system and updates the interface.
        """
        try:
            name = entry_name.get().strip()
            role = entry_role.get().strip()
            email = entry_email.get().strip()

            if not all([name, role, email]):
                messagebox.showerror("Error", "All fields are required!")
                return

            add_staff(name, role, email)  # Add to backend
            clear_entries()
            refresh_staff_list()  # Refresh the UI
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add staff member: {e}")

    def edit_selected_staff():
        """
        Edits the selected staff member's information.
        """
        try:
            selected_item = staff_tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No staff member selected!")
                return
            selected_staff = staff_tree.item(selected_item, "values")

            name = entry_name.get().strip()
            role = entry_role.get().strip()
            email = entry_email.get().strip()

            if not all([name, role, email]):
                messagebox.showerror("Error", "All fields are required!")
                return

            # Update the selected staff member
            delete_row("Staff", 0, selected_staff[0])  # Remove the old entry
            add_staff(name, role, email)  # Add the updated entry
            clear_entries()
            refresh_staff_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to edit staff member: {e}")

    def delete_selected_staff():
        """
        Deletes the selected staff member from the system and updates the interface.
        """
        try:
            selected_item = staff_tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No staff member selected!")
                return
            selected_staff = staff_tree.item(selected_item, "values")
            delete_row("Staff", 0, selected_staff[0])  # Delete by staff name
            refresh_staff_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete staff member: {e}")

    def clear_entries():
        """
        Clears the input fields for adding or editing staff.
        """
        entry_name.delete(0, tk.END)
        entry_role.delete(0, tk.END)
        entry_email.delete(0, tk.END)

    # Create the window
    window = tk.Tk()
    window.title("Manage Staff")
    window.geometry("700x500")

    # Staff label
    tk.Label(window, text="Staff Management", font=("Arial", 16, "bold")).pack(pady=10)

    # Treeview for staff
    staff_tree = ttk.Treeview(
        window,
        columns=("Name", "Role", "Email"),
        show="headings"
    )
    for col in ("Name", "Role", "Email"):
        staff_tree.heading(col, text=col)
    staff_tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # Refresh the staff list on load
    refresh_staff_list()

    # Add/Edit/Delete form
    form_frame = tk.Frame(window)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = tk.Entry(form_frame, width=25)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Role:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_role = tk.Entry(form_frame, width=25)
    entry_role.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Email:", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_email = tk.Entry(form_frame, width=25)
    entry_email.grid(row=2, column=1, padx=5, pady=5)

    # Buttons for actions
    action_frame = tk.Frame(window)
    action_frame.pack(pady=10)

    tk.Button(action_frame, text="Add Staff", command=add_new_staff, font=("Arial", 12), width=15).grid(row=0, column=0, padx=10)
    tk.Button(action_frame, text="Edit Staff", command=edit_selected_staff, font=("Arial", 12), width=15).grid(row=0, column=1, padx=10)
    tk.Button(action_frame, text="Delete Staff", command=delete_selected_staff, font=("Arial", 12), width=15).grid(row=0, column=2, padx=10)

    window.mainloop()
