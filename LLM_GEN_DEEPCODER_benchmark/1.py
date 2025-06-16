from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate balanced parentheses groups into a list of strings."""
    result = []
    current_group = []
    balance = 0
    
    for char in paren_string:
        # Ignore spaces
        if char == ' ':
            continue
        
        # Track balance and build current group
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            
            # When balance reaches 0, we've completed a group
            if balance == 0:
                result.append(''.join(current_group))
                current_group = []
    
    return result