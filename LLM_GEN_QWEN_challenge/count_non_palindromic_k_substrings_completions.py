MOD = 998244353

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def count_good_strings(N, K, S):
    # Count the number of '?' in the string
    q = S.count('?')
    
    # Generate all possible strings by replacing '?' with 'A' or 'B'
    def generate_strings(S, pos=0, current=""):
        if pos == N:
            return [current]
        if S[pos] == '?':
            # Replace '?' with 'A' or 'B'
            return (generate_strings(S, pos + 1, current + 'A') +
                    generate_strings(S, pos + 1, current + 'B'))
        else:
            return generate_strings(S, pos + 1, current + S[pos])
    
    # Generate all possible strings
    all_strings = generate_strings(S)
    
    # Count good strings
    good_string_count = 0
    
    for candidate in all_strings:
        valid = True
        # Check for each substring of length K
        for i in range(N - K + 1):
            if is_palindrome(candidate[i:i + K]):
                valid = False
                break
        if valid:
            good_string_count += 1
            good_string_count %= MOD
    
    return good_string_count

# Read input
N, K = map(int, input().split())
S = input().strip()

# Calculate and print the number of good strings
result = count_good_strings(N, K, S)
print(result)