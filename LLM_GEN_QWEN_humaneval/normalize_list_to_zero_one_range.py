from typing import List

# Function to rescale a list of numbers to a range between 0 and 1
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Calculate the range (difference between max and min) to avoid redundant computation
    range_val = max_val - min_val
    
    # Check if the range is zero to prevent division by zero error
    # If all numbers are the same, they will all be rescaled to 0
    if range_val == 0:
        return [0.0] * len(numbers)
    
    # Apply the linear transformation formula to each number in the list
    # Formula: (number - min_val) / range_val
    rescaled_numbers = [(num - min_val) / range_val for num in numbers]
    
    return rescaled_numbers


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Testing function to check the correctness of the rescale_to_unit function
def check(candidate):
    assert candidate([2.0, 49.9]) == [0.0, 1.0], "Test case 1 failed"
    assert candidate([100.0, 49.9]) == [1.0, 0.0], "Test case 2 failed"
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0], "Test case 3 failed"
    assert candidate([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75], "Test case 4 failed"
    assert candidate([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75], "Test case 5 failed"

# Example usage of the check function with the target function
check(rescale_to_unit)