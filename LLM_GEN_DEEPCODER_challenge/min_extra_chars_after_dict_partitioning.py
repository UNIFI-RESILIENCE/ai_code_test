def min_extra_char(s: str, dictionary: list[str]) -> int:
    n = len(s)
    # Convert dictionary to a set for O(1) lookups
    word_set = set(dictionary)
    # dp[i] represents the min extra chars up to the i-th character (0-indexed)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Initialize by considering current character as extra
        dp[i] = dp[i - 1] + 1
        
        # Check all possible substrings ending at current position
        for j in range(i - 1, -1, -1):
            substring = s[j:i]
            if substring in word_set:
                dp[i] = min(dp[i], dp[j])
                
    return dp[n]

# Example usage:
# print(min_extra_char("leetscode", ["leet","code","leetcode"]))  # Output: 1
# print(min_extra_char("sayhelloworld", ["hello","world"]))      # Output: 3