def max_product_with_increment(test_cases):
    results = []
    
    for _ in range(test_cases):
        n = int(input())
        digits = list(map(int, input().split()))
        
        # If there's any zero in the digits, incrementing a zero produces the maximum product
        if 0 in digits:
            max_product = 1
            for d in digits:
                if d != 0:
                    max_product *= d
            results.append(max_product)
        else:
            max_product = 0
            for i in range(n):
                incremented_digits = digits[:]
                incremented_digits[i] += 1
                product = 1
                for d in incremented_digits:
                    product *= d
                max_product = max(max_product, product)
            results.append(max_product)
    
    return results

# Read the number of test cases
t = int(input())

# Get the results for all test cases
results = max_product_with_increment(t)

# Print the results
for result in results:
    print(result)
```

### Explanation:
1. **Reading Input:** The code reads the number of test cases and for each test case, it reads the number of digits (`n`) and the list of digits.
2. **Handling Case with Zero:** If there is any `0` in the list of digits, the product can be maximized by turning the first `0` into a `1`. All other non-zero digits remain as they are since multiplying anything by `0` results in `0`.
3. **Incrementing Each Digit One By One:** If there are no `0`s in the digits, the code tries incrementing each digit by `1` once at a time, calculates the product, and keeps track of the maximum product obtained.
4. **Output:** After processing all test cases, the code outputs the maximum product for each test case.

### Assumptions:
- The constraints are adhered to: `1 <= t <= 10^4`, `1 <= n <= 9`, and `0 <= a_i <= 9`.
- `input()` function is used for simplicity, but you could also use standard input methods suitable for competitive programming environments like `sys.stdin`.

### Sample Run:
Given the sample input:

```
4
4
2 2 1 2
3
0 1 2
5
4 3 2 3 4
9
9 9 9 9 9 9 9 9 9
```

The output would be:

```
16
2
432
430467210