from collections import defaultdict

def longestEqualSubarray(nums, k):
    # Dictionary to store the frequency of each number in the current window
    count = defaultdict(int)
    
    # Initialize the sliding window pointers and the maximum length of equal subarray found
    left = 0
    max_equal_length = 0
    
    for right in range(len(nums)):
        # Increment the count of the current element
        count[nums[right]] += 1
        
        # Get the maximum frequency of any element in the current window
        max_freq = max(count.values())
        
        # Calculate the number of deletions required to make all elements in the window equal
        current_length = right - left + 1
        deletions_required = current_length - max_freq
        
        # If deletions required exceed k, shrink the window from the left
        if deletions_required > k:
            count[nums[left]] -= 1
            # If the count of the leftmost element drops to zero, remove it from the dictionary
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        
        # Update the maximum length of equal subarray found
        max_equal_length = max(max_equal_length, max_freq)
    
    return max_equal_length

# Example usage:
print(longestEqualSubarray([1, 3, 2, 3, 1, 3], 3))  # Output: 3
print(longestEqualSubarray([1, 1, 2, 2, 1, 1], 2))  # Output: 4