"""Easy general-purpose functions.

'Easy' means:
 * a cyclomatic complexity of 1 to 4
 * no for-loops
 * maximally one variable modified

0: `is_zero(x)`
1: `is_even(x)`
2: `is_odd(x)`
3: `is_probability(p)`
4: `is_number(x)`
5: `are_numbers(x)`
S1: `is_roman_number(x)`
"""

"""Example function: `is_zero(x)`."""

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

"""Exercise 1: develop the function 'is_even'.

In this context, 'even', means 'dividable by two', e.g. 2, 4, -6, 0.

-   Create a GitHub repository called `is_even`
-   Develop a function called `is_even`
-   Try to be **exemplary**
"""

"""Exercise 2: develop the function 'is_odd'

In this context, 'odd', means 'not dividable by two', e.g. 1, 3, -5.

-   Create a GitHub repository called `is_odd`
-   Develop a function called `is_odd`
-   Try to be **exemplary**
"""

"""Exercise 3: develop the function 'is_probability'.

In this context: the change of something happening;
a value between zero and one, including zero and one.

-   Create a GitHub repository called `is_probability`
-   Develop a function called `is_probability`
-   Try to be **exemplary**
"""

"""Exercise 4: develop the function 'is_number'.

This function determines if an object is a number.

-   Create a GitHub repository called `is_number`
-   Develop a function called `is_number`
-   Try to be **exemplary**
"""

"""Exercise 5: develop the function 'are_numbers'.

This function determines if the input are numbers [*],
similar to `is_number`, but for more numbers.

-   Create a GitHub repository called `are_numbers`
-   Develop a function called `are_numbers`
-   Try to be **exemplary**

[*] vague on purpose
"""

"""Exercise S1: develop the function 'is_roman_number'.

This function determines if a string is a roman number.

Examples are: 'I', 'II', 'IV', 'XI', etc.

-   Create a GitHub repository called `is_roman_number`
-   Develop a function called `is_roman_number`
-   Try to be **exemplary**
"""

"""Exercise S2: develop the function 'is_prime'.

This function determines if a number is a prime number.

-   Create a GitHub repository called `is_prime`
-   Develop a function called `is_prime`
-   Try to be **exemplary**
"""

