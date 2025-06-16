def sort_third(l: list) -> list:
    # Identify indices divisible by 3 (i.e., i % 3 == 0)
    indices_to_sort = [i for i in range(len(l)) if i % 3 == 0]

    # Extract elements at those indices
    values_to_sort = [l[i] for i in indices_to_sort]

    # Sort the extracted values
    sorted_values = sorted(values_to_sort)

    # Create a copy of the original list to avoid mutating it
    result = l[:]

    # Replace the elements at the divisible-by-3 indices with sorted values
    for idx, val in zip(indices_to_sort, sorted_values):
        result[idx] = val

    return result