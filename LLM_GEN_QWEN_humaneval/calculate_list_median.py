def median(l: list):
    # Sort the list to find the median
    sorted_list = sorted(l)
    
    # Calculate the number of elements in the list
    n = len(sorted_list)
    
    # Find the median based on whether the number of elements is odd or even
    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_list[n // 2]
    else:
        # If even, return the average of the two middle elements
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2.0

# Define metadata dictionary (though not used in the function)
METADATA = {}

# Function to test the median function with various test cases
def check(candidate):
    # Odd number of elements with a clear middle value
    assert candidate([3, 1, 2, 4, 5]) == 3
    
    # Even number of elements requiring average of two middle values
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 15.0
    
    # Single element list
    assert candidate([5]) == 5
    
    # Two element list requiring average
    assert candidate([6, 5]) == 5.5
    
    # Another example with an odd number of elements
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

# Uncomment the line below to run tests
# check(median)