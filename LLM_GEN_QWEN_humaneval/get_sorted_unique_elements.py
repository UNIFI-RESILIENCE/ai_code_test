# Function to return sorted unique elements from a list
def unique(l: list) -> list:
    # Convert the list to a set to remove duplicates
    unique_elements = set(l)
    
    # Sort the unique elements and convert back to a list
    sorted_unique_list = sorted(unique_elements)
    
    return sorted_unique_list

# Metadata dictionary (currently empty, but included per your instruction)
METADATA = {}

# Check function to validate the correctness of the unique function
def check(candidate):
    # Test case to verify the function's output
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]