def minimized_string_length(s: str) -> int:
    """
    Minimizes the string length by repeatedly removing the closest left and right occurrences
    of a selected character.

    Args:
        s (str): Input string to be minimized.

    Returns:
        int: The length of the minimized string.
    """
    stack = []
    for char in s:
        # If the stack is not empty and the top of the stack is the current character,
        # it means we have a pair of adjacent duplicates that can potentially be removed.
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)