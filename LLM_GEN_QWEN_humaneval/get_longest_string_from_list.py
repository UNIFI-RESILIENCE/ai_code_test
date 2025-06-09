from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    # Check if the input list is empty. If it is, return None.
    if not strings:
        return None
    
    # Initialize the longest string as the first element in the list.
    longest_string = strings[0]
    
    # Iterate over the list starting from the second element.
    for string in strings[1:]:
        # If the current string is longer than the longest string found so far,
        # update the longest string.
        if len(string) > len(longest_string):
            longest_string = string
    
    # Return the longest string found.
    return longest_string

# Metadata about the author and dataset (not directly used in the function, but provided for context).
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Test cases to verify the correctness of the function.
def check(candidate):
    # Test case 1: An empty list should return None.
    assert candidate([]) == None
    
    # Test case 2: A list with strings of equal length should return the first one.
    assert candidate(['x', 'y', 'z']) == 'x'
    
    # Test case 3: A list with varying lengths should return the first longest string.
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'