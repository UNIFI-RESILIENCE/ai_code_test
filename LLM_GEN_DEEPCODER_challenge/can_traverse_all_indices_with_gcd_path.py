import math
from collections import defaultdict

def canTraverseAllPairs(nums):
    if len(nums) == 1:
        return True
    
    # Union-Find (Disjoint Set Union - DSU) data structure
    parent = []
    size = []
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if size[u_root] > size[v_root]:
            parent[v_root] = u_root
            size[u_root] += size[v_root]
        else:
            parent[u_root] = v_root
            size[v_root] += size[u_root]
    
    max_num = max(nums) if nums else 0
    if max_num < 2:
        # All nums are 1, cannot form any gcd > 1
        return False
    
    # Initialize DSU
    n = len(nums)
    parent = list(range(n + max_num + 2))  # indices 0..n-1 for nodes, rest for factors
    size = [1] * (n + max_num + 2)
    
    for i in range(n):
        num = nums[i]
        if num == 1:
            # GCD with 1 is always 1, so no connections
            return False
        # Get all unique prime factors of num
        factors = set()
        x = num
        for p in range(2, int(math.isqrt(x)) + 1):
            if x % p == 0:
                factors.add(p)
                while x % p == 0:
                    x //= p
        if x > 1:
            factors.add(x)
        # Link the node to all its prime factors
        for p in factors:
            union(i, n + p)
    
    # Check if all nodes are connected via factors
    root = find(0)
    for i in range(1, n):
        if find(i) != root:
            return False
    return True