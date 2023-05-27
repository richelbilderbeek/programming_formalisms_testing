"""Test the functions in src.pfmp_richelbilderbeek.medium_solutions."""
import unittest
from random import seed

from pfmp_richelbilderbeek.testing_solutions import (
    flip_coin,
    get_digits,
    roll_dice,
)


class TestMediumSolutions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.medium_solutions."""

    def test_flip_coin(self):
        """Test 'flip_coin'."""
        self.assertIsNotNone(flip_coin.__doc__)

        # Repeats with same seed
        seed(42)
        coin_toss_1 = flip_coin()
        seed(42)
        coin_toss_2 = flip_coin()
        self.assertEqual(coin_toss_1, coin_toss_2)

        # Can be both True and False
        seed(2)
        self.assertFalse(flip_coin())
        seed(5)
        self.assertTrue(flip_coin())

        # Should be True in around 50% of all cases
        flips = [flip_coin() for i in range(1000)]
        n_heads = sum(flips)
        lowest_expectation = 400
        heighest_expectation = 600
        self.assertTrue(n_heads > lowest_expectation)
        self.assertTrue(n_heads < heighest_expectation)

    def test_get_digits(self):
        """Test 'get_digits'."""
        self.assertIsNotNone(get_digits.__doc__)
        self.assertRaises(TypeError, get_digits, "evil string")
        self.assertEqual(get_digits(1), [1])
        self.assertEqual(get_digits(0), [0])
        self.assertEqual(get_digits(12), [1, 2])
        self.assertEqual(get_digits(-12), [1, 2])

    def test_roll_dice(self):
        """Test 'roll_dice'."""
        # Repeats with same seed
        seed(42)
        dice_roll_1 = roll_dice()
        seed(42)
        dice_roll_2 = roll_dice()
        self.assertEqual(dice_roll_1, dice_roll_2)

        # Make a dict of 60
        dice_rolls = {}
        dice_rolls[1] = 0
        dice_rolls[2] = 0
        dice_rolls[3] = 0
        dice_rolls[4] = 0
        dice_rolls[5] = 0
        dice_rolls[6] = 0
        seed(42)
        for _ in range(60):
          dice_roll = roll_dice()
          dice_rolls[dice_roll] = dice_rolls[dice_roll] + 1
        lowest_expectation = 5
        heighest_expectation = 20
        for i in range(1, 6):
          self.assertTrue(dice_rolls[i] > lowest_expectation)
          self.assertTrue(dice_rolls[i] < heighest_expectation)
