from typing import List
from collections import defaultdict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """Remove all elements that occur more than once, preserving the original order."""
    # Use a dictionary to count occurrences of each number
    count_map = defaultdict(int)
    for num in numbers:
        count_map[num] += 1
    
    # Filter the original list to keep only numbers that occur once
    result = [num for num in numbers if count_map[num] == 1]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()