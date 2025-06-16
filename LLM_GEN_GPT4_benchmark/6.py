from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the input string by whitespace to process each group individually
    groups = paren_string.strip().split()

    # This list will store the maximum nesting level for each group
    result = []

    # Iterate over each group of parentheses
    for group in groups:
        max_depth = 0   # Tracks the deepest level for the current group
        current_depth = 0  # Tracks the current nesting level

        # Iterate through each character in the group
        for char in group:
            if char == '(':
                # Opening parenthesis increases current depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Closing parenthesis decreases current depth
                current_depth -= 1

        # Append the maximum depth encountered for this group
        result.append(max_depth)

    return result