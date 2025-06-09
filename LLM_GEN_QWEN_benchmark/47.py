def median(l: list) -> float:
    # Sort the input list to find the median easily
    sorted_list = sorted(l)
    
    # Get the number of elements in the list
    n = len(sorted_list)
    
    # Calculate and return the median
    # If the number of elements is odd, return the middle one
    if n % 2 == 1:
        return sorted_list[n // 2]
    # If the number of elements is even, return the average of the two middle elements
    else:
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

# Example usage
# print(median([3, 1, 2, 4, 5]))  # Output: 3
# print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0