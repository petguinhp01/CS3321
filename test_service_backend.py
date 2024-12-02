import unittest
from service_backend import add_service, edit_service, delete_service, get_services
from data_manager import initialize_data_file


class TestServiceBackend(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialize_data_file()
        add_service("Test Service", "Test Category", "1h", 100.0)

    def test_get_services(self):
        services = get_services()
        self.assertIn(("Test Service", "Test Category", "1h", 100.0), services)

    def test_add_service(self):
        add_service("New Service", "New Category", "2h", 200.0)
        services = get_services()
        self.assertIn(("New Service", "New Category", "2h", 200.0), services)

    def test_edit_service(self):
        edit_service("Test Service", "Updated Service", "Updated Category", "3h", 300.0)
        services = get_services()
        self.assertIn(("Updated Service", "Updated Category", "3h", 300.0), services)
        self.assertNotIn(("Test Service", "Test Category", "1h", 100.0), services)

    def test_delete_service(self):
        delete_service("Updated Service")
        services = get_services()
        self.assertNotIn(("Updated Service", "Updated Category", "3h", 300.0), services)


if __name__ == "__main__":
    unittest.main()
