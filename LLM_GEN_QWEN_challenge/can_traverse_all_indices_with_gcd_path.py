from math import gcd
from collections import defaultdict
from typing import List

def canTraverseAllPairs(nums: List[int]) -> bool:
    # Edge case: if the array has only one element, it's trivially connected
    if len(nums) == 1:
        return True
    
    # Edge case: if there's a 1 in the array, no other number can connect to it
    if 1 in nums:
        return False
    
    # Prime factorization: map each number to its prime factors
    prime_factors = {}
    
    def sieve_with_factorization(limit):
        sieve = list(range(limit + 1))
        for p in range(2, int(limit**0.5) + 1):
            if sieve[p] == p:  # p is a prime
                for multiple in range(p * p, limit + 1, p):
                    sieve[multiple] = p  # mark smallest prime factor
                
                # Collect prime factors for each number
                for num in range(p, limit + 1):
                    if sieve[num] == num:  # num is prime
                        prime_factors[num] = [num]
                    else:
                        factors = set()
                        n = num
                        while n > 1:
                            factors.add(sieve[n])
                            n //= sieve[n]
                        prime_factors[num] = factors
    
    # Find the maximum value in nums to set the limit for sieve
    max_val = max(nums)
    sieve_with_factorization(max_val)
    
    # Create a graph where each prime is a node and numbers sharing factors are connected
    factor_graph = defaultdict(set)
    for num in nums:
        for prime in prime_factors[num]:
            factor_graph[prime].add(num)
    
    # Union-Find (Disjoint Set Union) to group the numbers based on common prime factors
    parent = {num: num for num in nums}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY
    
    # Union numbers that share prime factors
    for factors in factor_graph.values():
        factors_list = list(factors)
        first_num = factors_list[0]
        for num in factors_list[1:]:
            union(first_num, num)
    
    # Check if all numbers are in the same connected component
    unique_roots = set(find(num) for num in nums)
    return len(unique_roots) == 1

# Example usage:
print(canTraverseAllPairs([2, 3, 6]))  # Output: True
print(canTraverseAllPairs([3, 9, 5]))  # Output: False
print(canTraverseAllPairs([4, 3, 12, 8]))  # Output: True