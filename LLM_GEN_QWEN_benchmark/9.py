from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store the rolling maximums
    max_list = []
    
    # Initialize a variable to keep track of the current maximum
    current_max = float('-inf')  # Start with the smallest possible value
    
    # Iterate through each number in the input list
    for num in numbers:
        # Update the current maximum if the current number is greater
        if num > current_max:
            current_max = num
        
        # Append the current maximum to the result list
        max_list.append(current_max)
    
    # Return the list of rolling maximums
    return max_list