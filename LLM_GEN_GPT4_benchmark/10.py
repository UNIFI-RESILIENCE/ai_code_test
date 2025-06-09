def make_palindrome(string: str) -> str:
    # If the input string is empty or already a palindrome, return it as is
    if not string or string == string[::-1]:
        return string

    # Iterate through the string to find the longest palindromic suffix
    for i in range(len(string)):
        # Check if substring starting at i to end is a palindrome
        if string[i:] == string[i:][::-1]:
            # Found palindromic suffix: string[i:]
            # The prefix before it is string[:i], which needs to be reversed and appended
            suffix_to_add = string[:i][::-1]
            return string + suffix_to_add

    # Fallback (shouldn't reach here as whole string reversed always works)
    return string + string[::-1}