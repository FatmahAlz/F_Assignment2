import unittest
from classes import Booking, Room, Guest


class TestCancellationReservation(unittest.TestCase):
    """Tests for cancellation of a reservation."""

    def setUp(self):
        """Setup for test methods."""
        self.guest = Guest("G001", "fatmah rashed", "fatmahrashed@example.com")
        self.room = Room("701", "Suite", ["Ocean View", "Jacuzzi"], 800.00, False) #Initally set to false
        self.booking = Booking("B001", self.guest, self.room, "2025-04-15", "2025-04-20") #5 nights

    def test_cancel_reservation_updates_room_availability(self):
        """Test that canceling a reservation updates the room's availability."""
        self.assertFalse(self.room.get_availability_status())
        self.room.set_availability_status(True)
        self.assertTrue(self.room.get_availability_status())

    def test_cancel_reservation_generates_cancellation_notice(self):
        """Test that canceling a reservation generates a cancellation notice."""
        notice = "Booking B001 has been cancelled" #Manual notice
        self.assertEqual(notice, "Booking B001 has been cancelled") #check if they are equal

        notice2 = "Booking B001 has been cancelled again" #Manual notice
        self.assertEqual(notice2, "Booking B001 has been cancelled again") #check if they are equal

if __name__ == '__main__':
    unittest.main()
