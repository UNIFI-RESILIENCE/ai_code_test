Here's the optimal implementation for the is_palindrome function based on the given description and test cases:

def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]

This function checks if the string is equal to its reverse, which is the most concise and efficient way to determine if a string is a palindrome in Python.