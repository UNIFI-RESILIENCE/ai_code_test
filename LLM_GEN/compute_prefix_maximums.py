Here's the optimum implementation of the rolling_max function that meets the given requirements:

from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    current_max = float('-inf')
    for num in numbers:
        current_max = max(current_max, num)
        result.append(current_max)
    return result

This implementation ensures optimal performance with a single pass through the list (O(n) time complexity) and uses only constant additional space.