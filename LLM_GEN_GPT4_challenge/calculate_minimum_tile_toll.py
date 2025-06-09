# Read input from standard input
Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

# Function to determine the tile coordinates.
# Each 2x1 tile covers two adjacent integer squares based on the parity of (i+j)
def get_tile_coordinates(x, y):
    if (x + y) % 2 == 0:
        return (x, y)
    else:
        return (x - 1, y)

# Extract the tile coordinates for the start and target points
start_tile_x, start_tile_y = get_tile_coordinates(Sx, Sy)
target_tile_x, target_tile_y = get_tile_coordinates(Tx, Ty)

# Compute number of tile transitions needed in x and y direction
# Since each tile spans 2 units in one direction, we divide the difference by 2
toll = (abs(start_tile_x - target_tile_x) + abs(start_tile_y - target_tile_y)) // 2

# Output the total toll
print(toll)