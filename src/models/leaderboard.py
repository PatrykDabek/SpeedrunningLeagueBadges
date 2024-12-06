
class Leaderboard:
    """Class to manage leaderboard bonuses and rankings."""

    BONUS_PERCENTAGES = {
        1: 50,   # Rank 1 gets a 50% bonus
        2: 25,   # Rank 2 gets a 25% bonus
        3: 10,   # Rank 3 gets a 10% bonus
    }
    """Leaderboard rank bonuses as percentages."""

    @classmethod
    def get_bonus_percentage(cls, leaderboard: dict, seconds_taken: float) -> int:
        """
        Get the player's bonus percentage based on their rank determined by the time taken.
        """
        for rank, top_time in sorted(leaderboard.items()):
            if seconds_taken <= top_time:
                return cls.BONUS_PERCENTAGES.get(rank, 1)  # Return the percentage for the rank
        return 1  # No bonus if not in the top ranks

    @classmethod
    def calculate_bonus(cls, leaderboard: dict, seconds_taken: float, credits: int) -> int:
        """
        Calculate the bonus credits earned based on leaderboard rank.
        """
        bonus_percentage = cls.get_bonus_percentage(leaderboard, seconds_taken)
        bonus_credits = int(credits * bonus_percentage / 100)  # Calculate percentage-based bonus
        return bonus_credits

