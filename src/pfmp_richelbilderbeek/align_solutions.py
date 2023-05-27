"""The functions from The Medium Project."""
from random import seed, shuffle
from time import time

from pandas import DataFrame

"""
These are all the solution functions for doing a DNA alignment.

This includes doing a speed measurement.
"""

def are_functions(fs):
    """Determine if `fs` is one or more functions.

    Returns `True` if `f` is one or more functions.
    """
    if (not is_list(fs)):
        return False
    if (len(fs) == 0):
        return False
    return all(is_function(fs[i]) for i in range(len(fs)))

def are_speed_measurements(x):
    """Determine if `x` is a table of speed measurements.

    The table of speed measurements must be a dictionary.

    Its three expected keys are:
     * `function_name`
     * `data_length`
     * `runtime_speed_secs`

    Each key element is a list.
    These three lists have an equal length.

    Returns `True` if `x` is a table of speed measurements.
    """
    if not isinstance(x, dict):
        return False
    num_cols = 3
    if (len(x) != num_cols):
        return False
    these_keys = list(x.keys())
    expected_keys = ["function_name", "data_length", "runtime_speed_secs"]
    if (these_keys != expected_keys):
        return False
    if (len(x["function_name"]) != len(x["data_length"])):
        return False
    if (len(x["function_name"]) != len(x["runtime_speed_secs"])):
        return False
    return True

class DnaSequence:

    """Class for a DNA sequence."""

    def __init__(self, s):
        """Create a DNA sequence.

        `s` must a string consisting of uppercase nucleotide one-letter abbreviations,
        for example 'ACGT'
        """
        if not isinstance(s, str):
            message = "'s' must be a string"
            raise TypeError(message)
        import re
        dna_pattern = re.compile("^[ACGT]*$")
        if not dna_pattern.match(s):
            message = "'s' must match pattern " + dna_pattern
            raise TypeError(message)
        self.s = s

def get_alignment_functions():
    """Get a list of alignment functions."""
    return []

def get_datas(rng_seed = 42, data_lengths = [9, 99, 999]):
    """Get a list of datasets (hence, the reduplicated/Gollumese plural).

    Each dataset is list of numbers,
    which can be used to illustrate sorting algorithms.
    """
    seed(rng_seed)
    datas = []
    for data_length in data_lengths:
        data = [x * x for x in range(0, data_length)]
        shuffle(data)
        datas.append(data)
    return datas

def get_speed_measurements(functions, datas):
    """Measure how long the runtime is of each function per each data.

    param functions functions: two or more functions
        that can work on an element of `datas`
    param list datas: one or more sets of data (hence, the
        reduplicated/Gollumese plural)

    Returns a dict with three columns:
      1. The function index (first function has index zero)
      2. The data index (first data has index zero)
      3. The time in seconds the function took to process the data
    """
    speed_measurements = {
        "function_name": [],
        "data_length": [],
        "runtime_speed_secs": [],
    }
    for f in functions:
        for data in datas:
            speed_measurements["data_length"].append(len(data))
            speed_measurements["function_name"].append(f.__name__)
            start = time()
            f(data)
            end = time()
            t = end - start
            speed_measurements["runtime_speed_secs"].append(t)

    return speed_measurements

def get_test_datas(rng_seed = 42):
    """Get a list of datasets (hence, the reduplicated/Gollumese plural).

    Each dataset is list of numbers,
    which can be used to illustrate sorting algorithms.
    """
    return get_datas(rng_seed = rng_seed, data_lengths = [2, 3, 4])

def get_test_speed_measurements():
    """Return a collection of speed measurements, to be used in tests."""
    return {
        "function_name": ["silly_sort", "stupid_sort"],
        "data_length": [0, 1],
        "runtime_speed_secs": [0.1, 0.2],
    }

def is_dict(x):
    """Determine if `x` is a dict.

    Returns `True` if `x` is a dict.
    """
    return type(x) == dict

def is_function(f):
    """Determine if `f` is a function.

    Returns `True` if `f` is a function.
    """
    return callable(f)

def is_list(x):
    """Determine if `x` is a list.

    Returns `True` if `x` is a list.
    """
    return type(x) == list

def is_sorted(data):
    """Determine if `data` is sorted.

    Returns `True` if the data is sorted.
    """
    return data == sorted(data)

def save_dict(x, csv_filename):
    """Save the dictionary `x` to a file named `csv_filename`."""
    # should fail in debug mode only
    assert is_dict(x)
    data_frame = DataFrame.from_dict(x)
    data_frame.to_csv(csv_filename, index = False)
    pass

def save_speed_measurements(speed_measurements, csv_filename):
    """Save the `speed_measurements` to a file named `csv_filename`."""
    # should fail in debug mode only
    assert are_speed_measurements(speed_measurements)
    save_dict(
        x = speed_measurements,
        csv_filename = csv_filename,
    )
