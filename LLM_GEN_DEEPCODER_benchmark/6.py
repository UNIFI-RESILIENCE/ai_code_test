from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parses a string of nested parenthesis groups and returns the maximum nesting depth for each group.
    
    Args:
        paren_string: A string containing multiple parenthesis groups separated by spaces.
        
    Returns:
        A list of integers representing the maximum nesting depth for each parenthesis group.
    """
    result = []
    current_max = 0
    current_depth = 0
    
    for char in paren_string:
        if char == '(':
            current_depth += 1
            current_max = max(current_max, current_depth)
        elif char == ')':
            current_depth -= 1
        elif char == ' ':
            # End of current group, store the max depth and reset counters
            result.append(current_max)
            current_max = 0
            current_depth = 0
    
    # Add the last group's max depth (if the string doesn't end with space)
    if current_max != 0 or (paren_string and paren_string[-1] == ')'):
        result.append(current_max)
        
    return result