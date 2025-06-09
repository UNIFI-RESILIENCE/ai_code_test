from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filters a list of mixed Python values, returning only the integers.
    
    Args:
        values: A list containing any Python values (e.g., strings, floats, lists, etc.)
    
    Returns:
        A new list containing only the integer values from the input list.
        
    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if type(x) is int]