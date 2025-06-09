def min_operations(num1, num2):
    # Maximum number of operations to consider (given constraints)
    MAX_OPS = 61
    
    # Try different numbers of operations from 0 to 60
    for k in range(1, MAX_OPS + 1):
        # Calculate the target value after k operations
        target = num1 - k * num2
        
        # Calculate the number of 1-bits in the binary representation of target
        bits_in_target = bin(target).count('1')
        
        # If the number of bits in the target is less than or equal to k
        # and the remaining value after subtracting k is non-negative
        if bits_in_target <= k and target >= k * k:
            return k
    
    # If no valid number of operations is found, return -1
    return -1

# Example usage:
print(min_operations(3, -2))  # Output: 3
print(min_operations(5, 7))   # Output: -1