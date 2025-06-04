Here's the optimum code that achieves the desired functionality of splitting a string of parentheses into balanced, non-nested groups, while ignoring any spaces:

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current = ''
    balance = 0
    for ch in paren_string:
        if ch == ' ':
            continue
        current += ch
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        if balance == 0 and current:
            result.append(current)
            current = ''
    return result

This function builds segments of parentheses, keeping track of the balance between opening and closing parentheses using a counter. When the balance returns to zero, a complete group is found and added to the result list.