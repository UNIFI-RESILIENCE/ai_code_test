from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Count the frequency of each number in the input list
    frequency = Counter(numbers)
    
    # Initialize a list to store elements that occur exactly once
    unique_numbers = []
    
    # Iterate through the original list to maintain order
    for num in numbers:
        # Include the number only if its frequency is 1
        if frequency[num] == 1:
            unique_numbers.append(num)
    
    return unique_numbers