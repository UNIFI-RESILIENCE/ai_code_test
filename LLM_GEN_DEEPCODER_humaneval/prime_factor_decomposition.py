from typing import List

def factorize(n: int) -> List[int]:
    """Return the prime factorization of n as a list of primes in ascending order with multiplicity."""
    if n == 1:
        return []
    factors = []
    # Divide by 2 first to handle even numbers efficiently
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Check for odd divisors up to sqrt(n)
    i = 3
    max_factor = int(n ** 0.5) + 1
    while i <= max_factor:
        while n % i == 0:
            factors.append(i)
            n = n // i
            max_factor = int(n ** 0.5) + 1  # Update max factor after dividing
        i += 2
    if n > 1:
        factors.append(n)
    return factors