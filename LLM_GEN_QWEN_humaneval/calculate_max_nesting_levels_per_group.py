from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize a list to store the maximum depth for each group
    max_depths = []
    
    # Iterate over each group of parentheses
    for group in groups:
        current_depth = 0  # Current depth of nested parentheses
        max_depth = 0      # Maximum depth encountered in this group
        
        # Iterate over each character in the group
        for char in group:
            if char == '(':
                # Increase the current depth when encountering an opening parenthesis
                current_depth += 1
                # Update the maximum depth if the current one is greater
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Decrease the current depth when encountering a closing parenthesis
                current_depth -= 1
        
        # Append the maximum depth of this group to the result list
        max_depths.append(max_depth)
    
    return max_depths

# Metadata dictionary (not used in the function but kept as per the prompt)
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the implementation
def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3], "Test case 1 failed"
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4], "Test case 2 failed"
    assert candidate('(()(())((())))') == [4], "Test case 3 failed"

# Running the check function to validate the solution
check(parse_nested_parens)