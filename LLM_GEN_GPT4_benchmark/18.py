def how_many_times(string: str, substring: str) -> int:
    # Return 0 immediately if substring is empty to avoid infinite loop or invalid match
    if not substring:
        return 0

    count = 0
    index = 0

    # Loop through the string and search for the substring starting at each index
    while index <= len(string) - len(substring):
        # If the substring matches at current index, increment count
        if string[index:index + len(substring)] == substring:
            count += 1
        # Move forward by one character to allow overlapping matches
        index += 1

    return count