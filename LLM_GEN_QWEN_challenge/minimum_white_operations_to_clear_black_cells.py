import sys

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
    input = sys.stdin.read().splitlines()
    
    # Read the number of test cases
    t_index = 0
    t = int(input[t_index])
    t_index += 1
    
    results = []
    
    for _ in range(t):
        # Read n and k for the current test case
        n, k = map(int, input[t_index].split())
        t_index += 1
        
        # Read the string s for the current test case
        s = input[t_index]
        t_index += 1
        
        # Initialize the number of operations
        operations = 0
        
        # Initialize the position where the next operation will start
        pos = 0
        
        while pos < n:
            if s[pos] == 'B':
                # If we encounter a black cell, start an operation here
                operations += 1
                # Skip the next k cells since they will be converted to white
                pos += k
            else:
                # Move to the next cell
                pos += 1
        
        # Store the result for the current test case
        results.append(operations)
    
    # Print all results at once for better performance
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()