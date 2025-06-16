def largest_divisor(n: int) -> int:
    # Start checking from n // 2 down to 1
    # This is because any divisor larger than n // 2 cannot be less than n itself
    for potential_divisor in range(n // 2, 0, -1):
        # If potential_divisor divides n evenly, return it immediately
        if n % potential_divisor == 0:
            return potential_divisor
    # If no divisors are found (which theoretically shouldn't happen for n > 1),
    # return 1 as the smallest possible divisor
    return 1

# Metadata dictionary (not used in the function, but included as per your request)
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the largest_divisor function
def check(candidate):
    assert candidate(3) == 1, "Test case 1 failed"
    assert candidate(7) == 1, "Test case 2 failed"
    assert candidate(10) == 5, "Test case 3 failed"
    assert candidate(100) == 50, "Test case 4 failed"
    assert candidate(49) == 7, "Test case 5 failed"

# Run the check function to verify the implementation
check(largest_divisor)