def change_base(x: int, base: int) -> str:
    # Initialize an empty list to store remainders which represent digits in the new base
    digits = []
    
    # Edge case for zero as any number in any base is zero
    if x == 0:
        return '0'
    
    # While loop to repeatedly divide the number by the base and store remainders
    while x > 0:
        remainder = x % base  # Get the remainder when x is divided by base
        digits.append(str(remainder))  # Convert remainder to string and add to list
        x = x // base  # Update x by performing integer division by base
    
    # The digits are stored in reverse order, so reverse them
    digits.reverse()
    
    # Join the list of strings into a single string to get the final result
    return ''.join(digits)

# Example usage:
# print(change_base(8, 3))  # Output: '22'
# print(change_base(8, 2))  # Output: '1000'
# print(change_base(7, 2))  # Output: '111'