def change_base(x: int, base: int) -> str:
    # Initialize an empty list to store the remainders
    remainders = []
    
    # Convert the number to the given base by repeatedly dividing by the base
    while x > 0:
        # Append the remainder of the current division
        remainders.append(str(x % base))
        # Update x to be the quotient of the current division
        x //= base
    
    # If the remainders list is empty, it means the input number was 0
    if not remainders:
        return "0"
    
    # Reverse the list to get the correct order of digits in the new base
    remainders.reverse()
    
    # Join the list into a single string to form the final result
    return ''.join(remainders)

# Test cases to validate the implementation of change_base
def check(candidate):
    # Test case for converting 8 to base 3, expected output is '22'
    assert candidate(8, 3) == "22", "Test case 1 failed"
    # Test case for converting 9 to base 3, expected output is '100'
    assert candidate(9, 3) == "100", "Test case 2 failed"
    # Test case for converting 234 to base 2, expected output is '11101010'
    assert candidate(234, 2) == "11101010", "Test case 3 failed"
    # Test case for converting 16 to base 2, expected output is '10000'
    assert candidate(16, 2) == "10000", "Test case 4 failed"
    # Test case for converting 8 to base 2, expected output is '1000'
    assert candidate(8, 2) == "1000", "Test case 5 failed"
    # Test case for converting 7 to base 2, expected output is '111'
    assert candidate(7, 2) == "111", "Test case 6 failed"
    
    # Additional test cases to ensure correctness for bases close to the number
    for x in range(2, 8):
        # The number x in base x+1 should be represented as the digit itself
        assert candidate(x, x + 1) == str(x), f"Test case for {x} in base {x + 1} failed"

# Uncomment the line below to run the check function with the implemented change_base
# check(change_base)