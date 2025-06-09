from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the input list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Calculate the range of the values
    range_val = max_val - min_val
    
    # Handle edge case where all numbers are the same to avoid division by zero
    if range_val == 0:
        return [0.0] * len(numbers)
    
    # Apply linear transformation: (x - min) / range
    return [(x - min_val) / range_val for x in numbers]