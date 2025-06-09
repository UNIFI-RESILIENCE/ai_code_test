def flip_case(string: str) -> str:
    """
    Flip the case of each character in the given string.
    Lowercase characters are converted to uppercase, and uppercase to lowercase.
    
    Args:
        string (str): The input string to be processed.
    
    Returns:
        str: The resulting string with flipped cases.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
        >>> flip_case('Python!')
        'pYTHON!'
    """
    flipped_string = []
    for char in string:
        if char.isupper():
            flipped_string.append(char.lower())
        elif char.islower():
            flipped_string.append(char.upper())
        else:
            flipped_string.append(char)
    return ''.join(flipped_string)