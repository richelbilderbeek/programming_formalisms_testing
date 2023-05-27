"""Tests all function in src.pfmp_richelbilderbeek.easy_questions."""
import unittest

from pfmp_richelbilderbeek.tdd_questions import (
    is_zero,
)


class TestEasySolutions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.easy_questions."""

    def test_is_zero(self):
        """Test 'is_zero'."""
        self.assertIsNotNone(is_zero.__doc__)
        self.assertTrue(is_zero(0))
        self.assertTrue(is_zero(0.0))
        self.assertFalse(is_zero(1))
        self.assertRaises(TypeError, is_zero, {1, 2})
        self.assertRaises(TypeError, is_zero, "I am a string")

