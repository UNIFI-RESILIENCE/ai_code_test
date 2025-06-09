import sys
from collections import defaultdict

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        m = n - k  # remaining characters after removing k
        
        if m == 0:
            print("YES")
            continue
        
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        # Calculate number of pairs and odd counts
        pairs = 0
        odd = 0
        for char in freq:
            pairs += freq[char] // 2
            odd += freq[char] % 2
        
        max_pairs_possible = pairs
        min_odd_required = 1 if m % 2 != 0 else 0
        
        # Each palindrome needs at least (m // 2) pairs (for half the string)
        needed_pairs = m // 2
        if max_pairs_possible >= needed_pairs:
            # The remaining characters after using needed_pairs is (2 * needed_pairs) + we may have 1 odd (if m is odd)
            # So available_odd = odd + 2*(max_pairs_possible - needed_pairs)
            available_odd = odd + 2 * (max_pairs_possible - needed_pairs)
            if available_odd >= min_odd_required:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")

solve()