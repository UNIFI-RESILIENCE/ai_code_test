from collections import Counter

def relocateMarbles(nums, moveFrom, moveTo):
    # Count marbles at each initial position
    position_counts = Counter(nums)

    # Process all moves
    for i in range(len(moveFrom)):
        from_pos = moveFrom[i]
        to_pos = moveTo[i]

        # Transfer all marbles from from_pos to to_pos, if any
        if from_pos in position_counts:
            count = position_counts[from_pos]
            position_counts[to_pos] += count
            del position_counts[from_pos]  # Remove from_pos if no marbles remain

    # Gather all remaining occupied positions and return them sorted
    return sorted(position_counts.keys())