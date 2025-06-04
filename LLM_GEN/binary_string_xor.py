Here is the optimum implementation for the string_xor function:

from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    """
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

This solution uses a generator expression with zip to pair elements from both strings and applies binary XOR logic: result is '1' if the bits differ, else '0'. It is concise and efficient.