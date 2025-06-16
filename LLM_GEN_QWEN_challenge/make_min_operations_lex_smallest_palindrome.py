def make_palindrome(s: str) -> str:
    # Convert the string to a list of characters to allow in-place modifications
    s_list = list(s)
    # Initialize two pointers: one at the start and one at the end of the string
    left = 0
    right = len(s) - 1
    
    # Loop until the two pointers meet in the middle
    while left < right:
        # If the characters at the two pointers are not the same,
        # replace the larger character with the smaller one to achieve
        # the lexicographically smallest palindrome
        if s_list[left] < s_list[right]:
            s_list[right] = s_list[left]
        elif s_list[left] > s_list[right]:
            s_list[left] = s_list[right]
        # Move the pointers towards the center
        left += 1
        right -= 1
    
    # Convert the list of characters back to a string and return it
    return ''.join(s_list)