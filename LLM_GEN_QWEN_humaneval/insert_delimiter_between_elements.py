def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    # If the input list is empty, return an empty list
    if not numbers:
        return []
    
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]
    
    # Iterate over the input list starting from the second element
    for number in numbers[1:]:
        # Append the delimeter and the current number to the result list
        result.append(delimeter)
        result.append(number)
    
    return result


# Metadata dictionary containing author and dataset information
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


# Function to check the correctness of the intersperse function
def check(candidate):
    # Test cases to validate the function
    assert candidate([], 7) == [], "Test case 1 failed"
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2], "Test case 2 failed"
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2], "Test case 3 failed"

# Call the check function to run the test cases
check(intersperse)