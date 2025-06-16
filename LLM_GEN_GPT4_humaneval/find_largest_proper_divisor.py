def largest_divisor(n: int) -> int:
    # Iterate from n // 2 down to 1 to find the largest proper divisor
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    # Fallback (this should never be reached for n > 1)
    return 1


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test with small prime number
    assert candidate(3) == 1
    # Test with another prime number
    assert candidate(7) == 1
    # Test with even number
    assert candidate(10) == 5
    # Test with round number
    assert candidate(100) == 50
    # Test with square of a prime
    assert candidate(49) == 7