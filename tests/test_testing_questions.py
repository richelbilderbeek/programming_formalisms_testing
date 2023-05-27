"""Test the functions in src.pfmp_richelbilderbeek.medium_questions."""
import unittest

from pfmp_richelbilderbeek.testing_questions import (
    is_prime,
)


class TestMediumQuestions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.medium_questions."""

    def test_is_prime(self):
        """Test 'is_prime'."""
        self.assertIsNotNone(is_prime.__doc__)
        self.assertRaises(TypeError, is_prime, "I am a string")
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(11))
