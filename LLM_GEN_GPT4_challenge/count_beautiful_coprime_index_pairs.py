from math import gcd

# Helper function to extract the first digit of a number
def get_first_digit(n):
    while n >= 10:
        n //= 10
    return n

# Helper function to extract the last digit of a number
def get_last_digit(n):
    return n % 10

def count_beautiful_pairs(nums):
    n = len(nums)
    count = 0

    # Iterate through all valid index pairs (i, j) such that i < j
    for i in range(n):
        first_digit = get_first_digit(nums[i])
        for j in range(i + 1, n):
            last_digit = get_last_digit(nums[j])

            # Check if the first digit of nums[i] and last digit of nums[j] are coprime
            if gcd(first_digit, last_digit) == 1:
                count += 1

    return count