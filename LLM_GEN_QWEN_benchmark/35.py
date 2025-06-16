def max_element(l: list):
    # Initialize the maximum element to be the first element of the list
    max_value = l[0]
    
    # Iterate through each element in the list starting from the second element
    for element in l[1:]:
        # Update the maximum value if the current element is greater
        if element > max_value:
            max_value = element
    
    # Return the maximum value found in the list
    return max_value

# Example usage
# print(max_element([1, 2, 3]))  # Output: 3
# print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123