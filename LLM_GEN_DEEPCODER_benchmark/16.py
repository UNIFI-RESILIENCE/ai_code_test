def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, case-insensitive.

    Args:
        string: The input string to analyze.

    Returns:
        int: The count of distinct characters, treating uppercase and lowercase as the same.

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to handle case insensitivity
    lower_string = string.lower()
    
    # Use a set to find distinct characters (sets automatically handle uniqueness)
    distinct_chars = set(lower_string)
    
    # Return the length of the set, which gives the count of distinct characters
    return len(distinct_chars)