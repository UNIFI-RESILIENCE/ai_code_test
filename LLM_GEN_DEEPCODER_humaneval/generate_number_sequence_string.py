def string_sequence(n: int) -> str:
    """
    Generate a string of space-delimited numbers from 0 up to n inclusive.
    
    Args:
        n: The upper bound of the sequence (inclusive).
        
    Returns:
        A string containing the sequence of numbers separated by spaces.
        
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return ' '.join(str(i) for i in range(n + 1))


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'