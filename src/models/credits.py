import logging
from src.exceptions.insufficient_credits import InsufficientCreditsError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Credits:
    """Credits class that contains the credits for a user."""

    BASE_MULTIPLIER = 500
    """The base multiplier for calculating credits based on time taken."""

    BASE_CREDITS = 10
    """The base credits earned by speedrunning."""

    def __init__(self):
        self._stored_credits: int = 0

    def add_credits(self, amount: int) -> None:
        """Add credits to the user's account."""
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self._stored_credits += amount
        logging.info(f"Added {amount} credits. New balance: {self._stored_credits}")

    def remove_credits(self, amount: int) -> None:
        """Remove credits from the user's account."""
        if amount < 0:
            raise ValueError("Amount to spend must be non-negative.")
        if amount > self._stored_credits:
            raise InsufficientCreditsError("Not enough credits to spend.")
        self._stored_credits -= amount
        logging.info(f"Removed {amount} credits. New balance: {self._stored_credits}")

    def update_credits(self, amount: int) -> None:
        """Update credits by adding (positive) or spending (negative)."""
        if amount >= 0:
            self.add_credits(amount)
        else:
            self.remove_credits(-amount)

    def get_credits(self) -> int:
        """Get the user's current credit balance."""
        return self._stored_credits

    def award_credits(self, seconds_taken: float, base_credits: int = 10) -> int:
        """
        Calculates and adds the credits earned based on time taken.
        The faster the completion, the more credits earned.
        """
        if seconds_taken <= 0:
            raise ValueError("Time taken must be greater than zero.")

        multiplier = max(1, int(self.BASE_MULTIPLIER / seconds_taken))
        earned_credits = int(base_credits * multiplier)
        self.add_credits(earned_credits)
        logging.info(f"Awarded {earned_credits} credits for {seconds_taken} seconds taken. New balance: {self._stored_credits}")
        return earned_credits
