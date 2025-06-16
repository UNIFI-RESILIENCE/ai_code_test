def decode_shift(s: str):
    # Decodes the input string by shifting each character 5 positions backwards in the alphabet
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])