def get_positive(l: list) -> list:
    # Use a list comprehension to filter and return only positive numbers from the list
    return [num for num in l if num > 0]

# METADATA dictionary (currently empty, but can be used to store additional information)
METADATA = {}

# Function to check the correctness of the get_positive function
def check(candidate):
    # Test cases to verify the function's behavior
    assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6], "Test case 1 failed"
    assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1], "Test case 2 failed"
    assert candidate([-1, -2]) == [], "Test case 3 failed"
    assert candidate([]) == [], "Test case 4 failed"

# Run the check function with get_positive as the candidate function
check(get_positive)