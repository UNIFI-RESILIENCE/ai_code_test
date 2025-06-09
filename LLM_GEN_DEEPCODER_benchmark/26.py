from typing import List
from collections import defaultdict


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once."""
    # Use defaultdict to count occurrences of each number
    count_map = defaultdict(int)
    
    # First pass: count occurrences of each number
    for num in numbers:
        count_map[num] += 1
    
    # Second pass: filter numbers that occurred only once
    return [num for num in numbers if count_map[num] == 1]