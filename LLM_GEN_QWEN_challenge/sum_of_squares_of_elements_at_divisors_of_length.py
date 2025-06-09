def sum_of_squares_of_special_elements(nums):
    # Initialize the sum variable to store the sum of squares of special elements
    total_sum = 0
    
    # Get the length of the nums array (1-indexed length)
    n = len(nums)
    
    # Iterate through the nums array considering 1-based index
    for i in range(1, n + 1):
        # Check if the current index 'i' divides the length of the array 'n'
        if n % i == 0:
            # If true, add the square of the current element nums[i-1] to total_sum
            total_sum += nums[i - 1] ** 2
    
    # Return the final computed sum
    return total_sum

# Example usage:
# Uncomment the lines below to test the function with example inputs
# print(sum_of_squares_of_special_elements([1, 2, 3, 4]))  # Output: 21
# print(sum_of_squares_of_special_elements([2, 7, 1, 19, 18, 3]))  # Output: 63