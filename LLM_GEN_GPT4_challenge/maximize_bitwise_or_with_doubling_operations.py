from typing import List

def maximumOr(nums: List[int], k: int) -> int:
    n = len(nums)
    
    # Initialize prefix and suffix arrays
    prefix = [0] * n
    suffix = [0] * n

    # Compute prefix OR values
    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] | nums[i]

    # Compute suffix OR values
    suffix[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] | nums[i]

    max_or = 0
    for i in range(n):
        # Apply the operation to the current element by multiplying it 2^k times
        powered = nums[i] << k

        # Compute the OR of all other elements excluding current
        current_or = 0
        if i > 0:
            current_or |= prefix[i - 1]
        if i < n - 1:
            current_or |= suffix[i + 1]

        # Combine the powered value with the OR of the rest
        total_or = powered | current_or

        max_or = max(max_or, total_or)

    return max_or