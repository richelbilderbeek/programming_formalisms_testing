"""Tests all function in src.pfmp_richelbilderbeek.easy_solutions."""
import unittest

from pfmp_richelbilderbeek.tdd_solutions import (
    are_numbers,
    are_strings,
    check_are_numbers,
    check_different,
    check_equal,
    check_is_number,
    check_is_probability,
    check_is_string,
    divide_safely,
    is_dividable_by_three,
    is_even,
    is_number,
    is_odd,
    is_probability,
    is_string,
    is_zero,
)


class TestEasySolutions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.easy_solutions."""

    def test_are_numbers(self):
        """Test 'are_numbers'."""
        self.assertIsNotNone(are_numbers.__doc__)
        self.assertFalse(are_numbers(":-/"))
        self.assertTrue(are_numbers([1, 2]))
        self.assertTrue(are_numbers([1.1]))
        self.assertFalse(are_numbers([]))
        self.assertFalse(are_numbers(["1.2"]))

    def test_are_strings(self):
        """Test 'are_strings'."""
        self.assertIsNotNone(are_strings.__doc__)
        self.assertTrue(are_strings(["A"]))
        self.assertTrue(are_strings(["A", "B"]))
        self.assertFalse(are_strings("A"))
        self.assertFalse(are_strings(3.14))
        self.assertFalse(are_strings(["A", 3.14]))
        self.assertFalse(are_strings([]))

    def test_check_are_numbers(self):
        """Test 'are_numbers'."""
        self.assertIsNotNone(check_are_numbers.__doc__)
        check_are_numbers([3.14])
        check_are_numbers([3.14, 42])
        self.assertRaises(RuntimeError, check_are_numbers, "A")

    def test_check_different(self):
        """Test 'check_different'."""
        self.assertIsNotNone(check_different.__doc__)
        check_different(1.2, 1.3)
        check_different(1.2, "A")
        self.assertRaises(RuntimeError, check_different, 1.1, 1.1)
        self.assertRaises(RuntimeError, check_different, "1.1", "1.1")

    def test_check_equal(self):
        """Test 'check_equal'."""
        self.assertIsNotNone(check_equal.__doc__)
        check_equal(1.2, 1.2)
        check_equal("A", "A")
        self.assertRaises(RuntimeError, check_equal, 1.1, 2.2)
        self.assertRaises(RuntimeError, check_equal, 1.1, "1.1")

    def test_check_is_number(self):
        """Test 'check_is_number'."""
        self.assertIsNotNone(check_is_number.__doc__)
        check_is_number(1.2)
        self.assertRaises(RuntimeError, check_is_number, [1.1, 2.2])
        self.assertRaises(RuntimeError, check_is_number, "0.1")

    def test_check_is_probability(self):
        """Test 'check_is_probability'."""
        self.assertIsNotNone(check_is_probability.__doc__)
        check_is_probability(0.2)
        self.assertRaises(RuntimeError, check_is_probability, [0.1, 0.2])
        self.assertRaises(RuntimeError, check_is_probability, "0.1")
        self.assertRaises(RuntimeError, check_is_probability, 123.456)

    def test_check_is_string(self):
        """Test 'check_is_string'."""
        self.assertIsNotNone(check_is_string.__doc__)
        check_is_string("A")
        self.assertRaises(RuntimeError, check_is_string, ["A", "B"])
        self.assertRaises(RuntimeError, check_is_string, 3.14)

    def test_divide_safely(self):
        """Test 'divide_safely'."""
        self.assertIsNotNone(divide_safely.__doc__)
        numerator = 1.2
        denominator = 0.3
        zero = 0.0
        self.assertTrue(divide_safely(numerator , denominator) > zero)
        self.assertRaises(RuntimeError, divide_safely, 1.1, 0.0)

    def test_is_dividable_by_three(self):
        """Test 'is_dividable_by_three'."""
        self.assertIsNotNone(is_dividable_by_three)
        self.assertFalse(is_dividable_by_three(2))
        self.assertRaises(TypeError, is_dividable_by_three, 3.14)

    def test_is_even(self):
        """Test 'is_even'."""
        self.assertIsNotNone(is_even.__doc__)
        self.assertFalse(is_even(1))
        self.assertRaises(TypeError, is_even, 3.14)

    def test_is_number(self):
        """Test 'is_number'."""
        self.assertIsNotNone(is_number.__doc__)
        self.assertTrue(is_number(42))
        self.assertTrue(is_number(3.14))
        self.assertFalse(is_number("a string"))

    def test_is_odd(self):
        """Test 'is_odd'."""
        self.assertIsNotNone(is_odd.__doc__)
        self.assertFalse(is_odd(2))
        self.assertRaises(TypeError, is_odd, 3.14)

    def test_is_probability(self):
        """Test 'is_string'."""
        self.assertIsNotNone(is_probability.__doc__)
        self.assertTrue(is_probability(0.1))
        self.assertFalse(is_probability(1.2))
        self.assertFalse(is_probability(-1.2))
        self.assertRaises(TypeError, is_probability, "I am a string")

    def test_is_string(self):
        """Test 'is_string'."""
        self.assertIsNotNone(is_string.__doc__)
        self.assertTrue(is_string("Hello"))
        self.assertFalse(is_string({"Hello", "too much strings"}))


    def test_is_zero(self):
        """Test 'is_zero'."""
        self.assertIsNotNone(is_zero.__doc__)
        self.assertTrue(is_zero(0))
        self.assertTrue(is_zero(0.0))
        self.assertFalse(is_zero(1))
        self.assertRaises(TypeError, is_zero, {1, 2})
        self.assertRaises(TypeError, is_zero, "I am a string")

