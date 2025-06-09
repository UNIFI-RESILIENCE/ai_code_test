def sort_even(l: list) -> list:
    # Extract elements at even indices (0-based indexing: 0, 2, 4, ...)
    even_index_values = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the extracted values
    even_index_values.sort()
    
    # Initialize an iterator for the sorted even-indexed values
    even_iter = iter(even_index_values)
    
    # Construct the output list by replacing even indices with sorted values,
    # and keeping odd indices unchanged
    result = [next(even_iter) if i % 2 == 0 else l[i] for i in range(len(l))]
    
    return result