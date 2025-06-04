Here's the optimum implementation for the filter_by_prefix function:

from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

This code efficiently filters the list using list comprehension and the str.startswith method.