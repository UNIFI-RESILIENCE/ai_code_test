def smallest_string(s):
    # Convert the string to a list for easier manipulation
    chars = list(s)
    n = len(chars)
    
    # Initialize a flag to check if we've found the non-'a' substring
    found_non_a = False
    
    # Iterate over the characters in the string
    for i in range(n):
        # If the character is 'a' and we haven't found a non-'a' substring yet, continue
        if chars[i] == 'a':
            if found_non_a:
                break
            else:
                continue
        
        # If the character is not 'a' and we haven't found a non-'a' substring yet,
        # mark that we've found one
        found_non_a = True
        
        # Decrement the character by converting it to the previous char in the alphabet
        chars[i] = chr(ord(chars[i]) - 1)
    
    # If no non-'a' characters were found (i.e., the string is all 'a's),
    # change the last character to 'z' to make it the smallest possible string
    if not found_non_a:
        chars[-1] = 'z'
    
    # Join the list back into a string and return it
    return ''.join(chars)

# Example usage:
print(smallest_string("cbabc"))    # Output: "baabc"
print(smallest_string("acbbc"))    # Output: "abaab"
print(smallest_string("leetcode")) # Output: "kddsbncd"