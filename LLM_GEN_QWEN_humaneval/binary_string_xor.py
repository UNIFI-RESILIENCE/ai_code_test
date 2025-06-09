from typing import List


def string_xor(a: str, b: str) -> str:
    # Perform binary XOR on two input strings consisting of '1's and '0's
    # Convert each character to an integer, perform XOR, and convert back to string
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    return result


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test cases to verify the correctness of the `string_xor` function
    assert candidate('111000', '101010') == '010010', "Test case 1 failed"
    assert candidate('1', '1') == '0', "Test case 2 failed"
    assert candidate('0101', '0000') == '0101', "Test case 3 failed"


# Example usage of the `check` function to validate `string_xor`
check(string_xor)