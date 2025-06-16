def median(l: list):
    # Sort the list to arrange elements in ascending order
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    # Calculate the midpoint index
    mid = n // 2

    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle one
        return sorted_list[mid]
    else:
        # If the list has an even number of elements, return the average of the two middle elements
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0