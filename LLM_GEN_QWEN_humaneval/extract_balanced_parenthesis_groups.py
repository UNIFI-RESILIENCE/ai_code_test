from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize variables
    result = []  # To store the final groups
    balance = 0  # Counter to track the balance of parentheses
    current_group = []  # List to build the current group

    # Iterate through each character in the cleaned string
    for char in paren_string:
        current_group.append(char)  # Add character to the current group
        if char == '(':
            balance += 1  # Increase balance for an open parenthesis
        else:  # Assuming the character is ')'
            balance -= 1  # Decrease balance for a close parenthesis
        
        # A group is balanced when balance returns to zero
        if balance == 0:
            result.append(''.join(current_group))  # Join characters and add to result
            current_group.clear()  # Clear the current group for the next one

    return result  # Return the list of separated groups