from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Generate all prefixes of the input string, ordered from shortest to longest.
    
    Args:
        string: The input string for which prefixes are to be generated.
    
    Returns:
        A list of strings representing all prefixes of the input string, 
        ordered from shortest to longest.
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]