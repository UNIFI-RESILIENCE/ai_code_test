Here is the optimum implementation for the given prompt:

from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [v for v in values if type(v) is int]

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate([]) == []
    assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]

This solution uses a list comprehension to filter values of exact type int, ensuring that booleans (which are subclasses of int) are excluded.