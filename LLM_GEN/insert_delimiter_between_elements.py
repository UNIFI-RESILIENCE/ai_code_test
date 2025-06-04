Here's the optimum implementation of the intersperse function based on the given prompt:

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
    return result

This code handles all scenarios including empty input and ensures that the delimiter is inserted between each pair of elements but not at the beginning or end.