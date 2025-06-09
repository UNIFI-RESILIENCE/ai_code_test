import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        freq = defaultdict(int)
        count1 = 0
        count2 = 0
        
        for num in a:
            if num == 1:
                count1 += 1
            elif num == 2:
                count2 += 1
            freq[num] += 1
        
        # Pairs where a_i = a_j: C(freq[num], 2) for all num
        res = 0
        for num in freq:
            res += freq[num] * (freq[num] - 1) // 2
        
        # Pairs where (1, 2) and (2, 1): count1 * count2
        res += count1 * count2
        print(res)

solve()