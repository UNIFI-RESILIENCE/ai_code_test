def maxStrength(nums):
    """
    Calculate the maximum strength of any non-empty subset of nums, where strength is the product of all elements in the subset.
    
    Args:
        nums: List of integers representing student scores.
    
    Returns:
        Maximum product (strength) achievable by any non-empty subset of nums.
    """
    if not nums:
        return 0
    
    max_prod = min_prod = nums[0]
    result = nums[0]
    
    for num in nums[1:]:
        if num == 0:
            # Reset max and min for subarrays not including 0
            current_max = current_min = 0
        else:
            candidates = (num, max_prod * num, min_prod * num)
            current_max = max(candidates)
            current_min = min(candidates)
        
        # Update the result with the current_max encountered so far
        result = max(result, current_max)
        
        # Update max_prod and min_prod for the next iteration
        max_prod, min_prod = current_max, current_min
    
    return result