import unittest
from classes import Guest

class TestGuestCreation(unittest.TestCase):
    def test_guest_creation_with_full_details(self):
        """Test creating guest with all details"""
        guest = Guest(1001, "Fatmah rashed", "fatmah@example.com", "Gold")
        self.assertEqual(guest.name, "Fatmah rashed")
        self.assertEqual(guest.contact_info, "fatmah@example.com")
        self.assertEqual(guest.loyalty_status, "Gold")

    def test_guest_creation_with_minimal_info(self):
        """Test creating guest with minimal information"""
        guest = Guest(1002, "Bob Smith", "555-1234", "Basic")
        self.assertEqual(guest.guest_id, 1002)
        self.assertEqual(guest.contact_info, "555-1234")

if __name__ == '__main__':
    unittest.main()