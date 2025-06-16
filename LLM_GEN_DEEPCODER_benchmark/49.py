def modp(n: int, p: int) -> int:
    """
    Efficiently computes 2^n modulo p using modular exponentiation to avoid large intermediate values.
    
    Args:
        n: The exponent in 2^n.
        p: The modulus value.
    
    Returns:
        The result of 2^n modulo p.
    
    Examples:
        >>> modp(3, 5)
        3
        >>> modp(1101, 101)
        2
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