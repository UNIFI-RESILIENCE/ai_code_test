def remove_trailing_zeros(num: str) -> str:
    """
    Removes trailing zeros from the string representation of a number.
    
    Args:
        num: A string representing a positive integer with no leading zeros.
    
    Returns:
        The string representation of the number with trailing zeros removed.
    """
    # Iterate from the end of the string to find the first non-zero digit
    end = len(num) - 1
    while end >= 0 and num[end] == '0':
        end -= 1
    
    # Return the substring up to the first non-zero digit from the end
    return num[:end + 1]