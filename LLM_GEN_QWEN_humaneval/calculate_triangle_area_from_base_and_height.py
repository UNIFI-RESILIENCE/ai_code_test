METADATA = {}

def triangle_area(a, h):
    # Calculate the area using the formula: (base * height) / 2
    return (a * h) / 2

def check(candidate):
    # Test case 1: Check with base 5 and height 3
    assert candidate(5, 3) == 7.5, "Test case 1 failed"
    
    # Test case 2: Check with base 2 and height 2
    assert candidate(2, 2) == 2.0, "Test case 2 failed"
    
    # Test case 3: Check with base 10 and height 8
    assert candidate(10, 8) == 40.0, "Test case 3 failed"

# Run the check function to validate the triangle_area function
check(triangle_area)