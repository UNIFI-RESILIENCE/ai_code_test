from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Identify the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Calculate the range (difference between max and min)
    range_val = max_val - min_val

    # Avoid division by zero if all values in the list are the same
    if range_val == 0:
        # All values are the same; return a list of zeros
        return [0.0 for _ in numbers]

    # Apply linear transformation to rescale each number to the [0,1] interval
    return [(x - min_val) / range_val for x in numbers]