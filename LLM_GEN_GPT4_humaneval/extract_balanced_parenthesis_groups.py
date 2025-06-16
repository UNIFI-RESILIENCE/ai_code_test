from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove all spaces from the input to sanitize the string
    paren_string = paren_string.replace(' ', '')
    result = []         # List to store individual balanced parenthesis groups
    stack = []          # Stack to help track balance of parentheses
    current_group = []  # Current group being processed

    for char in paren_string:
        current_group.append(char)  # Append current character to the in-progress group
        if char == '(':
            stack.append(char)      # Push opening parenthesis to stack
        elif char == ')':
            stack.pop()             # Pop when matching closing parenthesis is found

        # When stack is empty, we have a complete balanced group
        if not stack:
            result.append(''.join(current_group))  # Add current group to result
            current_group = []  # Reset current group for next one

    return result  # Return list of separated balanced parenthesis groups