def sort_third(l: list) -> list:
    # Extract elements at indices divisible by three
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    
    # Sort the extracted elements
    divisible_by_three.sort()
    
    # Create a new list to hold the result
    result = l[:]
    
    # Replace elements at indices divisible by three with sorted elements
    index = 0
    for i in range(0, len(l), 3):
        result[i] = divisible_by_three[index]
        index += 1
    
    return result

# Example usage
print(sort_third([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]