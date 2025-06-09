from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`."""
    result = []
    
    # Iterate through each element in the input list
    for i, num in enumerate(numbers):
        # Add the current number to the result
        result.append(num)
        
        # Add the delimeter after each element except the last one
        if i != len(numbers) - 1:
            result.append(delimeter)
    
    return result