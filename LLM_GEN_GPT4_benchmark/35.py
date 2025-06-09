def max_element(l: list):
    # Check if the list is empty to avoid ValueError from max()
    if not l:
        raise ValueError("max_element() arg is an empty list")
    
    # Initialize the maximum with the first element of the list
    maximum = l[0]
    
    # Iterate through the list to find the maximum element
    for element in l[1:]:
        if element > maximum:
            maximum = element
    
    return maximum