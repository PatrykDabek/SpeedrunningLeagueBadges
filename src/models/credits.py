from src.exceptions.insufficient_credits import InsufficientCreditsError


class Credits:
    """Credits class that contains the credits for a user."""
    def __init__(self):
        self._stored_credits: int = 0

    def add_credits(self, amount: int) -> None:
        """Add credits to the user's account."""
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self._stored_credits += amount

    def remove_credits(self, amount: int) -> None:
        """Remove credits from the user's account."""
        if amount < 0:
            raise ValueError("Amount to spend must be non-negative.")
        if amount > self._stored_credits:
            raise InsufficientCreditsError("Not enough credits to spend.")
        self._stored_credits -= amount

    def update_credits(self, amount: int) -> None:
        """Update credits by adding (positive) or spending (negative)."""
        if amount >= 0:
            self.add_credits(amount)
        else:
            self.remove_credits(-amount)

    def get_credits(self) -> int:
        """Get the user's current credit balance."""
        return self._stored_credits

