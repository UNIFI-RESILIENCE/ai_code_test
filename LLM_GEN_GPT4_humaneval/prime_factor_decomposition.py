from typing import List

def factorize(n: int) -> List[int]:
    # Initialize an empty list to store the prime factors
    factors = []
    
    # Divide out all factors of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors from 3 up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2  # Only test odd numbers since even numbers are not prime (except 2)

    # If n is greater than 1 here, it is a prime number
    if n > 1:
        factors.append(n)

    return factors


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(2) == [2]
    assert candidate(4) == [2, 2]
    assert candidate(8) == [2, 2, 2]
    assert candidate(3 * 19) == [3, 19]
    assert candidate(3 * 19 * 3 * 19) == [3, 3, 19, 19]
    assert candidate(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
    assert candidate(3 * 19 * 19 * 19) == [3, 19, 19, 19]
    assert candidate(3 * 2 * 3) == [2, 3, 3]