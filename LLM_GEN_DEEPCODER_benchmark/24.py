def largest_divisor(n: int) -> int:
    """
    Finds the largest divisor of n that is smaller than n.
    
    Args:
        n: The input number to find the largest divisor for.
    
    Returns:
        The largest divisor of n that is smaller than n. Returns -1 if no such divisor exists (i.e., n <= 1).
    
    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
        >>> largest_divisor(1)
        -1
    """
    if n <= 1:
        return -1
    
    # Iterate from n//2 down to 1 to find the largest divisor
    for i in range(n // 2, 0, -):
        if n % i == 0:
            return i
    
    # This line is theoretically unreachable for n > 1
    return -1