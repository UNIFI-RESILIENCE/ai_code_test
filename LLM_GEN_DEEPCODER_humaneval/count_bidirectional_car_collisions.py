def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of cars moving in opposite directions.
    
    Each car moving left to right will collide with every car moving right to left. Since there are
    n cars in each direction, the total number of collisions is n * n.
    
    Args:
        n: Number of cars moving in each direction (left to right and right to left).
    
    Returns:
        The total number of collisions, which is n squared.
    """
    return n * n


METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100