Here's the optimum implementation for the sort_even function as described:

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    """
    even_indices = sorted(l[::2])  # Values at even indices sorted
    result = l[:]  # Copy of the original list
    ei = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even_indices[ei]
            ei += 1
    return result

This implementation efficiently:
- Extracts even-indexed values using slicing.
- Sorts them.
- Replaces original even indices with the sorted values, while leaving odd-indexed values unchanged.