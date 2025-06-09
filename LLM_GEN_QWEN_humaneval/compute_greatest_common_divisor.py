def greatest_common_divisor(a: int, b: int) -> int:
    # Use the Euclidean algorithm to find the greatest common divisor
    while b != 0:
        a, b = b, a % b  # Replace a with b and b with a % b until b becomes 0
    return a  # When b is 0, a contains the GCD

# Metadata for tracking the author and dataset
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the greatest_common_divisor function
def check(candidate):
    assert candidate(3, 7) == 1, "Test case 1 failed: GCD of 3 and 7 should be 1"
    assert candidate(10, 15) == 5, "Test case 2 failed: GCD of 10 and 15 should be 5"
    assert candidate(49, 14) == 7, "Test case 3 failed: GCD of 49 and 14 should be 7"
    assert candidate(144, 60) == 12, "Test case 4 failed: GCD of 144 and 60 should be 12"
    print("All test cases passed!")

# Run the check function to validate the implementation
check(greatest_common_divisor)