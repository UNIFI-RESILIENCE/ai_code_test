from collections import defaultdict

def longest_equal_subarray(nums, k):
    # Map each value to the list of its indices in nums
    positions = defaultdict(list)
    for index, value in enumerate(nums):
        positions[value].append(index)

    max_length = 0

    # Iterate through all possible values in nums
    for indices in positions.values():
        left = 0  # Left pointer of the sliding window
        # Iterate with right pointer through indices of a particular number
        for right in range(len(indices)):
            # Number of deletions needed to make current subarray contiguous
            deletions = indices[right] - indices[left] - (right - left)
            # Shrink the window from the left until deletions <= k
            while deletions > k:
                left += 1
                deletions = indices[right] - indices[left] - (right - left)
            # Update the maximum length of equal subarray
            max_length = max(max_length, right - left + 1)

    return max_length