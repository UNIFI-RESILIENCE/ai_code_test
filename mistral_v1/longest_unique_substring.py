def longest_unique_substring(s: str) -> str:
    char_index_map = {}
    start = 0
    max_length = 0
    max_substring = ""

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1

        char_index_map[s[end]] = end

        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = s[start:end + 1]

    return max_substring
