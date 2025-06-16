import sys
from collections import defaultdict

# Read the input
input = sys.stdin.read().strip().split()

# Initialize the index to process from
idx = 0

# Number of test cases
t = int(input[idx])

# List to store the results for each test case
results = []

# Process each test case
for _ in range(t):
    idx += 1
    n = int(input[idx])

    idx += 1

    # Extract the values for the current test case
    a = list(map(int, input[idx:idx+n]))
    idx += n

    # Dictionary to count occurrences of each value
    count = defaultdict(int)
    for val in a:
        count[val] += 1

    # Variable to keep track of pairs with equal values (a_i = a_j)
    equal_pairs = 0

    # Variable to keep track of pairs where a_i / log2(a_i) == a_j / log2(a_j)
    special_pairs = 0

    # Count pairs with a_i = a_j
    for val in count.values():
        if val > 1:
            equal_pairs += (val * (val - 1)) // 2

    # Count pairs where a_i = 2 * a_j or a_j = 2 * a_i
    for ai in a:
        # Check if ai / 2 exists in the dictionary
        if (ai > 1) and (ai // 2 in count):

            # We want a_i to be even and a_i / 2 == a_j
            if ai % 2 == 0:
                special_pairs += count[ai // 2]

        # Check if ai * 2 exists in the dictionary
        if 2 * ai in count:
            special_pairs += count[2 * ai]

    # Since we consider both ai * 2 and ai / 2, we are considering the same pairs twice.
    # So we divide the special_pairs by 2.
    special_pairs //= 2

    # Total pairs is the sum of equal_pairs and special_pairs
    total_pairs = equal_pairs + special_pairs

    # Store the result
    results.append(total_pairs)

# Print the results for all test cases
print("\n".join(map(str, results)))