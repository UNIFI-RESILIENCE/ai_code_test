Here's the optimum implementation for the how_many_times function that counts overlapping occurrences of a substring in a string:

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases. """
    count = 0
    i = 0
    while i <= len(string) - len(substring):
        if string[i:i+len(substring)] == substring:
            count += 1
        i += 1
    return count

This code uses a sliding window approach to check for the substring at every position, allowing it to count overlapping occurrences correctly.