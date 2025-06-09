def minimum_k_avoiding_array_sum(n, k):
    # Set to store the chosen numbers
    chosen_numbers = set()
    
    # Start from the smallest number, i.e., 1
    current_number = 1
    
    # Iterate until we have selected 'n' numbers
    while len(chosen_numbers) < n:
        # Calculate the complement that would make the sum equal to 'k'
        complement = k - current_number
        
        # If the complement is not in the chosen numbers, it's safe to add
        if complement not in chosen_numbers:
            chosen_numbers.add(current_number)
        
        # Move to the next number
        current_number += 1
    
    # Calculate the sum of the chosen numbers
    result_sum = sum(chosen_numbers)
    
    # Return the calculated sum
    return result_sum

# Example usage:
print(minimum_k_avoiding_array_sum(5, 4))  # Output: 18
print(minimum_k_avoiding_array_sum(2, 6))  # Output: 3