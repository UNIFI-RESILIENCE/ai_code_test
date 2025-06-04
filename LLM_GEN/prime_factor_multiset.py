Here's the optimum implementation of the factorize function to return the list of prime factors of a given integer n:

from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    """
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

This implementation uses trial division starting from 2 and continues up to the square root of n. If n is still greater than 1 after the loop, then n itself is a prime number and is added to the result.