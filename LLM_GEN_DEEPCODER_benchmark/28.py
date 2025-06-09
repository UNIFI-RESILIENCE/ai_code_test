from typing import List


def concatenate(strings: List[str]) -> str:
    """Concatenate list of strings into a single string.
    
    Args:
        strings: List of strings to be concatenated
        
    Returns:
        Single string formed by concatenating all input strings
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Using join() is the most efficient way to concatenate strings in Python
    # as it avoids creating intermediate string objects
    return ''.join(strings)