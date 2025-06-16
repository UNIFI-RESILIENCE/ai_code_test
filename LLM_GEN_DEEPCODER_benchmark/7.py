from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filters a list of strings, returning only those that contain the specified substring.
    
    Args:
        strings: List of strings to be filtered.
        substring: Substring to search for within each string.
    
    Returns:
        List of strings that contain the given substring.
    
    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]