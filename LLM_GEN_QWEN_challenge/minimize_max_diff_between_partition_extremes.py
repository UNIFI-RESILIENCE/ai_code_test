def min_partition(nums):
    # Step 1: Sort the input array
    nums.sort()

    # Step 2: Initialize the minimum partition value with a large number
    min_partition_value = float('inf')

    # Step 3: Iterate through the sorted array to find the minimum partition
    for i in range(len(nums) - 1):
        # Calculate the difference between adjacent elements
        current_difference = abs(nums[i] - nums[i + 1])
        
        # Update the minimum partition value if the current difference is smaller
        min_partition_value = min(min_partition_value, current_difference)

    # Step 4: Return the minimum partition value
    return min_partition_value

# Example usage:
# print(min_partition([1, 3, 2, 4]))  # Output: 1
# print(min_partition([100, 1, 10]))  # Output: 9