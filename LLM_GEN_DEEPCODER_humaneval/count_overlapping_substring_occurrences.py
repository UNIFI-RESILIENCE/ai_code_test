def how_many_times(string: str, substring: str) -> int:
    """
    Counts the occurrences of a substring in a string, including overlapping cases.
    
    Args:
        string: The original string to search within.
        substring: The substring to search for.
    
    Returns:
        The count of how many times the substring appears in the string.
    """
    if not substring:  # Edge case: empty substring
        return 0
    
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    
    # Slide through the string one character at a time
    for i in range(str_len - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    
    return count