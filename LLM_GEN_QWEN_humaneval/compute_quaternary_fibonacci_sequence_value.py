def fib4(n: int) -> int:
    # Base cases for fib4 sequence
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the first four elements of the sequence
    fib_prev_3, fib_prev_2, fib_prev_1, fib_curr = 0, 2, 0, 0
    
    # Iterate from 4 to n to compute the n-th element
    for i in range(4, n + 1):
        # Compute the current element based on the previous four elements
        fib_curr = fib_prev_1 + fib_prev_2 + fib_prev_3 + fib_prev_4
        
        # Update the previous elements for the next iteration
        fib_prev_4 = fib_prev_3
        fib_prev_3 = fib_prev_2
        fib_prev_2 = fib_prev_1
        fib_prev_1 = fib_curr
    
    return fib_curr

# Test cases to validate the implementation
if __name__ == "__main__":
    assert fib4(5) == 4, "Test case 5 failed"
    assert fib4(6) == 8, "Test case 6 failed"
    assert fib4(7) == 14, "Test case 7 failed"
    assert fib4(8) == 28, "Test case 8 failed"
    assert fib4(10) == 104, "Test case 10 failed"
    assert fib4(12) == 386, "Test case 12 failed"