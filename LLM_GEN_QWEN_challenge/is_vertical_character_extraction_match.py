# Read input strings S and T
S, T = input().split()

# Get the lengths of the strings S and T
len_S = len(S)
len_T = len(T)

# Function to check if a valid (c, w) pair exists
def find_valid_pair(S, T, len_S, len_T):
    # Iterate over all possible values of w
    for w in range(1, len_S):
        # Initialize an empty string to store the concatenated characters
        result = ""
        # Iterate over all possible starting points of substrings with width w
        for i in range(0, len_S, w):
            substring = S[i:i+w]
            # Check if the substring's length is at least c
            if len(substring) >= 1:  # Starting with c=1 since 1 <= c <= w
                for c in range(1, w + 1):  # Ensure c is less than or equal to w
                    # Append the c-th character of the substring to result
                    if len(substring) >= c:
                        result += substring[c-1]
                        # If the result matches T, return True
                        if result == T:
                            return True
        # Reset result for the next value of w
        result = ""
    # If no valid pair (c, w) is found, return False
    return False

# Determine if a valid (c, w) pair exists and print "Yes" or "No"
if find_valid_pair(S, T, len_S, len_T):
    print("Yes")
else:
    print("No")