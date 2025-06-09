from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Dictionary to count occurrences of each number
    count = {}
    
    # First pass: Count occurrences of each element
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    # Second pass: Collect elements that occur only once
    result = []
    for number in numbers:
        if count[number] == 1:
            result.append(number)
    
    return result

# Example usage
# print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]