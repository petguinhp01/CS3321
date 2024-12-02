"""
File: staff_backend.py
Description: Backend logic for managing staff bookings, availability, and management.
Authors: Nhan Nguyen (Enhanced), Michael M.
Date: 12/01/2024
"""

from data_manager import append_row, read_all_rows, delete_row


def get_staff_bookings(staff_name):
    """
    Retrieves bookings specific to a staff member.

    Parameters:
        staff_name (str): The name of the staff.

    Returns:
        list: A list of tuples containing the staff member's assigned bookings.
    """
    try:
        bookings = read_all_rows("Bookings")
        return [booking for booking in bookings if booking[5] == staff_name]  # Staff name is in the 6th column
    except Exception as e:
        print(f"Error retrieving staff bookings: {e}")
        return []


def get_staff_availability(staff_name):
    """
    Retrieves availability slots for a specific staff member.

    Parameters:
        staff_name (str): Name of the staff.

    Returns:
        list: A list of tuples containing the staff's availability slots.
    """
    try:
        availability = read_all_rows("Staff Availability")
        return [slot for slot in availability if slot[0] == staff_name]  # Only match staff name
    except Exception as e:
        print(f"Error retrieving staff availability: {e}")
        return []


def set_staff_availability(staff_name, day, time_slot):
    """
    Adds a new availability slot for a staff member.

    Parameters:
        staff_name (str): Name of the staff.
        day (str): Day of availability (e.g., "2024-12-01").
        time_slot (str): Time slot of availability (e.g., "10:00-14:00").
    """
    try:
        # Avoid duplicate availability
        existing_availability = get_staff_availability(staff_name)
        if any(slot[1] == day and slot[2] == time_slot for slot in existing_availability):
            print(f"Duplicate availability detected: {day} {time_slot} for {staff_name}.")
            return
        append_row("Staff Availability", [staff_name, day, time_slot])
        print(f"Availability added for {staff_name}: {day} {time_slot}")
    except Exception as e:
        print(f"Error adding staff availability: {e}")


def delete_staff_availability(staff_name, day, time_slot):
    """
    Deletes an availability slot for a staff member.

    Parameters:
        staff_name (str): Name of the staff.
        day (str): Day of availability.
        time_slot (str): Time slot of availability.
    """
    try:
        availability = read_all_rows("Staff Availability")
        for row in availability:
            if row[0] == staff_name and row[1] == day and row[2] == time_slot:
                delete_row("Staff Availability", 1, row[1])  # Match day (row[1])
                print(f"Availability deleted for {staff_name}: {day} {time_slot}")
                break
    except Exception as e:
        print(f"Error deleting staff availability: {e}")


def add_staff(name, role, email):
    """
    Adds a new staff member to the 'Staff' sheet.

    Parameters:
        name (str): Name of the staff member.
        role (str): Role of the staff (e.g., "Manager", "Staff").
        email (str): Email of the staff.
    """
    try:
        # Check for duplicates
        existing_staff = read_all_rows("Staff")
        if any(staff[0] == name and staff[1] == role and staff[2] == email for staff in existing_staff):
            print(f"Duplicate staff entry detected: {name}, {role}, {email}.")
            return
        append_row("Staff", [name, role, email])
        print(f"Staff member added: {name}, {role}, {email}")
    except Exception as e:
        print(f"Error adding staff member: {e}")


def get_staff():
    """
    Retrieves all staff details from the 'Staff' sheet.

    Returns:
        list: A list of tuples containing staff details.
    """
    try:
        return read_all_rows("Staff")
    except Exception as e:
        print(f"Error retrieving staff details: {e}")
        return []
