def how_many_times(string: str, substring: str) -> int:
    # Return 0 immediately if substring is empty to avoid infinite loop
    if not substring:
        return 0

    count = 0
    index = 0

    # Iterate over string and find overlapping occurrences of substring
    while index <= len(string) - len(substring):
        if string[index:index + len(substring)] == substring:
            count += 1
        index += 1  # Move forward by one character to allow overlapping matches

    return count


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}