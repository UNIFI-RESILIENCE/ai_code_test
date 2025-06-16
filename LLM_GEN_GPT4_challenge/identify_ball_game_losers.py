def find_losers(n, k):
    # Initialize a list to track how many times each friend received the ball
    received = [0] * n

    # Start from the first friend (index 0 in zero-based indexing)
    current = 0
    step = 1  # Step multiplier starts from 1

    # Continue the game until a friend gets the ball twice
    while received[current] == 0:
        received[current] = 1
        # Calculate the next position in the circle using modular arithmetic
        current = (current + step * k) % n
        step += 1

    # Gather all friends who never received the ball
    losers = []
    for i in range(n):
        if received[i] == 0:
            losers.append(i + 1)  # Convert back to 1-based indexing

    return losers
