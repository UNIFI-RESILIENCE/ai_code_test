from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Linearly rescales a list of numbers to the range [0, 1], where the smallest value becomes 0
    and the largest value becomes 1. Works for both ascending and descending input lists.

    Args:
        numbers: A list of floats with at least two elements.

    Returns:
        A new list of floats transformed to the range [0, 1].
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    
    # Edge case: If all values are the same, return [0.0, 0.0, ...] or handle as needed
    if min_val == max_val:
        return [0.0] * len(numbers)
    
    # Apply linear transformation: (x - min) / (max - min)
    return [(x - min_val) / (max_val - min_val) for x in numbers]