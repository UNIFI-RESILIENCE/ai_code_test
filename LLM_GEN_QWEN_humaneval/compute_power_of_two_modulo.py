def modp(n: int, p: int) -> int:
    # Use Python's built-in pow function to compute (2^n) % p efficiently.
    # The third argument of pow allows us to compute the result modulo p directly.
    return pow(2, n, p)

# Define a check function to verify the correctness of the modp function.
def check(candidate):
    assert candidate(3, 5) == 3, "Test case 1 failed"
    assert candidate(1101, 101) == 2, "Test case 2 failed"
    assert candidate(0, 101) == 1, "Test case 3 failed"
    assert candidate(3, 11) == 8, "Test case 4 failed"
    assert candidate(100, 101) == 1, "Test case 5 failed"
    assert candidate(30, 5) == 4, "Test case 6 failed"
    assert candidate(31, 5) == 3, "Test case 7 failed"

# Run the check function to validate the implementation
check(modp)