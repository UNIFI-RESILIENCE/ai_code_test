from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenates a list of strings into a single string.
    
    Args:
        strings: A list of strings to be concatenated.
        
    Returns:
        The concatenated string. Returns an empty string if the input list is empty.
        
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'xyz'
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'