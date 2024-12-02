import unittest
from login_backend import authenticate_user
from data_manager import append_row, initialize_data_file


class TestLoginBackend(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialize_data_file()
        append_row("User", ["test_admin", "password123", "Admin"])
        append_row("User", ["test_staff", "password123", "Staff"])
        append_row("User", ["test_customer", "password123", "Customer"])

    def test_authenticate_admin(self):
        role = authenticate_user("test_admin", "password123")
        self.assertEqual(role, "Admin")

    def test_authenticate_staff(self):
        role = authenticate_user("test_staff", "password123")
        self.assertEqual(role, "Staff")

    def test_authenticate_customer(self):
        role = authenticate_user("test_customer", "password123")
        self.assertEqual(role, "Customer")

    def test_invalid_user(self):
        role = authenticate_user("invalid_user", "password123")
        self.assertIsNone(role)

    def test_invalid_password(self):
        role = authenticate_user("test_admin", "wrong_password")
        self.assertIsNone(role)


if __name__ == "__main__":
    unittest.main()
