def maxOr(nums, k):
    max_or = 0
    # We'll consider each bit position from highest to lowest
    for bit in range(30, -1, -1):
        # Check if setting this bit could potentially increase the max_or
        potential_max = max_or | (1 << bit)
        temp_or = 0
        operations_needed = 0
        
        # Determine if we can achieve this potential_max with <= k operations
        # We'll try to set this bit in as many numbers as possible
        for num in nums:
            # If the current number doesn't have this bit set, check if we can set it
            if (num & potential_max) < (1 << bit):
                # Calculate how many operations are needed to set this bit
                required_ops = 0
                current_num = num
                while (current_num & (1 << bit)) == 0 and required_ops <= k:
                    current_num <<= 1
                    required_ops += 1
                if required_ops <= k:
                    operations_needed += required_ops
                    if operations_needed > k:
                        break
                    temp_or |= current_num
                else:
                    temp_or |= num
            else:
                temp_or |= num
        
        if operations_needed <= k:
            max_or = potential_max
    
    # Now reconstruct the actual maximum OR by applying the best possible operations
    # We need to find which elements to multiply to maximize the OR
    # Since k is small (<=15), we can use dynamic programming or greedy approach
    
    # Greedy approach: multiply the element that gives the highest gain each time
    from heapq import heappush, heappop
    heap = []
    original_or = 0
    for num in nums:
        original_or |= num
    
    # We'll track the current OR and the best elements to multiply
    current_or = original_or
    # We can multiply any element up to k times, but optimally we should multiply the same element all k times
    # or distribute among a few elements
    
    # The optimal strategy is to apply all k operations to a single element
    # So we try each element, apply all k operations, and compute the OR
    max_possible = current_or
    for i in range(len(nums)):
        temp_num = nums[i]
        for _ in range(k):
            temp_num <<= 1
        temp_or = original_or | temp_num
        if temp_or > max_possible:
            max_possible = temp_or
    
    return max_possible