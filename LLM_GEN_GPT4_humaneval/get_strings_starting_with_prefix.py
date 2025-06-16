from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    # Return a list of strings from the input that start with the specified prefix
    return [s for s in strings if s.startswith(prefix)]

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    # Test with empty list and prefix
    assert candidate([], 'john') == []
    # Test with a mix of matching and non-matching prefixes
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']