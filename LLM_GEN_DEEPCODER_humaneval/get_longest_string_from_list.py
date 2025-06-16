from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from the input list. If there are multiple strings with the same
    maximum length, the first occurring one is returned. Returns None if the input list is empty.

    Args:
        strings: A list of strings to evaluate.

    Returns:
        The longest string, or None if the list is empty.
    """
    if not strings:
        return None
    
    max_length = -1
    result = None
    
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            result = s
    
    return result