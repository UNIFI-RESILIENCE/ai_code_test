def marbles_position(nums, moveFrom, moveTo):
    """
    Process the moves of marbles from initial positions and return the final occupied positions in sorted order.
    
    Args:
        nums: List[int], initial positions of marbles.
        moveFrom: List[int], list of source positions for each move.
        moveTo: List[int], list of destination positions for each move.
        
    Returns:
        List[int]: Sorted list of occupied positions after all moves.
    """
    # Use a dictionary to keep track of the count of marbles at each position
    position_counts = {}
    
    # Initialize the position counts with the initial positions
    for pos in nums:
        position_counts[pos] = position_counts.get(pos, 0) + 1
    
    # Process each move
    for i in range(len(moveFrom)):
        src = moveFrom[i]
        dest = moveTo[i]
        
        # Check if there are marbles at the source position
        if src in position_counts:
            count = position_counts[src]
            # Remove the marbles from the source position
            del position_counts[src]
            # Add the marbles to the destination position
            position_counts[dest] = position_counts.get(dest, 0) + count
    
    # Extract the keys (positions), sort them, and return
    return sorted(position_counts.keys())