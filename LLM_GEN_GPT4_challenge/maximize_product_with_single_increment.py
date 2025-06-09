t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of digits in the current test case
    a = list(map(int, input().split()))  # The digits array

    max_product = 0

    # Try adding 1 to each digit one by one
    for i in range(n):
        modified_digits = a.copy()
        modified_digits[i] += 1  # Add 1 to the i-th digit

        product = 1
        for digit in modified_digits:
            product *= digit  # Compute the product of all digits after modification

        # Keep track of the maximum product found so far
        max_product = max(max_product, product)

    print(max_product)  # Output the result for this test case