def min_operations(test_cases):
    results = []
    for n, k, s in test_cases:
        operations = 0
        # Convert the string to a list for ease of manipulation
        s_list = list(s)
        for i in range(n):
            if s_list[i] == 'B':
                # We need to perform an operation starting at index i
                operations += 1
                # Flip the next k cells to 'W'
                for j in range(i, min(i + k, n)):
                    s_list[j] = 'W'
        results.append(operations)
    return results

# Read input
import sys
import io
# Simulating the input reading from stdin
input_data = """8
6 3
WBWWWB
7 3
WWBWBWW
5 4
BWBWB
5 5
BBBBB
8 2
BWBWBBBB
10 2
WBBWBBWBBW
4 1
BBBB
3 2
WWW"""

# Use io.StringIO to simulate stdin
sys.stdin = io.StringIO(input_data)

# Read the number of test cases
t = int(input().strip())
test_cases = []
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input().strip()
    test_cases.append((n, k, s))

# Get the results
results = min_operations(test_cases)

# Output the results
for result in results:
    print(result)