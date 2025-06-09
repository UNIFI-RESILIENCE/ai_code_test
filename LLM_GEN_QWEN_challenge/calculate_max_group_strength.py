from typing import List
import itertools
import math

def maxStrength(nums: List[int]) -> int:
    # Initialize the maximum strength to a very low value
    max_strength = -math.inf
    
    # Iterate over all possible group sizes (from 1 to len(nums))
    for group_size in range(1, len(nums) + 1):
        # Generate all combinations of the current group size
        for group in itertools.combinations(nums, group_size):
            # Calculate the strength of the current group
            current_strength = math.prod(group)
            # Update the maximum strength if the current one is greater
            if current_strength > max_strength:
                max_strength = current_strength
    
    return max_strength

# Example usage:
nums1 = [3, -1, -5, 2, 5, -9]
print(maxStrength(nums1))  # Output: 1350

nums2 = [-4, -5, -4]
print(maxStrength(nums2))  # Output: 20