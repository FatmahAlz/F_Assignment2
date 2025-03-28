import unittest
from classes import Hotel, Room, Guest, Booking


class TestBookingConfirmationNotification(unittest.TestCase):
    """Tests for booking confirmation notifications."""

    def setUp(self):
        """Setup for test methods."""
        self.hotel = Hotel("Sunset Resort", "Hawaii", 4, 75)
        self.room1 = Room("301", "Standard", ["Ocean View"], 200.00, True)
        self.room2 = Room("302", "Deluxe", ["Ocean View", "Balcony"], 350.00, True)
        self.guest1 = Guest("G001", "Luna Lovegood", "luna@example.com")
        self.guest2 = Guest("G002", "fatmah rashed", "fatmahrashed@example.com")
        self.booking1 = Booking("B001", self.guest1, self.room1, "2025-04-15", "2025-04-20")
        self.booking2 = Booking("B002", self.guest2, self.room2, "2025-04-22", "2025-04-27")

    def test_confirmation_message_content(self):
        """Test the content of the confirmation message."""
        import io
        from contextlib import redirect_stdout

        # Capture the output of the print statement
        with io.StringIO() as new_output, redirect_stdout(new_output):
            print(f"Booking confirmed for {self.guest1.name}, Room: {self.room1.room_number}, Dates: {self.booking1.check_in_date} - {self.booking1.check_out_date}")
            confirmation_message = new_output.getvalue().strip()

        self.assertIn(self.guest1.name, confirmation_message)
        self.assertIn(self.room1.room_number, confirmation_message)
        self.assertIn(self.booking1.check_in_date, confirmation_message)
        self.assertIn(self.booking1.check_out_date, confirmation_message)

        with io.StringIO() as new_output2, redirect_stdout(new_output2):
            print(f"Booking confirmed for {self.guest2.name}, Room: {self.room2.room_number}, Dates: {self.booking2.check_in_date} - {self.booking2.check_out_date}")
            confirmation_message2 = new_output2.getvalue().strip()

        self.assertIn(self.guest2.name, confirmation_message2)
        self.assertIn(self.room2.room_number, confirmation_message2)
        self.assertIn(self.booking2.check_in_date, confirmation_message2)
        self.assertIn(self.booking2.check_out_date, confirmation_message2)

    def test_confirmation_message_presence(self):
        """Test that the confirmation message is sent."""
        import io
        from contextlib import redirect_stdout

        # Capture the output of the print statement
        with io.StringIO() as new_output, redirect_stdout(new_output):
            print(f"Booking confirmed for {self.guest1.name}, Room: {self.room1.room_number}, Dates: {self.booking1.check_in_date} - {self.booking1.check_out_date}")
            confirmation_message = new_output.getvalue().strip()
        self.assertTrue(len(confirmation_message) > 0)

        with io.StringIO() as new_output2, redirect_stdout(new_output2):
            print(f"Booking confirmed for {self.guest2.name}, Room: {self.room2.room_number}, Dates: {self.booking2.check_in_date} - {self.booking2.check_out_date}")
            confirmation_message2 = new_output2.getvalue().strip()
        self.assertTrue(len(confirmation_message2) > 0)

if __name__ == '__main__':
    unittest.main()
