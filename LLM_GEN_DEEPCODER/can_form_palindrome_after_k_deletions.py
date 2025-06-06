import sys
from collections import defaultdict

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        m = n - k
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        total_pairs = 0
        for c in freq:
            total_pairs += freq[c] // 2
        
        max_possible_pairs = m // 2
        if total_pairs >= max_possible_pairs:
            print("YES")
        else:
            print("NO")

solve()