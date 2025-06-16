def longestSemiRepetitiveSubstring(s):
    max_len = 0           # Stores the maximum length found
    start = 0             # Start index of current substring
    repeat_count = 0      # Number of consecutive repeated digits

    for end in range(len(s)):
        # If current and previous characters are the same
        if end > 0 and s[end] == s[end - 1]:
            repeat_count += 1

        # If there is more than one repeated pair, shrink window
        while repeat_count > 1:
            if s[start] == s[start + 1]:
                repeat_count -= 1
            start += 1

        # Update maximum length
        max_len = max(max_len, end - start + 1)

    return max_len