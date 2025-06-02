def longest_substring_without_repeating_characters(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index_map:
            # Move the start to the right of the last occurrence of s[end]
            start = max(start, char_index_map[s[end]] + 1)

        # Update the last seen index of the current character
        char_index_map[s[end]] = end

        # Update the maximum length found
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
s = "abcabcbb"
print(longest_substring_without_repeating_characters(s))  # Output: 3