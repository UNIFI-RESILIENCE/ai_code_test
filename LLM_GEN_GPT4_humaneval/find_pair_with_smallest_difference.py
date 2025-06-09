from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # First, sort the list to bring close elements next to each other
    sorted_numbers = sorted(numbers)

    # Initialize minimum difference with a large number
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])

    # Iterate through the sorted list to find the pair with the smallest difference
    for i in range(len(sorted_numbers) - 1):
        a, b = sorted_numbers[i], sorted_numbers[i + 1]
        diff = b - a
        if diff < min_diff:
            min_diff = diff
            closest_pair = (a, b)

    return closest_pair