import unittest
from src.models.leaderboard import Leaderboard


class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        """Set up the initial state for each test."""
        self.credits = 100
        self.leaderboard = {
            1: 50,  # Rank 1 time
            2: 100,  # Rank 2 time
            3: 150,  # Rank 3 time
        }

    def test_get_bonus_percentage_rank_1(self):
        """Test that the correct bonus percentage is returned for rank 1."""
        bonus_percentage = Leaderboard.get_bonus_percentage(self.leaderboard, 45)
        self.assertEqual(bonus_percentage, 50)

    def test_get_bonus_percentage_rank_2(self):
        """Test that the correct bonus percentage is returned for rank 2."""
        bonus_percentage = Leaderboard.get_bonus_percentage(self.leaderboard, 75)
        self.assertEqual(bonus_percentage, 25)

    def test_get_bonus_percentage_rank_3(self):
        """Test that the correct bonus percentage is returned for rank 3."""
        bonus_percentage = Leaderboard.get_bonus_percentage(self.leaderboard, 125)
        self.assertEqual(bonus_percentage, 10)

    def test_get_bonus_percentage_no_rank(self):
        """Test that no bonus is returned if the time does not qualify for any rank."""
        bonus_percentage = Leaderboard.get_bonus_percentage(self.leaderboard, 200)
        self.assertEqual(bonus_percentage, 1)

    def test_calculate_bonus(self):
        """Test that the correct bonus credits are calculated."""
        bonus_credits = Leaderboard.calculate_bonus(self.leaderboard, 45, self.credits)
        self.assertEqual(bonus_credits, 50)


if __name__ == '__main__':
    unittest.main()
