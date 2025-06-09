def greatest_common_divisor(a: int, b: int) -> int:
    # Use the Euclidean algorithm to compute the greatest common divisor (GCD)
    while b != 0:
        a, b = b, a % b  # Replace a with b and b with the remainder of a divided by b
    return abs(a)  # Return the absolute value to handle negative inputs gracefully

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12