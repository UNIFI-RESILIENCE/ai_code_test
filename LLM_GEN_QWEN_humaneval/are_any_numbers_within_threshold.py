from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers to bring close elements next to each other
    sorted_numbers = sorted(numbers)
    
    # Iterate through the sorted list and check the difference between consecutive elements
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True  # Return True if any two consecutive elements are closer than the threshold
    
    return False  # Return False if no such pair is found

# Metadata about the code
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the `has_close_elements` function
def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True, "Test case 1 failed"
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False, "Test case 2 failed"
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True, "Test case 3 failed"
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False, "Test case 4 failed"
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True, "Test case 5 failed"
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True, "Test case 6 failed"
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False, "Test case 7 failed"