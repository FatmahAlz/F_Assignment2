import unittest
from classes import Payment, Booking, Guest, Room


class TestPaymentProcessing(unittest.TestCase):
    """Tests for processing different payment methods."""

    def setUp(self):
        """Setup for test methods."""
        self.guest = Guest("G001", "fatmah rashed", "fatmah rashed@example.com")
        self.room = Room("501", "Standard", ["TV"], 150.00)
        self.booking = Booking("B001", self.guest, self.room, "2025-04-05", "2025-04-08")  # 3 nights

    def test_credit_card_payment(self):
        """Test payment processing with a credit card."""
        payment = Payment("P001", self.booking, 450.00, "Credit Card")
        self.assertEqual(payment.payment_method, "Credit Card")
        self.assertTrue(payment.process_payment())  # Assuming process_payment always returns True for testing

        payment2 = Payment("P002", self.booking, 450.00, "Credit Card")
        self.assertEqual(payment2.payment_method, "Credit Card")
        self.assertTrue(payment2.process_payment())  # Assuming process_payment always returns True for testing

    def test_mobile_wallet_payment(self):
        """Test payment processing with a mobile wallet."""
        payment = Payment("P002", self.booking, 450.00, "Mobile Wallet")
        self.assertEqual(payment.payment_method, "Mobile Wallet")
        self.assertTrue(payment.process_payment())  # Assuming process_payment always returns True for testing

        payment2 = Payment("P003", self.booking, 450.00, "Mobile Wallet")
        self.assertEqual(payment2.payment_method, "Mobile Wallet")
        self.assertTrue(payment2.process_payment())  # Assuming process_payment always returns True for testing

if __name__ == '__main__':
    unittest.main()
