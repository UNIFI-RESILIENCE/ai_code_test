def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        The greatest common divisor of a and b
    
    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Ensure both numbers are non-negative since GCD is defined for absolute values
    a, b = abs(a), abs(b)
    
    # Implement Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    
    return a