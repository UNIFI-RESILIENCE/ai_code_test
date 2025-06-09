def how_many_times(string: str, substring: str) -> int:
    count = 0  # Initialize count of occurrences
    index = 0  # Start searching from the beginning of the string

    # Loop through the string to find all occurrences of the substring
    while index <= len(string) - len(substring):
        # Check if substring is found at the current index
        if string[index:index + len(substring)] == substring:
            count += 1  # Increment the count for each found occurrence
            index += 1  # Move one character forward to allow overlapping
        else:
            index += 1  # Move to the next character in the string

    return count  # Return the total count of overlapping occurrences