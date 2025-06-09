from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs a bitwise XOR operation on two binary strings (consisting of '0's and '1's) of the same length.
    Returns the result as a binary string.
    
    Args:
        a: First binary string.
        b: Second binary string.
    
    Returns:
        The result of the XOR operation as a binary string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Ensure the input strings are of the same length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length")
    
    result = []
    for bit_a, bit_b in zip(a, b):
        # XOR operation: 1 if bits are different, 0 otherwise
        xor_bit = '1' if bit_a != bit_b else '0'
        result.append(xor_bit)
    
    return ''.join(result)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'