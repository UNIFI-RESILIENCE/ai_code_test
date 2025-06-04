Here's the optimum implementation of the greatest_common_divisor function using the efficient Euclidean algorithm:

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)  # Ensure the result is non-negative

This implementation is both concise and efficient, and it passes all the test cases in the check function.