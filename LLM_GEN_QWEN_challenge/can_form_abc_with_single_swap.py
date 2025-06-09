# Number of test cases
t = int(input().strip())

# Iterate through each test case
for _ in range(t):
    # Read the current arrangement of cards
    current_arrangement = input().strip()
    
    # Check if the current arrangement is already "abc"
    if current_arrangement == "abc":
        print("YES")
    else:
        # Generate all possible arrangements after one swap
        swapped_arrangements = [
            current_arrangement[1] + current_arrangement[0] + current_arrangement[2],
            current_arrangement[0] + current_arrangement[2] + current_arrangement[1],
            current_arrangement[2] + current_arrangement[1] + current_arrangement[0]
        ]
        
        # Also consider the arrangements where the second character is swapped
        swapped_arrangements.extend([
            current_arrangement[0] + current_arrangement[2] + current_arrangement[1],
            current_arrangement[1] + current_arrangement[0] + current_arrangement[2]
        ])
        
        # Check if any of the swapped arrangements is "abc"
        if "abc" in swapped_arrangements:
            print("YES")
        else:
            print("NO")