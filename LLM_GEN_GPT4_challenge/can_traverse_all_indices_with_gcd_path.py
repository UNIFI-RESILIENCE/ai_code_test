from collections import defaultdict
import math

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    # Find with path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by root
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px

def canTraverseAllPairs(nums):
    if len(nums) == 1:
        return True  # Only one element, trivially connected

    n = len(nums)
    max_num = max(nums)

    # Union-Find data structure for indices
    uf = UnionFind(n)

    # Map from prime factor to the list of indices that share this factor
    factor_to_indices = defaultdict(list)

    # Sieve to find smallest prime factors (SPF) for fast factorization
    spf = list(range(max_num + 1))
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if spf[i] == i:
            for j in range(i * i, max_num + 1, i):
                if spf[j] == j:
                    spf[j] = i

    # Function to get unique prime factors of a number using SPF
    def get_prime_factors(x):
        factors = set()
        while x > 1:
            factors.add(spf[x])
            x //= spf[x]
        return factors

    # Create factor to indices mapping
    for idx, num in enumerate(nums):
        prime_factors = get_prime_factors(num)
        for factor in prime_factors:
            factor_to_indices[factor].append(idx)

    # Union all indices sharing the same prime factor
    for indices in factor_to_indices.values():
        for i in range(1, len(indices)):
            uf.union(indices[0], indices[i])

    # Check if all indices belong to the same connected component
    root = uf.find(0)
    for i in range(1, n):
        if uf.find(i) != root:
            return False

    return True