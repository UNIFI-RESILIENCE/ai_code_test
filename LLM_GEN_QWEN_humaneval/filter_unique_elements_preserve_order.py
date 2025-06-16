from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Count occurrences of each number in the list
    counts = Counter(numbers)
    
    # Filter numbers, keeping only those that occur exactly once, maintaining original order
    return [num for num in numbers if counts[num] == 1]

# Metadata about the code snippet
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

# Example usage of the function
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Output should be [1, 3, 4]