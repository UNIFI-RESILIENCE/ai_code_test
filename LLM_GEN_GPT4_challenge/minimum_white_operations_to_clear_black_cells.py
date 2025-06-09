from sys import stdin, stdout

# Function to compute the minimum number of operations needed
def min_operations_to_remove_black(n, k, s):
    operations = 0
    i = 0
    s = list(s)  # Convert string to list for in-place modification
    
    while i <= n - k:
        if s[i] == 'B':
            # Perform an operation: make k consecutive cells white starting from position i
            for j in range(i, i + k):
                s[j] = 'W'
            operations += 1
        i += 1

    # After processing up to n - k, check if any 'B' is left in the tail
    for j in range(n - k + 1, n):
        if s[j] == 'B':
            operations += 1
            break  # Just one extra operation at worst required to convert the last segment

    return operations

# Read input efficiently
t = int(stdin.readline())
results = []

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    s = stdin.readline().strip()
    results.append(str(min_operations_to_remove_black(n, k, s)))

# Write all results at once
stdout.write("\n".join(results) + "\n")