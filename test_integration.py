import unittest
from staff_backend import set_staff_availability, get_staff_availability
from booking_backend import save_booking, get_customer_bookings
from service_backend import add_service, get_services
from data_manager import initialize_data_file


class TestIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialize_data_file()
        # Add test data
        add_service("Integration Test Service", "Integration Category", "1h", 150.0)
        set_staff_availability("test_staff", "2024-12-01", "10:00-12:00")
        save_booking("test_customer", "Integration Test Service", "2024-12-01", "10:00", "test_staff")

    def test_service_and_availability_integration(self):
        services = get_services()
        self.assertIn(("Integration Test Service", "Integration Category", "1h", 150.0), services)

        availability = get_staff_availability("test_staff")
        self.assertIn(("test_staff", "2024-12-01", "10:00-12:00"), availability)

    def test_booking_integration(self):
        bookings = get_customer_bookings("test_customer")
        self.assertTrue(any(booking[2] == "Integration Test Service" and booking[3] == "2024-12-01" for booking in bookings))


if __name__ == "__main__":
    unittest.main()
