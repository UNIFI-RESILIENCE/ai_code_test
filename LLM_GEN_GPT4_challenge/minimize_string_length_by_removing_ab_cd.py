def min_length(s: str) -> int:
    stack = []

    for char in s:
        # Check if the current character and the last character in stack form "AB" or "CD"
        if stack:
            last_char = stack[-1]
            if (last_char == 'A' and char == 'B') or (last_char == 'C' and char == 'D'):
                # Remove the last character as this pair gets removed
                stack.pop()
                continue
        # If no pair is formed, push current character to the stack
        stack.append(char)

    # The minimum length is the size of the stack after processing
    return len(stack)