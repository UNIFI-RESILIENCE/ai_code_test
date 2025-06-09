def strlen(string: str) -> int:
    # Initialize a counter to zero
    count = 0
    
    # Iterate over each character in the string
    for char in string:
        # Increment the counter for each character found
        count += 1
    
    # Return the final count which represents the length of the string
    return count