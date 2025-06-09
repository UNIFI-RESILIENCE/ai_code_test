def sort_even(l: list):
    # Extract values at even indices
    even_index_values = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the extracted values
    even_index_values.sort()
    
    # Create a new list to store the result
    result = l[:]
    
    # Replace values at even indices in the result list with the sorted values
    even_index = 0
    for i in range(0, len(l), 2):
        result[i] = even_index_values[even_index]
        even_index += 1
    
    return result