from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove all spaces as they are to be ignored
    cleaned = paren_string.replace(" ", "")
    
    groups = []                # List to hold complete balanced parentheses groups
    balance = 0                # Counter to track balance of opening and closing parentheses
    current_group = []         # Temporary list to build the current group
    
    for char in cleaned:
        current_group.append(char)
        
        # Update the balance counter
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # If balance is zero, we have a complete group
        if balance == 0 and current_group:
            groups.append(''.join(current_group))
            current_group = []  # Reset current group for the next sequence
    
    return groups