def make_smallest_palindrome(s: str) -> str:
    # Convert the input string to a list for easier manipulation
    chars = list(s)
    n = len(chars)

    # Iterate from both ends toward the center
    for i in range(n // 2):
        j = n - 1 - i
        if chars[i] != chars[j]:
            # If characters differ, choose the lexicographically smaller one
            smaller_char = min(chars[i], chars[j])
            chars[i] = chars[j] = smaller_char

    # Join list of characters back to a string
    return ''.join(chars)