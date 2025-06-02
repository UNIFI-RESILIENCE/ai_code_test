def longest_substring_without_repeating_characters(s: str) -> str:
    # Dictionary to store the last positions of each character
    last_seen = {}
    start = 0  # Start index of the current window
    max_length = 0  # Length of the longest substring found
    max_substring = ""  # The longest substring found

    for end, char in enumerate(s):
        # If the character is already in the dictionary and it's within the current window
        if char in last_seen and last_seen[char] >= start:
            # Move the start pointer to the right of the last occurrence of the current character
            start = last_seen[char] + 1
        
        # Update the last seen position of the character
        last_seen[char] = end
        
        # Check if the current window is the longest one found so far
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = s[start:end + 1]

    return max_substring

# Example usage:
input_string = "abcabcbb"
result = longest_substring_without_repeating_characters(input_string)
print(f"The longest substring without repeating characters is: '{result}'")