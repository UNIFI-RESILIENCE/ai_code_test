# Read the number of test cases
t = int(input().strip())

# Loop through each test case
for _ in range(t):
    # Read the number of digits in the array
    n = int(input().strip())
    
    # Read the digits as a list of integers
    a = list(map(int, input().strip().split()))
    
    # Initialize the maximum product to a very small number
    max_product = -1
    
    # Iterate through each digit in the list
    for i in range(n):
        # Temporary list where the i-th digit is incremented by 1
        temp_a = a[:]
        temp_a[i] += 1
        
        # Calculate the product of the new list
        product = 1
        for num in temp_a:
            product *= num
        
        # Update the maximum product if the current product is larger
        max_product = max(max_product, product)
    
    # Output the maximum product found
    print(max_product)