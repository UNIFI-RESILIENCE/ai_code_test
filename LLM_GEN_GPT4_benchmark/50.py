def decode_shift(s: str):
    # Shift each character in the input string back by 5 positions in the alphabet
    # Handles wrap-around using modulo operation
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])