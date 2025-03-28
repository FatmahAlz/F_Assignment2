import unittest
from classes import Hotel, Room, Guest, Booking


class TestRoomReservation(unittest.TestCase):
    """Tests for making room reservations."""

    def setUp(self):
        """Setup for test methods."""
        self.hotel = Hotel("Ocean View Resort", "Miami", 4, 50)
        self.room1 = Room("201", "Deluxe", ["Ocean View", "Balcony"], 300.00, True)
        self.room2 = Room("202", "Suite", ["Ocean View", "Jacuzzi"], 500.00, True)
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room2)
        self.guest1 = Guest("G001", "Harry Potter", "harry@example.com")
        self.guest2 = Guest("G002", "fatmah rashed", "fatmahrashed@example.com")

    def test_make_valid_reservation(self):
        """Test making a valid room reservation."""
        booking1 = Booking("B001", self.guest1, self.room1, "2025-04-10", "2025-04-15")
        self.assertEqual(booking1.guest, self.guest1)
        self.assertEqual(booking1.room, self.room1)
        self.assertEqual(booking1.check_in_date, "2025-04-10")
        self.assertEqual(booking1.check_out_date, "2025-04-15")

        booking2 = Booking("B002", self.guest2, self.room2, "2025-04-20", "2025-04-25")
        self.assertEqual(booking2.guest, self.guest2)
        self.assertEqual(booking2.room, self.room2)
        self.assertEqual(booking2.check_in_date, "2025-04-20")
        self.assertEqual(booking2.check_out_date, "2025-04-25")

    def test_room_unavailable_after_reservation(self):
        """Test that the room becomes unavailable after a reservation."""
        booking = Booking("B003", self.guest1, self.room1, "2025-05-01", "2025-05-05")
        self.room1.set_availability_status(False) #Sets to false after booking
        self.assertFalse(self.room1.get_availability_status())

        booking2 = Booking("B004", self.guest2, self.room2, "2025-05-06", "2025-05-10")
        self.room2.set_availability_status(False) #Sets to false after booking
        self.assertFalse(self.room2.get_availability_status())

if __name__ == '__main__':
    unittest.main()
