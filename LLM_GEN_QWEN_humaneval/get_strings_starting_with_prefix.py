from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    # Use list comprehension to filter strings that start with the given prefix
    return [s for s in strings if s.startswith(prefix)]

# Define metadata for reference
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the filter_by_prefix function
def check(candidate):
    # Test case: empty list should return an empty list
    assert candidate([], 'john') == [], "Test case with empty list failed"
    
    # Test case: list with multiple strings, some starting with 'xxx'
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx'], \
        "Test case with multiple strings, some starting with 'xxx' failed"

# Uncomment the line below to run the check function with filter_by_prefix
# check(filter_by_prefix)