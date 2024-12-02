"""
File: service_backend.py
Description: Backend logic for managing services.
Authors: Abel Thomas
Date: 12/01/2024
"""

from data_manager import append_row, read_all_rows, delete_row, update_row


def get_services():
    """
    Retrieves all services from the 'Services' sheet.

    Returns:
        list: A list of tuples containing service details.
    """
    try:
        return read_all_rows("Services")
    except Exception as e:
        print(f"Error retrieving services: {e}")
        return []


def add_service(name, category, duration, price):
    """
    Adds a new service to the 'Services' sheet.

    Parameters:
        name (str): Name of the service.
        category (str): Category of the service.
        duration (str): Duration of the service (e.g., "1h").
        price (float): Price of the service.
    """
    try:
        append_row("Services", [name, category, duration, price])
    except Exception as e:
        print(f"Error adding service: {e}")


def edit_service(old_name, name, category, duration, price):
    """
    Edits an existing service in the 'Services' sheet.

    Parameters:
        old_name (str): Existing name of the service to edit.
        name (str): New name of the service.
        category (str): New category of the service.
        duration (str): New duration of the service.
        price (float): New price of the service.
    """
    try:
        update_row("Services", 0, old_name, [name, category, duration, price])
    except Exception as e:
        print(f"Error editing service '{old_name}': {e}")


def delete_service(name):
    """
    Deletes a service from the 'Services' sheet.

    Parameters:
        name (str): Name of the service to delete.
    """
    try:
        delete_row("Services", 0, name)
    except Exception as e:
        print(f"Error deleting service '{name}': {e}")
