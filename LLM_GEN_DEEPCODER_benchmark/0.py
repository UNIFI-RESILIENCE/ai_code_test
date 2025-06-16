from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if any two distinct numbers in the list are closer to each other than the threshold.
    
    Args:
        numbers: List of floating-point numbers
        threshold: Minimum distance between elements to check against
        
    Returns:
        bool: True if any two elements are closer than threshold, False otherwise
    
    Approach:
        - First sort the list to easily compare adjacent elements
        - Then iterate through the sorted list checking consecutive elements
        - This reduces time complexity from O(n^2) to O(n log n)
    """
    if len(numbers) < 2:
        return False
        
    sorted_numbers = sorted(numbers)
    
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True
            
    return False