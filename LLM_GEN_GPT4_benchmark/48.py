def is_palindrome(text: str):
    """
    Determines whether the given text is a palindrome.
    A palindrome reads the same forwards and backwards.

    Args:
        text (str): The string to evaluate.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

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
    # Compare string with its reverse
    return text == text[::-1]