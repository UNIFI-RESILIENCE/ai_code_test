def change_base(x: int, base: int):
    # Validate that base is between 2 and 9 (inclusive)
    if not (2 <= base < 10):
        raise ValueError("Base must be between 2 and 9 inclusive.")
    
    # Edge case: if x is 0, the result is '0' in any base
    if x == 0:
        return '0'
    
    digits = []

    # Perform repeated division to convert the number to the target base
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))  # Append the remainder as the next digit
        x //= base                     # Reduce x by dividing it by the base

    # Reverse the digits since the conversion process produces them in reverse order
    return ''.join(reversed(digits))