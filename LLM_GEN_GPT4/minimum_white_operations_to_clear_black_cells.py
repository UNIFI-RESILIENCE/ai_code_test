def minimum_operations(t, test_cases):
    results = []
    for n, k, s in test_cases:
        cnt = 0
        i = 0
        s = list(s)
        while i <= n - k:
            if s[i] == 'B':
                cnt += 1
                for j in range(k):
                    s[i + j] = 'W'
                i += 1  # move forward by 1 to allow potential overlap if needed
            else:
                i += 1
        # Check for any remaining 'B's in the tail that cannot be the start of a k-group
        for i in range(n - k + 1, n):
            if s[i] == 'B':
                cnt += 1
                break  # only need one such operation
        results.append(cnt)
    return results

# Read input and run the function
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, k, s))

res = minimum_operations(t, test_cases)
for r in res:
    print(r)