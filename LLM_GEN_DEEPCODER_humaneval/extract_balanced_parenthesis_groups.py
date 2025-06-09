from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separates balanced parentheses groups from the input string into a list of strings.
    Balanced groups are properly nested and closed, and not nested within each other.
    Spaces in the input are ignored.

    Args:
        paren_string: Input string containing multiple groups of nested parentheses.

    Returns:
        A list of separated balanced parentheses groups.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    groups = []
    current_group = []
    balance = 0

    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            if balance == 0:
                groups.append(''.join(current_group))
                current_group = []
    
    return groups