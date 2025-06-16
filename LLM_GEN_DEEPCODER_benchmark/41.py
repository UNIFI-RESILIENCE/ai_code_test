def car_race_collision(n: int):
    """
    Calculate the number of collisions between two sets of cars moving in opposite directions.
    
    Each left-to-right car will collide with each right-to-left car exactly once. Since there are
    n cars in each direction, the total number of collisions is n * n.
    
    Args:
        n (int): Number of cars in each direction.
        
    Returns:
        int: Total number of collisions.
    """
    return n * n