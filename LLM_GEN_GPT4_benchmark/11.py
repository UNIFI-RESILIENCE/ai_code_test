from typing import List

def string_xor(a: str, b: str) -> str:
    # Perform bitwise XOR between two binary strings of equal length
    # Iterate through the paired characters of both strings
    # XOR logic: if bits are the same, result is '0'; if different, result is '1'
    return ''.join('0' if bit_a == bit_b else '1' for bit_a, bit_b in zip(a, b))