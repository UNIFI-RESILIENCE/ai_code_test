def separate_paren_groups(paren_string: str) -> List[str]:
    # Initialize an empty list to store the resulting groups of parentheses
    groups = []
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Initialize an empty string to build the current group of parentheses
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # Ignore spaces in the input string
        if char == " ":
            continue
        
        # Add the character to the current group
        current_group += char
        
        # Adjust the balance counter
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        
        # If balance is zero, we have a complete group of balanced parentheses
        if balance == 0:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group for the next potential group
            current_group = ""
    
    # Return the list of separated groups of balanced parentheses
    return groups