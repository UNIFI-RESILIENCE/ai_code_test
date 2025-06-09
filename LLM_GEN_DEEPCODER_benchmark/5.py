from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Inserts a delimeter between every two consecutive elements of the input list.
    
    Args:
        numbers: List of integers to be processed
        delimeter: Integer to be inserted between elements
        
    Returns:
        New list with delimeter inserted between original elements
    """
    # Handle empty list case immediately
    if not numbers:
        return []
    
    # Initialize result with first element to avoid leading delimeter
    result = [numbers[0]]
    
    # Iterate through remaining elements, adding delimeter before each
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
        
    return result