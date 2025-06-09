from typing import List

def min_partition_value(nums: List[int]) -> int:
    # Sort the array so we can evaluate adjacent elements for optimal partition
    nums.sort()

    # Initialize the minimum value as infinity
    min_value = float('inf')

    # Iterate through the array to compute differences between adjacent elements.
    # This will help in finding the minimal possible value of |max(nums1) - min(nums2)|
    for i in range(1, len(nums)):
        # The maximum of nums1 would be nums[i - 1]
        # The minimum of nums2 would be nums[i]
        partition_value = abs(nums[i] - nums[i - 1])

        # Update min_value if the current partition has a smaller difference
        min_value = min(min_value, partition_value)

    return min_value