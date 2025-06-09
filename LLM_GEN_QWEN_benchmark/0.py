from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers to make it easier to compare adjacent elements
    sorted_numbers = sorted(numbers)
    
    # Iterate through the sorted list and compare each element with the next one
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between consecutive elements
        diff = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        
        # If the difference is less than the threshold, return True
        if diff < threshold:
            return True
    
    # If no such pair is found, return False
    return False