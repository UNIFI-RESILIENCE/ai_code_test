def flip_case(string: str) -> str:
    """
    Flip the case of each character in the input string.
    Lowercase characters become uppercase, and uppercase become lowercase.
    
    Args:
        string: Input string whose characters' cases need to be flipped.
    
    Returns:
        str: The transformed string with flipped cases.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    flipped_string = []
    for char in string:
        if char.islower():
            flipped_string.append(char.upper())
        elif char.isupper():
            flipped_string.append(char.lower())
        else:
            flipped_string.append(char)  # Leave non-alphabetic characters unchanged
    return ''.join(flipped_string)