"""Test the functions in src.pfmp_richelbilderbeek.prime_solutions."""
import unittest

from src.pfmp_richelbilderbeek.prime_solutions import (
    are_primes,
    are_primes_cache_with_dict,
    are_primes_cache_with_set,
    are_primes_no_cache,
    are_primes_no_cache_recursion,
    is_prime,
    is_prime_recursive,
)


class TestPrimeSolutions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.prime_solutions."""

    def test_are_primes(self):
        """Test 'are_primes'."""
        self.assertIsNotNone(are_primes.__doc__)
        self.assertEqual(are_primes([]), [])
        self.assertEqual(are_primes([2]), [True])
        self.assertEqual(are_primes([3, 4]), [True, False])

    def test_are_primes_no_cache(self):
        """Test 'are_primes_no_cache'."""
        self.assertIsNotNone(are_primes_no_cache.__doc__)
        self.assertEqual(are_primes_no_cache([]), [])
        self.assertEqual(are_primes_no_cache([2]), [True])
        self.assertEqual(are_primes_no_cache([3, 4]), [True, False])

    def test_are_primes_no_cache_recursion(self):
        """Test 'are_primes_no_cache_recursion'."""
        self.assertIsNotNone(are_primes_no_cache_recursion.__doc__)
        self.assertEqual(are_primes_no_cache_recursion([]), [])
        self.assertEqual(are_primes_no_cache_recursion([2]), [True])
        self.assertEqual(are_primes_no_cache_recursion([3, 4]), [True, False])

    def test_are_primes_cache_with_dict(self):
        """Test 'are_primes_cache_with_dict'."""
        self.assertIsNotNone(are_primes_cache_with_dict.__doc__)
        self.assertEqual(are_primes_cache_with_dict([]), [])
        self.assertEqual(are_primes_cache_with_dict([2]), [True])
        self.assertEqual(are_primes_cache_with_dict([3, 4]), [True, False])
        self.assertEqual(are_primes_cache_with_dict([3, 3, 4]), [True, True, False])
        self.assertEqual(are_primes_cache_with_dict([4, 3]), [False, True])

    def test_are_primes_cache_with_set(self):
        """Test 'are_primes_cache_with_set'."""
        self.assertIsNotNone(are_primes_cache_with_set.__doc__)
        self.assertEqual(are_primes_cache_with_set([]), [])
        self.assertEqual(are_primes_cache_with_set([1]), [False])
        self.assertEqual(
            are_primes_cache_with_set(
                [1, 2, 3, 4, 1, 2, 3, 4],
            ),
            [False, True, True, False, False, True, True, False],
        )
        self.assertEqual(are_primes_cache_with_set([2]), [True])
        self.assertEqual(are_primes_cache_with_set([3, 4]), [True, False])
        self.assertEqual(are_primes_cache_with_set([4, 3]), [False, True])

    def test_is_prime(self):
        """Test 'is_prime'."""
        self.assertIsNotNone(is_prime.__doc__)
        self.assertRaises(TypeError, is_prime, "I am a string")
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(11))

    def test_is_prime_recursive(self):
        """Test 'is_prime_recursive'."""
        self.assertIsNotNone(is_prime_recursive.__doc__)
        self.assertRaises(TypeError, is_prime_recursive, "I am a string")
        self.assertTrue(is_prime_recursive(2))
        self.assertFalse(is_prime_recursive(1))
        self.assertTrue(is_prime_recursive(11))
        for i in range(0, 100):
            self.assertEqual(is_prime(i), is_prime_recursive(i))
