# Define the target string
target = "abc"

# Read number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    s = input().strip()  # Read the input string

    # If already sorted as 'abc', it's valid
    if s == target:
        print("YES")
        continue

    found = False
    # Convert the string to a list for easy swapping
    chars = list(s)

    # Try all possible pairs to swap (there are 3 positions => 3 unique swaps)
    for i in range(3):
        for j in range(i + 1, 3):
            chars[i], chars[j] = chars[j], chars[i]  # Swap
            if ''.join(chars) == target:
                found = True
            chars[i], chars[j] = chars[j], chars[i]  # Swap back to restore

    print("YES" if found else "NO")