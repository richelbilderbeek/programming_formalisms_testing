"""Easy general-purpose functions.

'Easy' means:
 * a cyclomatic complexity of 1 to 4
 * no for-loops
 * maximally one variable modified
"""

def are_numbers(x):
    """Determine if `x` is one or more numbers.

    Numbers can be integer or floating point.

    Returns `True` if `x` is one or more numbers.
    """
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return False
    return all(is_number(e) for e in x)

def are_strings(x):
    """Determine if `x` is one or more strings.

    Returns `True` if `x` is one or more strings.
    """
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return False
    return all(is_string(e) for e in x)

def check_are_numbers(x):
    """Determine if `x` is one or more numbers.

    If `x` is not one or more numbers, a `RuntimeError` is raised.

    Returns nothing.
    """
    if not are_numbers(x):
        msg = "'x' must be numbers. "
        raise RuntimeError(
            msg,
            "Actual value of 'x': ", x,
        )


def check_different(a, b):
    """Determine if `a` and `b` are different.

    Raises `RuntimeError` when not.

    Returns nothing.
    """
    if a == b:
        msg = "'a' and 'b' must be different. "
        raise RuntimeError(
            msg,
            "Value of 'a': ", a,
        )

def check_equal(a, b):
    """Determine if `a` and `b` are equal.

    Raises `RuntimeError` when not.

    Returns nothing.
    """
    if a != b:
        msg = "'a' and 'b' must be equal. "
        raise RuntimeError(
            msg,
            "Value of 'a': ", a, ". ",
            "Value of 'b': ", b,
        )

def check_is_number(x):
    """Determine if `x` is a number.

    If `x` is not a number, a `RuntimeError` is raised.

    Returns nothing.
    """
    if not is_number(x):
        msg = "'x' must be a number. "
        raise RuntimeError(
            msg,
            "Actual value of 'x': ", x,
        )

def check_is_probability(x):
    """Determine if `x` is a probability.

    If `x` is not a probability, a `RuntimeError` is raised.

    Returns nothing.
    """
    check_is_number(x)
    if not is_probability(x):
        msg = "'x' must be a probability. "
        raise RuntimeError(
            msg,
            "Actual value of 'x': ", x,
        )

def check_is_string(x):
    """Determine if `x` is a string.

    If `x` is not a string, a `RuntimeError` is raised.

    Returns nothing.
    """
    if not is_string(x):
        msg = "'x' must be a string. "
        raise RuntimeError(
            msg,
            "Actual value of 'x': ", x,
        )

def divide_safely(a, b):
    """Divide `a` by `b`.

    If `a` or `b` are not a floating point number, a `TypeError` is raised.
    If `b` is `0.0`, a `RuntimeError` is raised.

    Returns `a` divided by `b`
    """
    zero = 0.0
    if b == zero:
        msg = "'b' must not be zero"
        raise RuntimeError(
            msg,
        )
    return a / b

def is_dividable_by_three(x):
    """Determine if `x` is dividable by three.

    If `x` is not an integer number, a `TypeError` is raised.

    Returns `True` if `x` is dividable by three
    """
    if not isinstance(x, int):
        msg = "'number' must be a number. Actual type of 'number': "
        raise TypeError(
            msg, type(x),
        )
    return x % 3 == 0

def is_even(x):
    """Determine if `x` is even.

    If `x` is not an integer number, a `TypeError` is raised.

    Returns `True` if `x` is even
    """
    if not isinstance(x, int):
        msg = "'number' must be a number. Actual type of 'number': "
        raise TypeError(
            msg, type(x),
        )
    return x % 2 == 0

def is_number(x):
    """Determine if `x` is one number.

    Determine if `x` is one number,
    for example, '42' or '3.14.

    Returns `True` if `x` is one number
    """
    return isinstance(x, (int, float) )

def is_odd(x):
    """Determine if `x` is odd.

    If `x` is not an integer number, a `TypeError` is raised.

    Returns `True` if `x` is odd
    """
    return not is_even(x)

def is_probability(x):
    """Determine if `x` is a probability.

    Determine if `x` is a probability,
    i.e. a value between 0.0 and 1.0, including both 0.0 and 1.0.
    If `x` is not a floating point number, a `TypeError` is raised.

    Returns `True` if `x` is a probability
    """
    if not isinstance(x, float):
        msg = "'number' must be a floating point number. "
        raise TypeError(
            msg,
            "Actual type of 'number': ", type(x),
        )
    min_probability = 0.0
    max_probability = 1.0
    return x >= min_probability and x <= max_probability

def is_string(x):
    """Determine if `x` is one string.

    Returns `True` if `x` one string
    """
    return isinstance(x, str)

def is_zero(x):
    """Determine if `x` is zero.

    If `x` is not a number, a `TypeError` is raised.

    Returns `True` if `x` is zero
    """
    if not isinstance(x, (int, float)):
        msg = "'number' must be a number. "
        raise TypeError(
            msg,
            "Actual type of 'number': ", type(x),
        )
    return x == 0
