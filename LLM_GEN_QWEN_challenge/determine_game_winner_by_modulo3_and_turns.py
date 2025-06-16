# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    # Read the initial integer value for the current test case
    n = int(input().strip())
    
    # Determine the remainder when n is divided by 3
    remainder = n % 3
    
    # Based on the remainder, determine the outcome
    if remainder == 0:
        # If n is already divisible by 3, Vanya wins immediately
        print("First")
    elif remainder == 1:
        # If remainder is 1, it means after Vanya's turn, the number can never be made divisible by 3 on his turn.
        # Vova will make the number divisible by 3 on his turn in the best case.
        print("First")
    else:  # remainder == 2
        # If remainder is 2, it's Vanya's turn to make the number divisible by 3 (subtract 1 and make it divisible by 3)
        print("First")

    # Explanation:
    # - If `remainder` is `0`, Vanya wins immediately as `n` is already divisible by 3.
    # - If `remainder` is `1` or `2`, Vanya can always force the number to become divisible by 3 in his first turn:
    #   - If `remainder` is `1`, Vanya adds `1` -> `(n + 1) % 3 == 0`.
    #   - If `remainder` is `2`, Vanya subtracts `1` -> `(n - 1) % 3 == 0`.

    # In all these scenarios, Vanya wins on his first move or ensures that within the 10 moves constraint, he will win.