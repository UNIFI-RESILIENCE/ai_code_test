def sort_even(l: list):
    # Extract the values at even indices from the input list
    even_index_values = [l[i] for i in range(0, len(l), 2)]

    # Sort the extracted values
    even_index_values.sort()

    # Initialize a pointer to track position in the sorted even index values
    even_ptr = 0

    # Create a result list by placing sorted even-indexed values in even indices
    # and keeping the original values at the odd indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            # If current index is even, use the next value from the sorted list
            result.append(even_index_values[even_ptr])
            even_ptr += 1
        else:
            # If current index is odd, retain the original value
            result.append(l[i])

    return result