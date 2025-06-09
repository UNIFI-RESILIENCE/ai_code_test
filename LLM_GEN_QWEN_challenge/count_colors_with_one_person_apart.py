# Read input from standard input
N = int(input())
A = list(map(int, input().split()))

# Initialize a dictionary to store the positions of each color
color_positions = {}

# Iterate over the list A to store the positions of each color
for index, color in enumerate(A):
    if color not in color_positions:
        color_positions[color] = [index + 1]  # Store position (1-based index)
    else:
        color_positions[color].append(index + 1)

# Initialize a counter for the number of valid colors
valid_color_count = 0

# Check each color's positions to see if there is exactly one person in between
for color, positions in color_positions.items():
    # Calculate the difference between the positions of the two people wearing the same color
    position_diff = abs(positions[1] - positions[0])
    
    # If the difference is 2, it means there is exactly one person in between
    if position_diff == 2:
        valid_color_count += 1

# Print the result
print(valid_color_count)