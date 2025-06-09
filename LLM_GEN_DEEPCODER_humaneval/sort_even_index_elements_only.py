def sort_even(l: list):
    # Extract values at even indices
    even_indices_values = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the even indices values
    sorted_even_values = sorted(even_indices_values)
    
    # Reconstruct the list by placing sorted values back at even indices
    result = []
    sorted_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_values[sorted_index])
            sorted_index += 1
        else:
            result.append(l[i])
    
    return result