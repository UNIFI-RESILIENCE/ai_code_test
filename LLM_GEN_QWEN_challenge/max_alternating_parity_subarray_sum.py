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
    
    import sys
    
    from sys import stdin
    
    input = stdin.read().split()
    
    index = 0
    t = int(input[index])  # Number of test cases
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(input[index])  # Length of the array
        index += 1
        
        a = list(map(int, input[index:index + n]))  # Elements of the array
        index += n
        
        max_sum = float('-inf')
        current_sum = 0
        last_parity = None
        
        for i in range(n):
            if i == 0 or (last_parity is not None and (a[i] % 2 != last_parity)):
                # Start a new subarray or continue with the current one if parities are alternating
                current_sum += a[i]
                max_sum = max(max_sum, current_sum)
                last_parity = a[i] % 2
            else:
                # Reset the current sum to the current element
                current_sum = a[i]
                max_sum = max(max_sum, current_sum)
                last_parity = a[i] % 2
        
        results.append(max_sum)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()