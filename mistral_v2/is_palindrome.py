def is_palindrome(s: str) -> bool:
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))                         # Output: True
print(is_palindrome("hello"))                          # Output: False