import unittest
from booking_backend import save_booking, get_customer_bookings, get_all_bookings

class TestBookingBackend(unittest.TestCase):

    def test_save_booking(self):
        save_booking("test_user", "Test Service", "2024-12-01", "10:00", "test_staff")
        result = get_customer_bookings("test_user")
        self.assertTrue(any(booking[1] == "test_user" for booking in result))

    def test_get_customer_bookings(self):
        result = get_customer_bookings("test_user")
        self.assertIsInstance(result, list)

    def test_get_all_bookings(self):
        result = get_all_bookings()
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()
