# Read input
N = int(input())
A = list(map(int, input().split()))

# Create a dictionary to store positions of each color
color_positions = {}

# Traverse the list and record each occurrence of each color
for index, color in enumerate(A):
    if color not in color_positions:
        color_positions[color] = []
    color_positions[color].append(index)

# Initialize the counter for valid colors
count = 0

# Check each color's two positions
for color in range(1, N + 1):
    pos1, pos2 = color_positions[color]
    
    # Check if there is exactly one person between the two positions
    if abs(pos1 - pos2) == 2:
        count += 1

# Output the result
print(count)