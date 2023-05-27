"""The functions from The Medium Project."""

def are_primes(xs):
    """Determine for each element in `xs` if it is prime.

    Input: `xs`: a list of integers

    Returns a list of booleans with the same length as `xs`.
    Returns an empty list if `xs` is empty.
    Raises TypeError if `xs` is not a list of integers, nor an empty list.
    """
    return are_primes_no_cache(xs)

def are_primes_cache_with_dict(xs):
    """Determine for each element in `xs` if it is prime.

    This function stores the results of earlier calculations
    in a dictionary. The dictionary stores if a number is prime yes/no.

    Input: `xs`: a list of integers

    Returns a list of booleans with the same length as `xs`.
    Returns an empty list if `xs` is empty.
    Raises TypeError if `xs` is not a list of integers, nor an empty list.
    """
    if len(xs) == 0:
        return []
    unique_xs_set = set(xs)
    n_unique_xs = len(unique_xs_set)
    nones = [None] * n_unique_xs
    unique_xs_dict = dict(zip(unique_xs_set, nones))
    for e in unique_xs_dict:
        unique_xs_dict[e] = is_prime(e)
    return [unique_xs_dict[x] for x in xs]

def are_primes_cache_with_set(xs):
    """Determine for each element in `xs` if it is prime.

    This function uses a set to store all (unique) integers in `xs`
    that are prime, after which it looks up for each element in `xs`
    if it is in that set.

    Input: `xs`: a list of integers

    Returns a list of booleans with the same length as `xs`.
    Returns an empty list if `xs` is empty.
    Raises TypeError if `xs` is not a list of integers, nor an empty list.
    """
    if len(xs) == 0:
        return []
    unique_xs_list = list(set(xs))
    are_unique_xs_primes = are_primes_no_cache(unique_xs_list)
    assert len(unique_xs_list) == len(are_unique_xs_primes)
    xs_that_are_prime = [
        unique_xs_list[i] for i in range(len(unique_xs_list)) if are_unique_xs_primes[i]
    ]
    return [i in xs_that_are_prime for i in xs]


def are_primes_no_cache(xs):
    """Determine for each element in `xs` if it is prime.

    This function does not store the results of earlier calculations.
    Instead, for each integer element in `xs` it is determined if it is prime,
    even if all elements are the same.

    Input: `xs`: a list of integers

    Returns a list of booleans with the same length as `xs`.
    Returns an empty list if `xs` is empty.
    Raises TypeError if `xs` is not a list of integers, nor an empty list.
    """
    return [is_prime(i) for i in xs]

def are_primes_no_cache_recursion(xs):
    """Determine for each element in `xs` if it is prime.

    This function does not store the results of earlier calculations.
    Instead, for each integer element in `xs` it is determined if it is prime,
    even if all elements are the same.

    Input: `xs`: a list of integers

    Returns a list of booleans with the same length as `xs`.
    Returns an empty list if `xs` is empty.
    Raises TypeError if `xs` is not a list of integers, nor an empty list.
    """
    return [is_prime_recursive(i) for i in xs]

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

def is_prime_recursive(n, i = 2):
    """Determine if `x` is prime.

    Returns True if `x` is an integer that is prime.
    Returns False if `x` is an integer that is not prime.
    Raises a TypeError if `x` is not an integer

    Modified after code by Smitha Dinesh Semwal
    from https://www.geeksforgeeks.org/recursive-program-prime-number/
    """
    if not isinstance(n, int):
        message = "'n' must be an integer"
        raise TypeError(message)
    lowest_prime = 2

    if n <= lowest_prime:
        return n == lowest_prime
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime_recursive(n, i + 1)

