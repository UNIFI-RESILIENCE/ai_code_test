# Each left-to-right car will collide with every right-to-left car
# Since there are n cars in each direction, the total number of collisions is n * n

def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of cars moving towards each other.

    Each car in the left-to-right direction will intersect with every car in the right-to-left direction,
    regardless of the exact position because all cars travel at the same speed and preserve direction post-collision.

    Args:
        n (int): Number of cars moving in each direction.

    Returns:
        int: Total number of collisions between the two sets of cars.
    """
    return n * n