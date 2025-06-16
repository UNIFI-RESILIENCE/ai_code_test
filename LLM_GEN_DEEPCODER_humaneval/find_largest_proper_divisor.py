def largest_divisor(n: int) -> int:
    """
    Finds the largest divisor of n that is smaller than n.
    
    Args:
        n: The number to find the largest divisor for.
        
    Returns:
        The largest divisor of n that is smaller than n. Returns 1 if n is prime.
        
    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(7)
        1
    """
    if n <= 1:
        raise ValueError("n must be greater than 1")
    
    # Iterate from n//2 down to 1 to find the largest divisor
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    return 1


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7