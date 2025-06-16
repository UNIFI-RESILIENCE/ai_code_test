import sys

# Read the number of test cases
t = int(sys.stdin.readline())

for _ in range(t):
    # Read the size of the array
    n = int(sys.stdin.readline())
    # Read the array elements
    a = list(map(int, sys.stdin.readline().split()))
    
    # Initialize answer with the first element
    max_sum = a[0]
    current_sum = a[0]
    
    for i in range(1, n):
        # Check if the current element has different parity than the previous one
        if (a[i] % 2) != (a[i-1] % 2):
            # Extend the alternating subarray
            current_sum += a[i]
        else:
            # Restart from current element
            current_sum = a[i]
        
        # Update the maximum sum seen so far
        if current_sum > max_sum:
            max_sum = current_sum
    
    # Output the result for this test case
    print(max_sum)