from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from the input list. In case of multiple strings with 
    the same maximum length, returns the first occurrence. Returns None if the input 
    list is empty.
    
    Args:
        strings: A list of strings to evaluate.
        
    Returns:
        The longest string (or first of equal length), or None if input is empty.
    """
    if not strings:
        return None
    # Iterate through the list, keeping track of the longest string found so far
    longest_str = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest_str):
            longest_str = s
    return longest_str