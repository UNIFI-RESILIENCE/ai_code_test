import bisect

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N, T = int(data[idx]), int(data[idx+1])
    idx +=2
    S = data[idx]
    idx +=1
    X = list(map(int, data[idx:idx+N]))
    
    left = []
    right = []
    for i in range(N):
        if S[i] == '0':
            left.append(X[i])
        else:
            right.append(X[i])
    
    left.sort()
    right.sort()
    
    res = 0
    # For each right-moving ant, find left-moving ants that X_left > X_right - 2T
    # and X_left < X_right
    for x in right:
        # The left ants must be in (x - 2T, x)
        low = x - 2 * T
        high = x
        # Find the number of left ants in (low, high)
        l = bisect.bisect_left(left, low)
        r = bisect.bisect_left(left, high)
        res += (r - l)
    
    print(res)

solve()