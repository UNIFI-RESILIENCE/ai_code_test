from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the input string by spaces to get individual groups of parentheses
    groups = paren_string.split()
    
    # Initialize a list to store the maximum depth of each group
    max_depths = []
    
    # Iterate over each group to determine its maximum depth
    for group in groups:
        current_depth = 0  # Current depth of nested parentheses
        max_depth = 0      # Maximum depth encountered in this group
        
        # Iterate over each character in the group
        for char in group:
            if char == '(':
                # Increase the current depth for an opening parenthesis
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Decrease the current depth for a closing parenthesis
                current_depth -= 1
        
        # Append the maximum depth of this group to the result list
        max_depths.append(max_depth)
    
    # Return the list of maximum depths for each group
    return max_depths