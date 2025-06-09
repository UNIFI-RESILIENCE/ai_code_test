def is_palindrome(string: str) -> bool:
    """Helper function to check if a string is a palindrome."""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with the supplied string.
    
    The algorithm works as follows:
    1. Find the longest palindromic suffix of the input string
    2. The minimal characters needed to form a palindrome are the reverse of the 
       remaining prefix before this palindromic suffix
    3. Append these characters to the end of the original string
    
    Args:
        string: Input string to be extended into a palindrome
        
    Returns:
        The shortest palindrome that starts with the input string
        
    Examples:
        >>> make_palindrome('')
        ''
        >>> make_palindrome('cat')
        'catac'
        >>> make_palindrome('cata')
        'catac'
    """
    if not string:
        return string
    
    # Find the largest index where string[:end] is a palindrome
    for end in range(len(string), -1, -1):
        if is_palindrome(string[:end]):
            # The characters to append are the reverse of the remaining prefix
            return string + string[end:][::-1]
    
    return string  # should never reach here for non-empty strings