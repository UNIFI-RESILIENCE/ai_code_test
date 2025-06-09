def sort_even(l: list):
    # Extract elements at even indices
    even_index_elements = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the extracted elements
    even_index_elements.sort()
    
    # Create a new list to hold the result
    result = l[:]
    
    # Place the sorted elements back into their original even indices
    even_index = 0
    for i in range(0, len(l), 2):
        result[i] = even_index_elements[even_index]
        even_index += 1
    
    return result

# Metadata dictionary can be used for additional data about the function if necessary
METADATA = {}

# Function to check the correctness of the sort_even function
def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3]), "Test case 1 failed"
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123]), "Test case 2 failed"
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10]), "Test case 3 failed"

# Run the check function to validate the implementation
check(sort_even)