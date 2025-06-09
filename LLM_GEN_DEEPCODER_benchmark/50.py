def decode_shift(s: str):
    """
    Decodes a string that was encoded by shifting every character by 5 positions in the alphabet.
    The decoding is done by shifting each character back by 5 positions.
    
    Args:
        s: String to be decoded (previously encoded with encode_shift)
        
    Returns:
        The decoded string with characters shifted back by 5 positions in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])