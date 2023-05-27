"""Test the functions in src.pfmp_richelbilderbeek.align_solutions."""
import os.path
import unittest

from src.pfmp_richelbilderbeek.align_solutions import (
    DnaSequence,
    are_functions,
    are_speed_measurements,
    get_alignment_functions,
    get_datas,
    get_speed_measurements,
    get_test_datas,
    get_test_speed_measurements,
    is_dict,
    is_function,
    is_list,
    is_sorted,
    save_dict,
    save_speed_measurements,
)


class TestAlignSolutions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.align_solutions."""

    def test_are_functions(self):
        """Test 'are_functions'."""
        self.assertIsNotNone(are_functions.__doc__)
        self.assertFalse(are_functions([]))
        self.assertFalse(are_functions(3.14))
        self.assertFalse(are_functions("Hello"))

    def test_are_speed_measurements(self):
        """Test 'are_speed_measurements'."""
        self.assertIsNotNone(are_speed_measurements.__doc__)
        self.assertTrue(are_speed_measurements(get_test_speed_measurements()))
        self.assertFalse(are_speed_measurements(0.1))
        self.assertFalse(are_speed_measurements({"x": 1.0}))
        self.assertFalse(are_speed_measurements({"x": 1.0, "y": 2.0, "z": 3.0}))
        nasty_data_1 = {
            "function_name": [0, 1, 234567], # Oops
            "data_length": [0, 0],
            "runtime_speed_secs": [0.1, 0.2],
        }
        self.assertFalse(are_speed_measurements(nasty_data_1))
        nasty_data_2 = {
            "function_name": [0, 1],
            "data_length": [0, 0, 123456789], # Oops
            "runtime_speed_secs": [0.1, 0.2],
        }
        self.assertFalse(are_speed_measurements(nasty_data_2))
        nasty_data_3 = {
            "function_name": [0, 1],
            "data_length": [0, 0],
            "runtime_speed_secs": [0.1, 0.2, 0.3456789], # Oops
        }
        self.assertFalse(are_speed_measurements(nasty_data_3))

    def test_dna_sequence_class(self):
        """Test the 'DnaSequence' class."""
        self.assertIsNotNone(DnaSequence.__doc__)
        self.assertRaises(TypeError, DnaSequence, 12345)
        self.assertRaises(TypeError, DnaSequence, ["A", "C"])
        self.assertRaises(TypeError, DnaSequence, "nonsense")
        self.assertEqual(DnaSequence("ACGT").s, "ACGT")

    def test_get_datas(self):
        """Test 'get_datas'."""
        self.assertIsNotNone(get_datas.__doc__)
        self.assertTrue(is_list(get_datas()))
        self.assertEqual(get_datas(42), get_datas(42))
        self.assertNotEqual(get_datas(42), get_datas(43))

    def test_get_speed_measurements(self):
        """Test 'get_speed_measurements'."""
        self.assertIsNotNone(get_speed_measurements.__doc__)
        speed_measurements = get_speed_measurements(
            datas = get_test_datas(),
            functions = get_alignment_functions(),
        )
        self.assertTrue(are_speed_measurements(speed_measurements))

    def test_get_test_datas(self):
        """Test 'get_test_datas'."""
        self.assertIsNotNone(get_test_datas.__doc__)
        self.assertTrue(is_list(get_test_datas()))
        self.assertEqual(get_test_datas(42), get_test_datas(42))
        self.assertNotEqual(get_test_datas(42), get_test_datas(43))

    def test_get_test_speed_measurements(self):
        """Test 'get_test_speed_measurements'."""
        self.assertIsNotNone(get_test_speed_measurements.__doc__)
        self.assertTrue(isinstance(get_test_speed_measurements(), dict))

    def test_is_dict(self):
        """Test 'is_dict'."""
        self.assertIsNotNone(is_dict.__doc__)
        self.assertTrue(is_dict({"X": 3.14}))
        self.assertFalse(is_dict(3.14))
        self.assertFalse(is_dict([3.14]))

    def test_is_function(self):
        """Test 'is_function'."""
        self.assertIsNotNone(is_function.__doc__)
        self.assertTrue(is_function(is_function))
        self.assertFalse(is_function(42))

    def test_is_list(self):
        """Test 'is_list'."""
        self.assertIsNotNone(is_list.__doc__)
        self.assertFalse(is_list(42))


    def test_is_sorted(self):
        """Test 'is_sorted'."""
        self.assertIsNotNone(is_sorted.__doc__)
        self.assertTrue(is_sorted([1, 2]))
        self.assertTrue(is_sorted([1]))
        self.assertFalse(is_sorted([2, 1]))
        self.assertFalse(is_sorted(get_datas()[0]))

    def test_save_dict(self):
        """Test 'save_dict'."""
        self.assertIsNotNone(save_dict.__doc__)
        csv_filename = "temp_save_dict.csv"
        if (os.path.isfile(csv_filename)):
            os.remove(csv_filename)
        self.assertFalse(os.path.isfile(csv_filename))

        save_dict(
            x = { "X": [1, 2, 3], "Y": [4, 5, 6]},
            csv_filename = csv_filename,
        )
        self.assertTrue(os.path.isfile(csv_filename))
        os.remove(csv_filename)

    def test_save_speed_measurements(self):
        """Test 'save_speed_measurements'."""
        self.assertIsNotNone(save_speed_measurements.__doc__)
        csv_filename = "temp_save_speed_measurements.csv"
        self.assertFalse(os.path.isfile(csv_filename))
        save_speed_measurements(
            speed_measurements = get_test_speed_measurements(),
            csv_filename = csv_filename,
        )
        self.assertTrue(os.path.isfile(csv_filename))
        os.remove(csv_filename)
