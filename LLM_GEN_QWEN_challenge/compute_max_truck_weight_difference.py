def main():
    import sys
    import sys
    input = sys.stdin.read().splitlines()
    
    index = 0
    t = int(input[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(input[index])
        index += 1
        weights = list(map(int, input[index].split()))
        index += 1
        
        # Calculate prefix sums for efficient subarray sum calculation
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + weights[i]
        
        max_diff = 0
        
        # Iterate over all possible values of k from 1 to n
        for k in range(1, n + 1):
            if n % k != 0:
                continue  # Skip if n is not divisible by k
            
            truck_weights = []
            for i in range(n // k):
                start_index = i * k
                end_index = (i + 1) * k
                truck_weight = prefix_sums[end_index] - prefix_sums[start_index]
                truck_weights.append(truck_weight)
            
            if truck_weights:
                max_weight = max(truck_weights)
                min_weight = min(truck_weights)
                max_diff = max(max_diff, abs(max_weight - min_weight))
        
        results.append(max_diff)
    
    for result in results:
        print(result)

# Read from stdin and run the main function
if __name__ == "__main__":
    main()