def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups of up to three characters.
    groups = [s[3 * i: min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group of exactly three characters.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join all groups back into a single string.
    return "".join(groups)


def decode_cyclic(s: str):
    # Split string into groups of up to three characters.
    groups = [s[3 * i: min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cyclic rotation for each group of exactly three characters.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    # Join all groups back into a single string to form the decoded output.
    return "".join(groups)