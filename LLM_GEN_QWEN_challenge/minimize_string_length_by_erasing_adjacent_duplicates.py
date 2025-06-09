def minimizedStringLength(s):
    # Use a set to store unique characters from the string
    unique_characters = set(s)
    
    # The length of the set gives the number of unique characters
    minimized_length = len(unique_characters)
    
    return minimized_length

# Example usage:
s1 = "aaabc"
s2 = "cbbd"
s3 = "dddaaa"

print(minimizedStringLength(s1))  # Output: 3
print(minimizedStringLength(s2))  # Output: 3
print(minimizedStringLength(s3))  # Output: 2