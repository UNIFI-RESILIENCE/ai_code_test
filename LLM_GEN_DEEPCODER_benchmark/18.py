def how_many_times(string: str, substring: str) -> int:
    """Find how many times a substring appears in a string, including overlapping cases.
    
    Args:
        string: The original string to search in.
        substring: The substring to count occurrences of.
        
    Returns:
        int: The number of occurrences of the substring, including overlaps.
    """
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    
    # Edge case: if substring is empty or longer than the string, return 0
    if sub_len == 0 or sub_len > str_len:
        return 0
    
    # Slide through the string and check for substring matches
    for i in range(str_len - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
            
    return count