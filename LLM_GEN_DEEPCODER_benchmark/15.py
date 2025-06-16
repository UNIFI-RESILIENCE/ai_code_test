def string_sequence(n: int) -> str:
    """
    Generates a space-delimited string of numbers from 0 to n inclusive.
    
    Args:
        n: The upper bound of the sequence (inclusive).
    
    Returns:
        A string containing numbers from 0 to n separated by spaces.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    # Generate the sequence using a list comprehension and join with spaces
    return ' '.join(str(i) for i in range(n + 1))