def find_lex_smallest_string(s):
    """
    Finds the lexicographically smallest string by performing exactly one operation:
    selecting a substring and decrementing each character by one (with 'a' becoming 'z').
    
    Args:
    s (str): Input string consisting of lowercase English letters.
    
    Returns:
    str: The lexicographically smallest string after one operation.
    """
    n = len(s)
    s_list = list(s)
    
    # Find the first position where the character is not 'a'
    for i in range(n):
        if s_list[i] != 'a':
            # Apply the operation from i onwards until the next 'a' or end of string
            j = i
            while j < n and s_list[j] != 'a':
                s_list[j] = chr(ord(s_list[j]) - 1)
                j += 1
            return ''.join(s_list)
    
    # If all characters are 'a', turn the last one to 'z'
    if all(c == 'a' for c in s_list):
        s_list[-1] = 'z'
        return ''.join(s_list)
    
    return ''.join(s_list)