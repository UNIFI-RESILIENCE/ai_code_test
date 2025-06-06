import sys
from collections import Counter

input = sys.stdin.read
def can_form_palindrome(n, k, s):
    freq = Counter(s)
    odd_count = sum(1 for v in freq.values() if v % 2 == 1)
    # To form a palindrome, the number of odd frequency characters
    # in the remaining string (after deletion) must be <= 1
    # So we need to be able to delete at least (odd_count - 1) characters to make it possible
    # We can delete up to k characters and must leave n - k characters
    # But we must leave at least enough characters to form the palindrome
    if k > n:
        return False
    remaining_length = n - k
    max_allowed_odds = 1 if remaining_length % 2 == 1 else 0
    return odd_count <= remaining_length and odd_count <= max_allowed_odds + k

def main():
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
        result = "YES" if can_form_palindrome(n, k, s) else "NO"
        results.append(result)

    print('\n'.join(results))

main()