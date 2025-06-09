from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs a bitwise XOR operation between two binary strings and returns the result.
    
    Args:
        a: First binary string consisting of '0's and '1's.
        b: Second binary string consisting of '0's and '1's.
        
    Returns:
        The resulting binary string after performing XOR operation bit by bit.
        
    Raises:
        ValueError: If input strings have different lengths or contain invalid characters.
    """
    # Check if input strings are of equal length
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    
    # Initialize an empty result string
    result = []
    
    # Iterate over each pair of bits from a and b
    for bit_a, bit_b in zip(a, b):
        # Validate that the characters are '0' or '1'
        if bit_a not in {'0', '1'} or bit_b not in {'0', '1'}:
            raise ValueError("Input strings must contain only '0's and '1's")
        
        # Perform XOR operation and append to result
        xor_bit = '1' if bit_a != bit_b else '0'
        result.append(xor_bit)
    
    return ''.join(result)