def find_losers(n, k):
    """
    Finds the friends who never receive the ball in the game.
    
    Args:
        n (int): Number of friends sitting in a circle.
        k (int): Initial step size used to pass the ball.
    
    Returns:
        list: Sorted list of friends who never received the ball.
    """
    received = set()  # Tracks friends who have received the ball
    current = 1       # The game starts with the 1st friend
    turn = 1          # Turn counter, starts at 1
    
    # Loop until a friend receives the ball for the second time
    while current not in received:
        received.add(current)
        # Calculate the next friend: (current + turn * k - 1) % n + 1
        # The modulo operation handles circular rotation
        current = (current + turn * k - 1) % n + 1
        turn += 1
    
    # The losers are all friends not in the received set
    losers = [i for i in range(1, n+1) if i not in received]
    return sorted(losers)  # Return sorted list of losers