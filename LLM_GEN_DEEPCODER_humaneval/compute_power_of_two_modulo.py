def modp(n: int, p: int) -> int:
    """Compute 2 raised to the power n modulo p efficiently using modular exponentiation.
    
    Args:
        n: The exponent in 2^n.
        p: The modulus value (must be a positive integer).
    
    Returns:
        The result of 2^n mod p.
    
    Examples:
        >>> modp(3, 5)
        3
        >>> modp(1101, 101)
        2
        >>> modp(0, 101)
        1
    """
    if p == 1:
        return 0
    
    result = 1
    base = 2 % p
    
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n = n // 2
    
    return result