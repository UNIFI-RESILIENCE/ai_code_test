from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    # Return None if the input list is empty
    if not strings:
        return None
    # Use max with key=len to find the longest string
    # In case of ties, max returns the first occurrence
    return max(strings, key=len)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    # Check for empty list
    assert candidate([]) == None
    # Check when all strings have the same length
    assert candidate(['x', 'y', 'z']) == 'x'
    # Check with multiple strings and varying lengths
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'