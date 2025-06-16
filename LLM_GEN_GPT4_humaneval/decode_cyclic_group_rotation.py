def decode_cyclic(s: str):
    # Split the input string into groups of 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Reverse the encoding by rotating each group of 3 characters one position to the left
    # For groups with fewer than 3 characters, leave them unchanged
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]

    # Join all groups into the final decoded string
    return "".join(groups)