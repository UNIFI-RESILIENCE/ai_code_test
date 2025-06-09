from typing import List


def factorize(n: int) -> List[int]:
    factors = []  # Initialize an empty list to store the prime factors

    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)  # Append 2 to the list of factors
        n //= 2  # Divide n by 2

    # n must be odd at this point, so a skip of 2 (i.e., check only odd numbers) is possible
    factor = 3
    max_factor = int(n**0.5) + 1  # Calculate the maximum factor to check

    # Check for odd factors from 3 to sqrt(n)
    while factor <= max_factor:
        while n % factor == 0:
            factors.append(factor)  # Append the factor to the list
            n //= factor  # Divide n by the factor
        factor += 2  # Move to the next odd number

    # If n is still greater than 2, then n must be a prime number
    if n > 2:
        factors.append(n)  # Append the remaining prime factor

    return factors  # Return the list of prime factors


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