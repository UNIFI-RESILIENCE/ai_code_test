import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        res = 0
        i = 0
        while i < n:
            if s[i] == 'B':
                res += 1
                i += k  # skip next k-1 cells as they are covered in this operation
            else:
                i += 1
        print(res)

solve()