def make_palindrome(string: str) -> str:
    # Helper function to check if a string is a palindrome
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    # Edge case: if the string is already empty or a palindrome, return it as is
    if not string or is_palindrome(string):
        return string

    # Iterate from the end of the string towards the beginning
    for i in range(len(string)):
        # Check if the substring from the current index to the end is a palindrome
        if is_palindrome(string[i:]):
            # If it is, append the reverse of the substring from the start to the current index
            return string + string[:i][::-1]
    
    # Fallback, though logically unreachable, return the string concatenated with its full reverse
    return string + string[::-1]