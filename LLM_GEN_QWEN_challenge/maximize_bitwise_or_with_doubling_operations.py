def maximum_or(nums, k):
    # Calculate the prefix OR values for the array
    prefix_or = [0] * len(nums)
    current_prefix_or = 0
    for i in range(len(nums)):
        current_prefix_or |= nums[i]
        prefix_or[i] = current_prefix_or

    # Calculate the suffix OR values for the array
    suffix_or = [0] * len(nums)
    current_suffix_or = 0
    for i in range(len(nums) - 1, -1, -1):
        suffix_or[i] = current_suffix_or
        current_suffix_or |= nums[i]

    max_or_value = 0

    # Iterate through each number in the array
    for i in range(len(nums)):
        # Consider the scenario where the operation is applied to nums[i]
        # Temporarily store the current number multiplied by 2^k
        modified_value = nums[i] << k
        
        # Calculate the OR value if nums[i] is the only changed element
        # This is done by combining the prefix OR value of the elements before nums[i]
        # and the suffix OR value of the elements after nums[i]
        new_or_value = (prefix_or[i-1] if i > 0 else 0) | modified_value | suffix_or[i+1]
        
        # Update the maximum OR value found so far
        max_or_value = max(max_or_value, new_or_value)

    return max_or_value


# Example usage:
nums1 = [12, 9]
k1 = 1
print(maximum_or(nums1, k1))  # Output: 30

nums2 = [8, 1, 2]
k2 = 2
print(maximum_or(nums2, k2))  # Output: 35