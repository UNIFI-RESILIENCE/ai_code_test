from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from the given list of integers.
    The rolling maximum at each position is the maximum value encountered up to that point in the list.
    
    Args:
        numbers: List of integers to compute rolling maximum for.
    
    Returns:
        List of integers representing the rolling maximum at each position.
    
    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    rolling_max_list = []
    current_max = numbers[0]
    
    for num in numbers:
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)
    
    return rolling_max_list