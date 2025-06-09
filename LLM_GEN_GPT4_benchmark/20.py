from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list to bring closest elements adjacent to each other
    sorted_numbers = sorted(numbers)
    
    # Initialize minimum difference with a large number
    min_diff = float('inf')
    closest_pair = (0.0, 0.0)

    # Iterate through the sorted list and compare adjacent elements
    for i in range(len(sorted_numbers) - 1):
        a, b = sorted_numbers[i], sorted_numbers[i + 1]
        diff = abs(b - a)

        # Update the closest pair if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (a, b)

    return closest_pair