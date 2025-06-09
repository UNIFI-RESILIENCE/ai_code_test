def sort_third(l: list):
    # Find indices that are divisible by 3
    indices_to_sort = [i for i in range(len(l)) if i % 3 == 0]

    # Extract elements from those indices
    elements_to_sort = [l[i] for i in indices_to_sort]

    # Sort the extracted elements
    sorted_elements = sorted(elements_to_sort)

    # Create a copy of the original list to avoid modifying it directly
    result = l[:]

    # Place the sorted elements back into their original positions
    for idx, val in zip(indices_to_sort, sorted_elements):
        result[idx] = val

    return result