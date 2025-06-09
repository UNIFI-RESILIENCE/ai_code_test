from itertools import combinations
from functools import reduce
import operator

def max_strength(nums):
    max_product = float('-inf')
    n = len(nums)

    # Iterate over all possible non-empty subsets
    for r in range(1, n + 1):
        for subset in combinations(nums, r):
            # Compute product of the current subset
            product = reduce(operator.mul, subset, 1)
            max_product = max(max_product, product)

    return max_product

# Example usage:
# Input: [3, -1, -5, 2, 5, -9]
# Output: 1350
# Explanation: Optimal group is [3, -5, 2, 5, -9] -> 3 * (-5) * 2 * 5 * (-9) = 1350
print(max_strength([3, -1, -5, 2, 5, -9]))

# Input: [-4, -5, -4]
# Output: 20
# Explanation: Optimal group is [-4, -5] -> (-4) * (-5) = 20
print(max_strength([-4, -5, -4]))