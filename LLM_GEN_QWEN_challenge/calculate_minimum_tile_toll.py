def min_toll(s_x, s_y, t_x, t_y):
    # Calculate the horizontal and vertical distances between the start and end points
    delta_x = abs(t_x - s_x)
    delta_y = abs(t_y - s_y)
    
    # Initialize the toll
    toll = 0
    
    # Check if the starting tile is the same as the ending tile
    # Starting tile identifier: (s_x // 2, s_y) if s_x is even else (s_x // 2, s_y - 1)
    # Ending tile identifier: (t_x // 2, t_y) if t_x is even else (t_x // 2, t_y - 1)
    start_tile = (s_x // 2, s_y if s_x % 2 == 0 else s_y - 1)
    end_tile = (t_x // 2, t_y if t_x % 2 == 0 else t_y - 1)
    
    # Check if we are already on the same tile
    if start_tile == end_tile:
        return toll
    
    # If start and end tiles are not the same, we need to calculate the toll
    # Since the tiles are 2x1, moving horizontally by 2 doesn't change the tile number
    # But moving vertically or horizontally by an odd distance changes the tile number
    toll += delta_x // 2  # Moving in steps of 2 horizontally doesn't cost any toll
    
    # If there's a remaining step in the horizontal direction, add 1 toll
    if delta_x % 2 != 0:
        toll += 1
    
    toll += delta_y // 2  # Moving in steps of 2 vertically doesn't cost any toll
    
    # If there's a remaining step in the vertical direction, add 1 toll
    if delta_y % 2 != 0:
        toll += 1
    
    # Adjust the toll if entering a new tile due to the special rule when i+j is even
    # Ensure the tile boundary adjustment doesn't affect the toll count as it's already considered
    
    return toll

# Read input from standard input
import sys
input = sys.stdin.read().split()

# Parse the input values
s_x, s_y = int(input[0]), int(input[1])
t_x, t_y = int(input[2]), int(input[3])

# Print the result
print(min_toll(s_x, s_y, t_x, t_y))