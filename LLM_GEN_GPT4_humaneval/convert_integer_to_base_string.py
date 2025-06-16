def change_base(x: int, base: int) -> str:
    # Handle the special case where x is zero
    if x == 0:
        return "0"
    
    digits = []
    
    # Repeatedly divide x by the base and store the remainders
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))  # Convert remainder to string and append to digits list
        x //= base  # Update x to the quotient for next iteration
    
    # The digits are collected in reverse order, so reverse and join them
    return ''.join(reversed(digits))