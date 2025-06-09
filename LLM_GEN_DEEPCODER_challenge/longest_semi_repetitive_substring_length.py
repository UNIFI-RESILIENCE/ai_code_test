def longestSemiRepetitiveSubstring(s):
    max_length = 1
    n = len(s)
    
    for i in range(n):
        consecutive_pairs = 0
        for j in range(i + 1, n):
            if s[j] == s[j - 1]:
                consecutive_pairs += 1
                if consecutive_pairs > 1:
                    break
            # Update max_length if current substring is semi-repetitive
            current_length = j - i + 1
            if consecutive_pairs <= 1 and current_length > max_length:
                max_length = current_length
    return max_length