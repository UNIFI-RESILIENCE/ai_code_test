from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Handle the case where all numbers are the same
    if min_val == max_val:
        return [0.0] * len(numbers)
    
    # Apply the linear transformation to scale the numbers
    return [(x - min_val) / (max_val - min_val) for x in numbers]