import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    H = list(map(int, input[ptr:ptr+N]))
    
    res = []
    max_so_far = 0
    total = 0
    for i in range(1, N+1):
        current_h = H[i-1]
        if current_h > max_so_far:
            max_so_far = current_h
        total += max_so_far
        res.append(str(total + i))
    print(' '.join(res))

solve()