def max_element(lst: list):
    # Initialize the maximum element as the first element of the list
    max_elem = lst[0]
    
    # Iterate through each element in the list starting from the second element
    for elem in lst[1:]:
        # Update max_elem if the current element is greater than max_elem
        if elem > max_elem:
            max_elem = elem
    
    # Return the maximum element found
    return max_elem

# Test cases to verify the correctness of the function
if __name__ == "__main__":
    # Check if the function correctly returns the maximum element in a simple list
    assert max_element([1, 2, 3]) == 3
    
    # Check if the function correctly handles negative numbers and larger lists
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124
    
    # Additional test cases
    assert max_element([-1, -2, -3, -4]) == -1  # All negative numbers
    assert max_element([10]) == 10             # Single element list
    assert max_element([0, 0, 0, 0]) == 0      # List with identical elements
    
    # Print success message if all test cases pass
    print("All test cases passed!")