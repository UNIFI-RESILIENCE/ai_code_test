def decode_cyclic(s: str):
    """
    Decodes a string that was encoded with encode_cyclic.
    The encoding process cyclically shifted each 3-character group left by 1.
    This decoding reverses that operation by shifting each 3-character group right by 1.
    """
    # Split the string into groups of 3 characters each
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cyclic shift for each complete group (length 3)
    decoded_groups = [
        (group[-1] + group[:-1]) if len(group) == 3 else group
        for group in groups
    ]
    
    return "".join(decoded_groups)