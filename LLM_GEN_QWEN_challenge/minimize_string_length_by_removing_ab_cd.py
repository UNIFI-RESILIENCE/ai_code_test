def min_length(s):
    # Initialize an empty stack to use for matching AB and CD substrings
    stack = []

    # Iterate through each character in the string
    for char in s:
        # Check if the current character with the top of the stack forms "AB" or "CD"
        if stack and ((stack[-1] == "A" and char == "B") or (stack[-1] == "C" and char == "D")):
            # If it does, pop the top of the stack (remove the matched substring part)
            stack.pop()
        else:
            # Otherwise, push the current character onto the stack
            stack.append(char)

    # The length of the stack is the minimum possible length of the resulting string
    return len(stack)

# Example usage:
# print(min_length("ABFCACDB"))  # Output: 2
# print(min_length("ACBBD"))     # Output: 5