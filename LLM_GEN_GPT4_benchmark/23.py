def strlen(string: str) -> int:
    # Initialize a counter to zero
    length = 0

    # Iterate through each character in the string
    for _ in string:
        # Increment the counter for each character
        length += 1

    # Return the final count as the length of the string
    return length