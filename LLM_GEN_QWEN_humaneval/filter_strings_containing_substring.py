from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    # Use a list comprehension to filter strings containing the specified substring
    return [s for s in strings if substring in s]


# Metadata about the author and dataset
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


# Function to check the correctness of the filter_by_substring function
def check(candidate):
    # Test with an empty list and a random substring
    assert candidate([], 'john') == [], "Test with an empty list failed."

    # Test with multiple occurrences of the substring 'xxx'
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx'], \
        "Test with multiple occurrences of 'xxx' failed."

    # Test with overlapping substring 'xx'
    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx'], \
        "Test with overlapping occurrences of 'xx' failed."

    # Test with a different substring 'run'
    assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune'], \
        "Test with 'run' substring failed."