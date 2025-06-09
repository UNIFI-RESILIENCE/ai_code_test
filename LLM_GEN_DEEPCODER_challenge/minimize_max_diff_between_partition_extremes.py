def min_partition_value(nums):
    """
    Calculate the minimum partition value given the constraints.

    The approach involves sorting the array and checking adjacent partitions,
    as the optimal partition will lie between two adjacent elements when ordered.
    This reduces the problem to comparing differences between adjacent elements
    after sorting, leading to O(n log n) time complexity.

    Args:
        nums: list of integers to be partitioned.

    Returns:
        The minimum value of the partition.
    """
    nums_sorted = sorted(nums)
    min_value = float('inf')
    n = len(nums_sorted)
    
    # The optimal partitions are either:
    # 1. Splitting after the first k elements (1 <= k < n)
    #    Then, |max(nums1) - min(nums2)| becomes |nums_sorted[k-1] - nums_sorted[k]|
    # To find the minimal difference, we find the minimal adjacent difference.
    for i in range(1, n):
        current_diff = nums_sorted[i] - nums_sorted[i-1]
        if current_diff < min_value:
            min_value = current_diff
        # Early exit if diff is 0 (minimum possible)
        if min_value == 0:
            return 0
    
    return min_value