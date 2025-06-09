from math import gcd

def count_beautiful_pairs(nums):
    # Initialize a counter for beautiful pairs
    beautiful_pairs_count = 0
    
    # Iterate over each pair of indices (i, j) with 0 <= i < j < len(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Extract the first digit of nums[i]
            first_digit = int(str(nums[i])[0])
            
            # Extract the last digit of nums[j]
            last_digit = nums[j] % 10
            
            # Check if the first digit and last digit are coprime
            if gcd(first_digit, last_digit) == 1:
                # Increment the counter if they are coprime
                beautiful_pairs_count += 1
    
    # Return the total count of beautiful pairs
    return beautiful_pairs_count

# Example usage:
print(count_beautiful_pairs([2, 5, 1, 4]))  # Output: 5
print(count_beautiful_pairs([11, 21, 12]))  # Output: 2