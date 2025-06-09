def is_palindrome(text: str) -> bool:
    """
    Determines if the input string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text: The string to be checked
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('hello')
        False
    """
    # Clean the string by removing case sensitivity (optional depending on requirements)
    cleaned = text.lower()
    
    # Compare the string with its reverse
    return cleaned == cleaned[::-1]