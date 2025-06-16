def decode_cyclic(s: str):
    # Split string into groups of 3 characters. The last group may be shorter.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]

    # For groups with exactly 3 characters, revert the cyclic encoding
    # During encoding, characters were rotated left: ABC -> BCA
    # To decode, rotate right: BCA -> ABC
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]

    # Join decoded groups back into a single string
    return "".join(decoded_groups)