from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the numbers to bring close values next to each other
    sorted_numbers = sorted(numbers)
    
    # Iterate through pairs of adjacent elements and check their absolute difference
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i + 1] - sorted_numbers[i]) < threshold:
            return True  # Found a pair with difference less than threshold
    
    return False  # No such pair found