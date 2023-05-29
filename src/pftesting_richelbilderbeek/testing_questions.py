"""Functions for the 'Testing' lesson.

0: `is_zero(x)` (example function)
1: `is_prime(x)`
2: `get_digits(x)`
3: `flip_coin(x)`
4: `roll_dice(x)`
"""


"""This is an example function"""

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


"""Exercise 1: develop the function 'is_prime'

This function determines if a number is prime.

-   Pair up
-   Switch roles every 3 minutes
-   Discuss how to keep the time first
-   Person with GitHub username first in alphabet starts
-   Create a Fork of <https://github.com/richelbilderbeek/programming_formalisms_testing>
-   Develop a function called `is_prime`
-   Try to be **exemplary**

[*] vague on purpose
"""


"""Exercise 2: develop the function 'get_digits'

This function splits up a number in its digits [*],
for example '12' becomes '[1, 2]'.

-   Pair up
-   Switch roles every 3 minutes
-   Discuss how to keep the time first
-   Person with GitHub username first in alphabet starts
-   Create a Fork of <https://github.com/richelbilderbeek/programming_formalisms_testing>
-   Develop a function called `get_digits`
-   Try to be **exemplary**

[*] vague on purpose
"""


"""Exercise 3: develop the function 'flip_coin'

This function returns either True of False, as if determined by the flip of a coin [*].

-   Pair up
-   Switch roles every 3 minutes
-   Discuss how to keep the time first
-   Person with GitHub username first in alphabet starts
-   Create a Fork of <https://github.com/richelbilderbeek/programming_formalisms_testing>
-   Develop a function called `get_digits`
-   Try to be **exemplary**

[*] vague on purpose

"""

"""Exercise 4: develop the function 'roll_dice'

This function returns a number between 1 and 6,
as if determined by the roll of a dice [*].

-   Pair up
-   Switch roles every 3 minutes
-   Discuss how to keep the time first
-   Person with GitHub username first in alphabet starts
-   Create a Fork of <https://github.com/richelbilderbeek/programming_formalisms_testing>
-   Develop a function called `get_digits`
-   Try to be **exemplary**

[*] vague on purpose
"""
