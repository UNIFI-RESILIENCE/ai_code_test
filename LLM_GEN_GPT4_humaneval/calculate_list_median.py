def median(l: list):
    # Sort the list to arrange elements in non-decreasing order
    l_sorted = sorted(l)
    n = len(l_sorted)

    # If the number of elements is odd, return the middle element
    if n % 2 == 1:
        return l_sorted[n // 2]
    else:
        # If even, return the average of the two middle elements
        mid1 = l_sorted[n // 2 - 1]
        mid2 = l_sorted[n // 2]
        return (mid1 + mid2) / 2.0