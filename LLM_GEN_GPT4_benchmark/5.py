from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    # If the input list is empty or contains only one element, 
    # return it as is since there are no gaps to insert delimiters
    if len(numbers) <= 1:
        return numbers[:]
    
    # Initialize a new list to hold the result
    result = []

    # Iterate through the list except the last element
    for i in range(len(numbers) - 1):
        result.append(numbers[i])      # Add current number
        result.append(delimeter)       # Add delimiter between elements

    # Append the last number, after which no delimiter is needed
    result.append(numbers[-1])
    
    return result