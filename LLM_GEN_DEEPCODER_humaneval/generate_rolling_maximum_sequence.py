from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements up to each position in the input list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A list where each element at position i is the maximum value in the input 
        list from the start up to and including position i.
    
    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    rolling_max_list = []
    current_max = numbers[0]
    
    for num in numbers:
        current_max = max(current_max, num)
        rolling_max_list.append(current_max)
    
    return rolling_max_list