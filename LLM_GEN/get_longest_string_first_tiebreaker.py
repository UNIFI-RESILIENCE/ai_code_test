Here's the optimum implementation for the longest function, adhering to the specifications in the docstring:

from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

This version uses Python's built-in max function with the key=len argument, which efficiently finds the longest string and returns the first one encountered in case of ties. This solution also correctly handles the empty list case by returning None.