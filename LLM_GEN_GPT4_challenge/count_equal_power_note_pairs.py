from collections import Counter
import sys
input = sys.stdin.read

# Read all inputs at once for efficiency
data = input().split()
index = 0

# Number of test cases
t = int(data[index])
index += 1

results = []

for _ in range(t):
    # Read the size of the current array
    n = int(data[index])
    index += 1

    # Read the array elements
    arr = list(map(int, data[index:index + n]))
    index += n

    # Count frequency of each exponent value a_i
    freq = Counter(arr)

    count = 0

    # Count all combinations where a_i == a_j (i < j)
    # These satisfy b_i^b_j == b_j^b_i since b_i == b_j
    for val in freq.values():
        if val >= 2:
            count += val * (val - 1) // 2

    # Since b_i = 2^a_i and b_j = 2^a_j
    # b_i^b_j = (2^a_i)^(2^a_j) = 2^(a_i * 2^a_j)
    # b_j^b_i = (2^a_j)^(2^a_i) = 2^(a_j * 2^a_i)
    # So we are looking for distinct pairs (x, y) such that:
    # x * 2^y == y * 2^x

    keys = sorted(freq.keys())
    seen = set()

    for i in range(len(keys)):
        x = keys[i]
        for j in range(i + 1, len(keys)):
            y = keys[j]
            # Use tuple to cache seen comparisons
            if (x, y) in seen:
                continue
            seen.add((x, y))

            # Compare x * 2^y with y * 2^x
            left = x * (1 << y)
            right = y * (1 << x)

            if left == right:
                count += freq[x] * freq[y]

    results.append(str(count))

# Output all results
print('\n'.join(results))