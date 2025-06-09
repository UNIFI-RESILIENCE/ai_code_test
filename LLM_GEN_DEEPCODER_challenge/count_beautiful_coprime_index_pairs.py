import math

def count_beautiful_pairs(nums):
    count = 0
    n = len(nums)
    
    for i in range(n):
        # Extract the first digit of nums[i]
        first_digit = nums[i]
        while first_digit >= 10:
            first_digit //= 10
        
        for j in range(i + 1, n):
            # Extract the last digit of nums[j]
            last_digit = nums[j] % 10
            
            # Check if the first and last digits are coprime
            if math.gcd(first_digit, last_digit) == 1:
                count += 1
                
    return count