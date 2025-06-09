def change_base(x: int, base: int) -> str:
    """
    Converts an integer from base 10 to a specified base (less than 10).
    
    Args:
        x: The integer to be converted (base 10)
        base: The target base (must be less than 10)
    
    Returns:
        String representation of the number in the target base
    
    Example:
        >>> change_base(8, 2)
        '1000'
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    
    if x == 0:
        return "0"
    
    digits = []
    is_negative = False
    
    # Handle negative numbers
    if x < 0:
        is_negative = True
        x = -x
    
    # Convert to target base
    while x > 0:
        digits.append(str(x % base))
        x = x // base
    
    # Add negative sign if needed and reverse digits
    if is_negative:
        digits.append('-')
    
    # Join digits in reverse order
    return ''.join(reversed(digits)) if digits else '0'
```

Key features of this implementation:
1. Input validation for base (must be between 2 and 9)
2. Handles zero as a special case
3. Properly processes negative numbers
4. Uses modulo and division operations to build the converted number digit by digit
5. Efficient string construction by reversing the collected digits

The algorithm follows the standard base conversion approach:
- Repeatedly divide the number by the base and collect remainders
- The remainders (in reverse order) form the converted number

Example usage:
```python
print(change_base(8, 2))  # Output: '1000'
print(change_base(-8, 3)) # Output: '-22'