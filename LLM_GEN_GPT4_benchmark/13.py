def greatest_common_divisor(a: int, b: int) -> int:
    # Implementing the Euclidean algorithm to find the GCD
    while b != 0:
        a, b = b, a % b  # Update a to b, and b to the remainder of a divided by b
    return abs(a)  # Return the absolute value to ensure non-negative result