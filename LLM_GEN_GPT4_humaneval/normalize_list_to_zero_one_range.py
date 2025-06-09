from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)  # Find the minimum value in the list
    max_val = max(numbers)  # Find the maximum value in the list
    range_val = max_val - min_val  # Calculate the range

    # Avoid division by zero in case all values are the same
    if range_val == 0:
        return [0.0 for _ in numbers]

    # Apply the rescaling transformation: (x - min) / (max - min)
    return [(x - min_val) / range_val for x in numbers]