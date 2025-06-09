import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        
        max_diff = 0
        # Iterate all possible k (number of boxes per truck)
        # k must divide n, so it's a divisor of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            sums = []
            # Calculate sum for each truck
            for i in range(0, n, k):
                truck_sum = prefix[i + k] - prefix[i]
                sums.append(truck_sum)
            if len(sums) < 2:
                current_diff = 0
            else:
                current_diff = max(sums) - min(sums)
            if current_diff > max_diff:
                max_diff = current_diff
        print(max_diff)

solve()