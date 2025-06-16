def decode_cyclic(s: str):
    """
    Decodes a string that was encoded using the encode_cyclic function.
    The encoding process cyclically shifts each group of three characters by one position.
    This function reverses that operation by shifting each group back to its original position.
    
    Args:
        s: The encoded string to be decoded.
        
    Returns:
        The decoded string.
    """
    # Split the string into groups of three characters each
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cyclic shift for each group of three characters
    # For groups of length 3, move the last character to the front (reverse of encoding)
    # For smaller groups, leave as-is (no shift was applied during encoding)
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    # Combine the groups back into a single string
    return "".join(groups)