import unittest
from classes import Guest, Booking, Room


class TestDisplayReservationHistory(unittest.TestCase):
    """Tests for displaying reservation history."""

    def setUp(self):
        """Setup for test methods."""
        self.guest = Guest("G001", "fatmah rashed", "fatmah rashed@example.com")
        self.room1 = Room("601", "Standard", ["TV"], 150.00)
        self.room2 = Room("602", "Deluxe", ["TV", "Mini-bar"], 250.00)
        self.booking1 = Booking("B001", self.guest, self.room1, "2025-04-10", "2025-04-13")
        self.booking2 = Booking("B002", self.guest, self.room2, "2025-05-01", "2025-05-04")

    def test_display_reservation_history(self):
        """Test that all past bookings are accurately displayed."""
        self.guest.add_reservation(self.booking1)
        self.guest.add_reservation(self.booking2)
        self.assertIn(self.booking1, self.guest.bookingList)
        self.assertIn(self.booking2, self.guest.bookingList)

        #Check with two different rooms.
        guest2 = Guest("G002", "alex", "alex@example.com")
        self.assertNotEqual(guest2.bookingList, self.guest.bookingList)

    def test_reservation_history_order(self):
        """Test that the reservation history is in the correct order."""
        self.guest.add_reservation(self.booking1)
        self.guest.add_reservation(self.booking2)
        self.assertEqual(self.guest.bookingList[0], self.booking1)
        self.assertEqual(self.guest.bookingList[1], self.booking2)

        guest2 = Guest("G002", "alex", "alex@example.com")
        room3 = Room("603", "Deluxe", ["TV", "Mini-bar"], 250.00)
        booking3 = Booking("B003", self.guest, room3, "2025-06-01", "2025-06-04")
        self.guest.add_reservation(booking3)
        self.assertEqual(self.guest.bookingList[2], booking3)

if __name__ == '__main__':
    unittest.main()
