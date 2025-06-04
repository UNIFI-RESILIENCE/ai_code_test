Here's the complete and optimum implementation for the provided prompt:

from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    groups = paren_string.strip().split()

    for group in groups:
        max_depth = 0
        current_depth = 0
        for c in group:
            if c == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif c == ')':
                current_depth -= 1
        result.append(max_depth)

    return result

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]