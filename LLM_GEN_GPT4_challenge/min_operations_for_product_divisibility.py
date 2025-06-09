from sys import stdin, stdout
import math
from collections import defaultdict

# Precompute smallest prime factors for numbers up to 10
# since ai ∈ [1, 10], this will be efficient enough
def prime_factors(x):
    factors = defaultdict(int)
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors[d] += 1
            x //= d
        d += 1
    if x > 1:
        factors[x] += 1
    return factors

# Compute the minimum operations required to make the product divisible by k
def min_operations(n, k, a):
    # Get prime factorization of k
    k_factors = prime_factors(k)

    # Current exponent count of each prime in the entire array's product
    curr_factors = defaultdict(int)
    for num in a:
        pf = prime_factors(num)
        for p, count in pf.items():
            curr_factors[p] += count

    # Check if already divisible
    met = True
    for p, req_count in k_factors.items():
        if curr_factors[p] < req_count:
            met = False
            break
    if met:
        return 0

    # Try incrementing each ai to ai + x until the deficiency is fixed
    # Brute force each ai, try increasing it up to a reasonable limit
    # Since ai is at most 10, and range of x is small, performance is acceptable
    min_ops = float('inf')
    for i in range(n):
        needed = defaultdict(int)
        for p, req_count in k_factors.items():
            needed[p] = max(0, req_count - curr_factors[p])

        # From ai to ai+30 or until all requirements are met
        cnt = 0
        local_pf = prime_factors(a[i])
        # Remove original contribution of a[i]
        for p, val in local_pf.items():
            curr_factors[p] -= val

        for x in range(31):
            new_val = a[i] + x
            pf = prime_factors(new_val)

            ok = True
            # Sum all factors again
            for p, req_count in k_factors.items():
                total = curr_factors[p] + pf[p]
                if total < req_count:
                    ok = False
                    break
            if ok:
                min_ops = min(min_ops, x)
                break
        # Restore back original value
        for p, val in local_pf.items():
            curr_factors[p] += val

    return min_ops

# Read input
t = int(stdin.readline())
results = []

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    results.append(str(min_operations(n, k, a)))

# Write all results
stdout.write('\n'.join(results) + '\n')