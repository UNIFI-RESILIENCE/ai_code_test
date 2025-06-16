def change_base(x: int, base: int) -> str:
    """
    Converts a given integer x to a specified base (less than 10) and returns the string representation.
    
    Args:
        x: The integer to be converted (must be non-negative).
        base: The target base (must be between 2 and 9).
    
    Returns:
        String representation of x in the given base.
    
    Raises:
        ValueError: If base is not between 2 and 9 or if x is negative.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x < 0:
        raise ValueError("x must be non-negative")
    
    if x == 0:
        return "0"
    
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x = x // base
    
    # The digits are collected in reverse order
    return ''.join(reversed(digits))