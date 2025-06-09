from typing import List

def string_xor(a: str, b: str) -> str:
    # Perform bitwise XOR between corresponding bits of input strings 'a' and 'b'
    # Assuming both strings are of the same length and contain only '0's and '1's
    result = []
    for bit_a, bit_b in zip(a, b):
        # XOR logic: if bits are the same, result is '0'; otherwise, '1'
        result.append('0' if bit_a == bit_b else '1')
    return ''.join(result)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'