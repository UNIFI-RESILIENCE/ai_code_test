def minExtraChar(s, dictionary):
    N = len(s)
    # Convert the dictionary to a set for O(1) average-case lookups
    word_set = set(dictionary)

    # Memoize results to avoid redundant computations
    def dp(start):
        # If we have reached the end of the string, there are no extra characters
        if start == N:
            return 0
        
        # If the result for this starting position is already known, return it
        if memo[start] != -1:
            return memo[start]
        
        # Initially assume all characters from this position onwards are extras
        min_extra = N - start
        
        # Try to match every possible substring starting from 'start'
        for end in range(start + 1, N + 1):
            substring = s[start:end]
            
            # If this substring is in the dictionary, it's not an extra character
            if substring in word_set:
                min_extra = min(min_extra, dp(end))
            else:
                # Otherwise, count it as extra and move forward
                min_extra = min(min_extra, dp(end) + (end - start))
                
        # Store the result for this starting position in the memo table before returning
        memo[start] = min_extra
        return min_extra
    
    # Initialize our memo table
    memo = [-1] * (N + 1)
    
    # Start the dp computation from the beginning of the string
    return dp(0)

# Example usage:
s1 = "leetscode"
dictionary1 = ["leet", "code", "leetcode"]
print(minExtraChar(s1, dictionary1))  # Output: 1

s2 = "sayhelloworld"
dictionary2 = ["hello", "world"]
print(minExtraChar(s2, dictionary2))  # Output: 3