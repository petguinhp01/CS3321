import unittest
from staff_backend import get_staff_bookings, get_staff_availability, set_staff_availability, delete_staff_availability, add_staff
from data_manager import initialize_data_file, append_row

class TestStaffBackend(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialize_data_file()
        append_row("Staff", ["test_staff", "Tester", "test_staff@example.com"])
        append_row("Staff Availability", ["test_staff", "2024-12-01", "09:00-12:00"])

    def test_get_staff_bookings(self):
        result = get_staff_bookings("test_staff")
        self.assertIsInstance(result, list)

    def test_get_staff_availability(self):
        result = get_staff_availability("test_staff")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "2024-12-01")

    def test_set_staff_availability(self):
        set_staff_availability("test_staff", "2024-12-02", "12:00-15:00")
        result = get_staff_availability("test_staff")
        self.assertIn(("test_staff", "2024-12-02", "12:00-15:00"), result)

    def test_delete_staff_availability(self):
        delete_staff_availability("test_staff", "2024-12-01", "09:00-12:00")
        result = get_staff_availability("test_staff")
        self.assertNotIn(("test_staff", "2024-12-01", "09:00-12:00"), result)

    def test_add_staff(self):
        add_staff("new_staff", "Tester", "new_staff@example.com")
        # Validate if the new staff was added
        from data_manager import read_all_rows
        staff_list = read_all_rows("Staff")
        self.assertIn(("new_staff", "Tester", "new_staff@example.com"), staff_list)

if __name__ == "__main__":
    unittest.main()
