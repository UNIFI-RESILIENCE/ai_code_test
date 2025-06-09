def main():
    import sys
    
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    
    # Initialize index for parsing the input data
    index = 0
    
    # Read the number of test cases
    t = int(input_data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        # Read n (number of elements in the array) and k (divisibility factor)
        n = int(input_data[index])
        k = int(input_data[index + 1])
        index += 2
        
        # Read the array elements
        a = list(map(int, input_data[index:index + n]))
        index += n
        
        # If k is 2 or 4, check how many even numbers are already in the array
        if k in {2, 4}:
            even_count = sum(1 for x in a if x % 2 == 0)
            
            # To make the product divisible by 2, we need at least one even number
            if k == 2 and even_count > 0:
                results.append(0)
            # To make the product divisible by 4, we need at least two even numbers
            elif even_count >= 2:
                results.append(0)
            else:
                # Find the smallest odd number to convert it to even
                min_odd = min(x for x in a if x % 2 != 0)
                
                if k == 2:
                    results.append(1)
                # For k == 4, we need one more operation to ensure the product is divisible by 4
                elif even_count == 1 or even_count == 0:
                    results.append(min(3 - min_odd, 2))
                elif even_count == 1:
                    min_second_odd = min(x for x in a if x % 2 != 0 and x != min_odd)
                    results.append(min(1, 3 - min_second_odd))
        
        # If k is 3 or 5, check how many numbers are already divisible by k
        elif k in {3, 5}:
            divisible_count = sum(1 for x in a if x % k == 0)
            
            # No operations needed if there's at least one number divisible by k
            if divisible_count > 0:
                results.append(0)
            else:
                # Find the numbers that require the least increment to become divisible by k
                increments = [(x % k, k - x % k) for x in a]
                # Sort increments by the number of operations required
                increments.sort(key=lambda x: x[1])
                
                # Try to use the least number of operations:
                # Either increment one number by (k - x % k) directly
                # Or increment two numbers partially to reach divisibility by k
                if increments[0][0] == 0:
                    results.append(0)
                elif increments[0][1] == k - 1 and len(increments) > 1:
                    results.append(1)
                else:
                    results.append(increments[0][1])
    
    # Print all results at once for efficiency
    print('\n'.join(map(str, results)))

# Execute the main function
if __name__ == "__main__":
    main()