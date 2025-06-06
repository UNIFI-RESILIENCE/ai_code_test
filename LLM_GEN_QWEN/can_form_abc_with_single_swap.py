# Function to determine if the string can be transformed to "abc" with at most one swap
def can_transform_to_abc(s):
    target = "abc"
    if s == target:
        return "YES"
    
    mismatch_count = 0
    mismatch_indices = []
    
    # Find the indices where the current string differs from the target string "abc"
    for i in range(3):
        if s[i] != target[i]:
            mismatch_count += 1
            mismatch_indices.append(i)
    
    # Check the number of mismatches
    if mismatch_count == 2:
        # Swap the two mismatched characters and check if the resulting string is "abc"
        i, j = mismatch_indices
        swapped_string = list(s)
        swapped_string[i], swapped_string[j] = swapped_string[j], swapped_string[i]
        swapped_string = ''.join(swapped_string)
        return "YES" if swapped_string == target else "NO"
    else:
        return "NO"

# Read input
import sys
input = sys.stdin.read().strip().split('\n')

# Number of test cases
t = int(input[0])

# Process each test case
results = []
for case in range(1, t + 1):
    s = input[case].strip()
    results.append(can_transform_to_abc(s))

# Print all results
for result in results:
    print(result)