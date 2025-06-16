def find_losers(n, k):
    # Create a set to keep track of friends who have received the ball
    received_ball = set()
    
    # Initialize the starting position
    current_friend = 0  # Using 0-based indexing for internal calculations
    
    # Add the starting friend as they receive the ball first
    received_ball.add(current_friend)
    
    # Counter for the current iteration (starting from 1 as per problem description)
    iterations = 1
    
    while True:
        # Calculate who will receive the ball next based on the current position, iteration, and k
        next_friend = (current_friend + iterations * k) % n
        # If the next friend has already received the ball, then the game ends
        if next_friend in received_ball:
            break
        # Update the received_ball set with the new friend receiving the
        received_ball.add(next_friend)
        # Move to the next friend and increment the iteration counter
        current_friend = next_friend
        iterations += 1
    
    # Friends who are not in 'received_ball' are the losers
    # Convert their indices from 0-based to 1-based
    losers = [friend + 1 for friend in range(n) if friend not in received_ball]
    
    # Return the sorted list of losers
    return sorted(losers)

# Example usage:
if __name__ == "__main__":
    print(find_losers(5, 2))  # Output: [4, 5]
    print(find_losers(4, 4))  # Output: [2, 3, 4]