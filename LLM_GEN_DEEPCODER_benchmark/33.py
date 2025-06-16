def sort_third(l: list):
    # Create a new list to avoid modifying the original list in place
    result = l.copy()
    
    # Extract elements at indices divisible by 3
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    
    # Sort the extracted elements
    divisible_by_three_sorted = sorted(divisible_by_three)
    
    # Replace the elements at indices divisible by 3 with the sorted values
    sorted_index = 0
    for i in range(len(result)):
        if i % 3 == 0:
            result[i] = divisible_by_three_sorted[sorted_index]
            sorted_index += 1
    
    return result