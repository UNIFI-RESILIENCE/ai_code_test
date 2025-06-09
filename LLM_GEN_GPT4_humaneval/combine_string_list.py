from typing import List

def concatenate(strings: List[str]) -> str:
    # Join all strings in the list into a single string
    return ''.join(strings)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    # Test with an empty list
    assert candidate([]) == ''
    # Test with a three-element list
    assert candidate(['x', 'y', 'z']) == 'xyz'
    # Test with a five-element list
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'