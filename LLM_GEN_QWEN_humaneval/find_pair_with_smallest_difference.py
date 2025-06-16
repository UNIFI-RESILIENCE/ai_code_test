from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers to ensure we can find the closest pair by simply comparing adjacent elements
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to store the smallest difference and the closest pair
    min_diff = float('inf')
    closest_pair = (0.0, 0.0)
    
    # Iterate over the sorted list and find the pair with the smallest difference
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair


# Metadata for reference
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Test cases to validate the function
def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1)


# Running the check function to validate the solution
check(find_closest_elements)