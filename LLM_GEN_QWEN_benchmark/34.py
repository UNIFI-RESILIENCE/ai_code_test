def unique(l: list) -> list:
    # Convert the list to a set to remove duplicate elements
    unique_elements = set(l)
    
    # Convert the set back to a list and sort it
    sorted_unique_list = sorted(unique_elements)
    
    return sorted_unique_list

# Example usage:
# result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
# print(result)  # Output: [0, 2, 3, 5, 9, 123]