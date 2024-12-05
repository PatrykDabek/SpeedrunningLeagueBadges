import unittest

from src.models.credits import Credits, InsufficientCreditsError


class TestCredits(unittest.TestCase):
    def setUp(self):
        """Set up the initial state for each test."""
        self.credit_account = Credits()  # Create a new Credits instance for each test

    def test_initial_credits(self):
        """Test that the initial credit balance is zero."""
        self.assertEqual(self.credit_account.get_credits(), 0)

    def test_add_credits(self):
        """Test that credits are correctly added to the user's account."""
        self.credit_account.add_credits(50)
        self.assertEqual(self.credit_account.get_credits(), 50)

    def test_add_credits_negative(self):
        """Test that adding negative credits raises an exception."""
        with self.assertRaises(ValueError):
            self.credit_account.add_credits(-10)

    def test_remove_credits(self):
        """Test that credits are correctly removed from the user's account."""
        self.credit_account.add_credits(100)  # First, add some credits
        self.credit_account.remove_credits(30)  # Then remove some
        self.assertEqual(self.credit_account.get_credits(), 70)

    def test_remove_credits_beyond_balance(self):
        """Test that removing credits beyond the balance raises an exception."""
        self.credit_account.add_credits(50)
        with self.assertRaises(InsufficientCreditsError):
            self.credit_account.remove_credits(100)

    def test_remove_credits_negative(self):
        """Test that removing a negative amount raises an exception."""
        with self.assertRaises(ValueError):
            self.credit_account.remove_credits(-10)

    def test_get_credits_after_multiple_operations(self):
        """Test that multiple add/remove operations work correctly."""
        self.credit_account.add_credits(200)
        self.credit_account.remove_credits(50)
        self.credit_account.add_credits(100)
        self.credit_account.remove_credits(150)
        self.assertEqual(self.credit_account.get_credits(), 100)

    def test_update_credits_positive(self):
        """Test that update_credits adds credits for positive input."""
        self.credit_account.update_credits(75)
        self.assertEqual(self.credit_account.get_credits(), 75)

    def test_update_credits_negative(self):
        """Test that update_credits removes credits for negative input."""
        self.credit_account.add_credits(100)
        self.credit_account.update_credits(-25)
        self.assertEqual(self.credit_account.get_credits(), 75)

    def test_update_credits_beyond_balance(self):
        """Test that update_credits prevents overspending."""
        self.credit_account.add_credits(50)
        with self.assertRaises(InsufficientCreditsError):
            self.credit_account.update_credits(-100)


if __name__ == '__main__':
    unittest.main()
