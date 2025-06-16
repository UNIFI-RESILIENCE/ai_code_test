from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store the rolling maximum values
    max_values = []
    
    # Check if the input list is empty
    if not numbers:
        return max_values  # Return the empty list if input is empty
    
    # Initialize the current maximum with the first element of the list
    current_max = numbers[0]
    
    # Iterate over each number in the input list
    for number in numbers:
        # Update the current maximum if the current number is greater than the current maximum
        if number > current_max:
            current_max = number
        # Append the current maximum to the result list
        max_values.append(current_max)
    
    return max_values  # Return the list of rolling maximums

# Metadata dictionary for reference
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the `rolling_max` function
def check(candidate):
    assert candidate([]) == []  # Test with an empty list
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]  # Test with strictly increasing list
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]  # Test with strictly decreasing list
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]  # Test with random values