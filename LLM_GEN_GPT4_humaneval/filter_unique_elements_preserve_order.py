from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Count the frequency of each number in the list
    counts = Counter(numbers)
    # Return elements that occur exactly once, preserving input order
    return [num for num in numbers if counts[num] == 1]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]