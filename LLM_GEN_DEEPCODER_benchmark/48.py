def is_palindrome(text: str) -> bool:
    """
    Check if the input string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text: Input string to be checked
    
    Returns:
        bool: True if palindrome, False otherwise
    
    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    # Clean the string by removing case sensitivity (convert to lowercase)
    cleaned_text = text.lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]