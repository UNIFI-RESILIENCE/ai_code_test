# Initialize a set with the initial positions of the marbles, ensuring no duplicates
occupied_positions = set(nums)

# Iterate over each move, updating the positions accordingly
for src, dest in zip(moveFrom, moveTo):
    # Remove all marbles from the source position
    occupied_positions.remove(src)
    # Add all marbles to the destination position
    occupied_positions.add(dest)

# Convert the set to a sorted list to return the final occupied positions
sorted_occupied_positions = sorted(occupied_positions)

# Output the sorted list of occupied positions
sorted_occupied_positions