"""General-purpose functions of moderate complexity.

Moderate complexity' means:
 * a cyclomatic complexity of 1 to 8
 * may have for-loops
 * maximally two variables modified
 * indeterministic

0: `is_prime(x)`
1: `get_digits(x)`
2a: `flip_coin(x)`
2b: `roll_dice(x)`
"""


"""This is an example function"""

def is_prime(x):
    """Determine if `x` is prime.

    Returns True if `x` is an integer that is prime.
    Returns False if `x` is an integer that is not prime.
    Raises a TypeError if `x` is not an integer
    """
    if not isinstance(x, int):
        message = "'x' must be an integer"
        raise TypeError(message)
    first_prime = 2
    if x < first_prime:
        return False
    return all(x % i != 0 for i in range(first_prime, x))

"""Exercise 1: develop the function 'get_digits'

This function splits up a number in its digits [*],
for example '12' becomes '[1, 2]'.

-   Pair up
-   Switch roles every 3 minutes
-   Discuss how to keep the time first
-   Person with GitHub username first in alphabet starts
-   Create a Fork of <https://github.com/richelbilderbeek/programming_formalisms_medium_project>
-   Develop a function called `get_digits`
-   Try to be **exemplary**

[*] vague on purpose
"""


"""Exercise 2a: develop the function 'flip_coin'

This function returns either True of False, as if determined by the flip of a coin [*].

-   Pair up
-   Switch roles every 3 minutes
-   Discuss how to keep the time first
-   Person with GitHub username first in alphabet starts
-   Create a Fork of <https://github.com/richelbilderbeek/programming_formalisms_medium_project>
-   Develop a function called `get_digits`
-   Try to be **exemplary**

[*] vague on purpose

"""

"""Exercise 2b: develop the function 'roll_dice'

This function returns a number between 1 and 6,
as if determined by the roll of a dice [*].

-   Pair up
-   Switch roles every 3 minutes
-   Discuss how to keep the time first
-   Person with GitHub username first in alphabet starts
-   Create a Fork of <https://github.com/richelbilderbeek/programming_formalisms_medium_project>
-   Develop a function called `get_digits`
-   Try to be **exemplary**

[*] vague on purpose
"""
