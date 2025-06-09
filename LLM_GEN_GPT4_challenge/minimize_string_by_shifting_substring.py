def lexicographically_smallest_string(s: str) -> str:
    # Convert the input string to a list for in-place modification
    s_list = list(s)
    n = len(s_list)

    # Find the first character that is not 'a'. We want to start decrementing here
    i = 0
    while i < n and s_list[i] == 'a':
        i += 1

    # If all characters are 'a', we change the last one to 'z'
    if i == n:
        s_list[-1] = 'z'
        return ''.join(s_list)

    # From the first non-'a' character, decrement characters until we hit another 'a' or the end of the string
    while i < n and s_list[i] != 'a':
        # Decrement character with wrap around using ASCII manipulation
        s_list[i] = chr(ord(s_list[i]) - 1) if s_list[i] != 'a' else 'z'
        i += 1

    return ''.join(s_list)