from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filters a list of strings to only include those that start with the specified prefix.
    The comparison is case-sensitive and checks for exact prefix matches.

    Args:
        strings: A list of strings to be filtered.
        prefix: The prefix string to filter by.

    Returns:
        A new list containing only strings that start with the given prefix.

    Examples:
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