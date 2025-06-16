def greatest_common_divisor(a: int, b: int) -> int:
    # Base case: if b is zero, the GCD is a
    while b != 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b
    # When b becomes zero, a contains the GCD
    return a

# Example Usage
# print(greatest_common_divisor(3, 5))  # Output: 1
# print(greatest_common_divisor(25, 15)) # Output: 5