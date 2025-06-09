from collections import Counter
import sys
input = sys.stdin.read

data = input().split()
index = 0
t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    s = data[index + 2]
    index += 3

    # Count frequency of each character in s
    freq = Counter(s)

    # Count how many characters have odd frequencies
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)

    # Number of characters remaining after removing k
    remaining_length = n - k

    # For remaining characters to form a palindrome:
    # - If remaining_length is even -> odd_count must be <= 0
    # - If remaining_length is odd -> odd_count must be <= 1
    # General condition: odd_count <= remaining_length % 2 + k

    if odd_count <= remaining_length % 2 + k:
        results.append("YES")
    else:
        results.append("NO")

# Output results
print('\n'.join(results))