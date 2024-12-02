"""
File: booking_backend.py
Description: Backend logic for managing bookings.
Authors: Samira Bechi
Date: 12/01/2024
"""

from data_manager import append_row, read_all_rows, update_row


def save_booking(customer_name, service, date, time, staff_name=""):
    """
    Saves a new booking to the 'Bookings' sheet.

    Parameters:
        customer_name (str): Name of the customer making the booking.
        service (str): Service being booked.
        date (str): Date of the booking (YYYY-MM-DD).
        time (str): Time of the booking (HH:MM).
        staff_name (str): Name of the staff (optional).
    """
    try:
        booking_id = f"BK-{len(read_all_rows('Bookings')) + 1}"  # Generate a unique booking ID
        status = "Pending"
        append_row("Bookings", [booking_id, customer_name, service, date, time, staff_name, status])
    except Exception as e:
        print(f"Error saving booking: {e}")


def get_customer_bookings(customer_name):
    """
    Retrieves bookings for a specific customer.

    Parameters:
        customer_name (str): The name of the customer.

    Returns:
        list: A list of tuples containing the customer's bookings.
    """
    try:
        bookings = read_all_rows("Bookings")
        return [booking for booking in bookings if booking[1] == customer_name]
    except Exception as e:
        print(f"Error retrieving bookings for customer {customer_name}: {e}")
        return []


def get_staff_bookings(staff_name):
    """
    Retrieves bookings for a specific staff member.

    Parameters:
        staff_name (str): The name of the staff.

    Returns:
        list: A list of tuples containing the staff's assigned bookings.
    """
    try:
        bookings = read_all_rows("Bookings")
        return [booking for booking in bookings if booking[5] == staff_name]
    except Exception as e:
        print(f"Error retrieving bookings for staff {staff_name}: {e}")
        return []


def get_all_bookings():
    """
    Retrieves all bookings from the system.

    Returns:
        list: A list of all bookings.
    """
    try:
        return read_all_rows("Bookings")
    except Exception as e:
        print(f"Error retrieving all bookings: {e}")
        return []


def cancel_booking(booking_id):
    """
    Cancels a booking by updating its status to 'Cancelled'.

    Parameters:
        booking_id (str): The ID of the booking to cancel.
    """
    try:
        bookings = get_all_bookings()
        for booking in bookings:
            if booking[0] == booking_id:  # Match Booking ID
                update_row("Bookings", 0, booking_id, [*booking[:6], "Cancelled"])  # Keep all columns except status
                break
    except Exception as e:
        print(f"Error cancelling booking with ID {booking_id}: {e}")


def update_booking(booking_id, new_data):
    """
    Updates a booking with new data.

    Parameters:
        booking_id (str): The ID of the booking to update.
        new_data (list): The updated booking data (excluding ID).
    """
    try:
        update_row("Bookings", 0, booking_id, [booking_id, *new_data])
    except Exception as e:
        print(f"Error updating booking with ID {booking_id}: {e}")
