def longest_semi_repetitive_substring(s):
    # Initialize variables
    n = len(s)
    max_length = 1  # At least each character itself is a semi-repetitive substring of length 1
    left = 0  # Left pointer for the sliding window
    last_pair_index = -1  # To keep track of the index of the last repeated pair

    # Iterate through the string with a right pointer
    for right in range(1, n):
        # Check if we encounter a consecutive pair of the same digit
        if s[right] == s[right - 1]:
            # Update the left boundary to the index after the previous pair
            left = last_pair_index + 1
            # Update the last pair index to the current one
            last_pair_index = right
        
        # Calculate the length of the current semi-repetitive substring
        current_length = right - left + 1
        # Update the maximum length found so far
        max_length = max(max_length, current_length)

    return max_length

# Test cases
print(longest_semi_repetitive_substring("52233"))  # Output: 4
print(longest_semi_repetitive_substring("5494"))   # Output: 4
print(longest_semi_repetitive_substring("1111111")) # Output: 2