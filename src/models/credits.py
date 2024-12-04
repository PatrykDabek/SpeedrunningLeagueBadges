

class Credits:
    """Credits class that contains the credits for a user."""
    def __init__(self):
        self.stored_credits: int = 0

    def add_credits(self, amount: int) -> None:
        """Add credits to the user's account."""
        self.stored_credits += amount

    def remove_credits(self, amount: int) -> None:
        """Remove credits from the user's account."""
        self.stored_credits -= amount

    def get_credits(self) -> int:
        """Get the user's current credit balance."""
        return self.stored_credits

