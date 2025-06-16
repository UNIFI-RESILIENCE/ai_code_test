from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Find the two closest numbers in a list and return them in ascending order."""
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    # Sort the numbers to minimize the number of comparisons needed
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    result = (sorted_numbers[0], sorted_numbers[1])
    
    # Iterate through consecutive pairs to find the smallest difference
    for i in range(len(sorted_numbers) - 1):
        current_diff = sorted_numbers[i+1] - sorted_numbers[i]
        if current_diff < min_diff:
            min_diff = current_diff
            result = (sorted_numbers[i], sorted_numbers[i+1])
    
    return result