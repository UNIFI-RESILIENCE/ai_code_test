def longest_equal_subarray(nums, k):
    from collections import defaultdict

    # We'll use a sliding window approach where we track the frequency of each number in the current window
    # The goal is to find the maximum window where (window length - max frequency of any number) <= k
    
    left = 0
    max_len = 0
    freq = defaultdict(int)
    max_freq = 0  # Tracks the highest frequency of any number in the current window

    for right in range(len(nums)):
        num = nums[right]
        freq[num] += 1
        max_freq = max(max_freq, freq[num])

        # Calculate the number of elements to delete: (window length - max_freq)
        # If this exceeds k, we need to move the left pointer forward
        while (right - left + 1 - max_freq) > k:
            freq[nums[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len