"""Test the functions in src.pftesting_richelbilderbeek.testing_questions."""
import unittest

from pftesting_richelbilderbeek.testing_questions import (
    is_prime,
)


class TestTestingQuestions(unittest.TestCase):

    """Class to test all functions."""

    def test_is_prime(self):
        """Test 'is_prime'."""
        self.assertIsNotNone(is_prime.__doc__)
        self.assertRaises(TypeError, is_prime, "I am a string")
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(11))
