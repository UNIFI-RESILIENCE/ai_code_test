def main():
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    input = sys.stdin.read().split()
    
    N = int(input[0])
    H = list(map(int, input[1:]))
    
    # Initialize the answer array with zeros
    answer = [0] * N
    
    # Initialize the count of operations
    current_operations = 0
    
    # Process each A_i from the end to the beginning
    for i in range(N-1, -1, -1):
        # Each round starts by increasing A_0, so we add 1 to the current operation count
        current_operations += 1
        
        # Calculate how many more operations are needed to make A_i > 0 for the first time
        required_operations = H[i] + 1
        
        # Sum up the operations needed for all subsequent elements
        answer[i] = current_operations + required_operations
        
        # Update current_operations to include the newly added operations
        current_operations += required_operations
    
    # Print the results separated by spaces
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    main()