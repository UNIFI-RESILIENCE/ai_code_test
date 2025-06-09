from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()  # Split the input string into groups
    nesting_levels = []

    for group in groups:
        max_depth = 0  # Tracks the maximum depth for the current group
        current_depth = 0  # Tracks the current nesting level

        # Iterate through each character in the group
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)  # Update max_depth
            elif char == ')':
                current_depth -= 1  # Decrease depth when closing paren

        nesting_levels.append(max_depth)  # Record the max depth for the group

    return nesting_levels


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]