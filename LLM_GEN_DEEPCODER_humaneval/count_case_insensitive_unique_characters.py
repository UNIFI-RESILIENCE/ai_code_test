def count_distinct_characters(string: str) -> int:
    """
    Counts the number of distinct characters in a string, case-insensitive.
    
    Args:
        string: The input string to analyze.
    
    Returns:
        The number of distinct characters, ignoring case differences.
        
    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to make the comparison case-insensitive
    # Then create a set of characters, which automatically handles uniqueness
    # The length of this set gives the count of distinct characters
    return len({char.lower() for char in string})