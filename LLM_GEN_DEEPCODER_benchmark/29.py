from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filters a list of strings, returning only those that start with the given prefix.
    
    Args:
        strings: List of strings to filter
        prefix: The prefix to check for
        
    Returns:
        List of strings that start with the given prefix (maintaining original order)
    
    Examples:
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
        >>> filter_by_prefix([], 'a')
        []
    """
    return [s for s in strings if s.startswith(prefix)]