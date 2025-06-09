from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Finds the two closest numbers in a list and returns them in ascending order.
    
    Args:
        numbers: A list of floats with at least two elements.
    
    Returns:
        A tuple containing the two closest numbers in ascending order.
    
    Approach:
        1. Sort the input list to easily compare adjacent elements.
        2. Iterate through the sorted list to find the pair with the smallest difference.
        3. Return the closest pair in ascending order.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    # Sort the list to easily compare adjacent elements
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    
    # Iterate through the sorted list to find the smallest difference
    for i in range(len(sorted_numbers) - 1):
        current_diff = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair