from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parses a string containing multiple groups of nested parentheses and returns a list
    of maximum nesting depths for each group.
    
    Args:
        paren_string: String containing space-separated groups of parentheses.
    
    Returns:
        List of integers representing maximum nesting depth for each group.
    """
    result = []
    current_max = 0
    current_depth = 0
    
    for group in paren_string.split():
        current_max = 0
        current_depth = 0
        
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > current_max:
                    current_max = current_depth
            elif char == ')':
                current_depth -= 1
                
        result.append(current_max)
    
    return result