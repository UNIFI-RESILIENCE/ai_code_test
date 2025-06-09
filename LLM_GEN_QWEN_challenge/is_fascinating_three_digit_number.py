def is_fascinating(n):
    # Check if n is within the valid range
    if n < 100 or n > 999:
        return False
    
    # Calculate 2 * n and 3 * n
    n2 = 2 * n
    n3 = 3 * n
    
    # Concatenate n, 2n, and 3n into a string
    concatenated_str = str(n) + str(n2) + str(n3)
    
    # Convert string to a set to check for unique characters and length
    char_set = set(concatenated_str)
    
    # Check if the concatenated string has all digits from 1 to 9 exactly once
    return len(char_set) == 9 and '0' not in char_set and len(concatenated_str) == 9

# Example Usage:
# print(is_fascinating(192))  # Output: True
# print(is_fascinating(100))  # Output: False