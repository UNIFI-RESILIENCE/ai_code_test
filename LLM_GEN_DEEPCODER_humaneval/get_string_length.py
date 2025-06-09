def strlen(string: str) -> int:
    """
    Calculate the length of a string by counting its characters.
    
    Args:
        string: Input string whose length needs to be determined.
    
    Returns:
        Integer representing the number of characters in the string.
    """
    count = 0
    for _ in string:
        count += 1
    return count