def max_achievable_number(num, t):
    # To maximize x, we need to increase x as much as possible while decreasing num
    # Since we can perform the operation up to t times, and each operation allows
    # both num and x to change by 1, the maximum difference we can achieve is 2 * t
    # Thus, the maximum possible value of x is num + 2 * t
    
    return num + 2 * t

# Example usage:
# Example 1
num1 = 4
t1 = 1
print(max_achievable_number(num1, t1))  # Output should be 6

# Example 2
num2 = 3
t2 = 2
print(max_achievable_number(num2, t2))  # Output should be 7