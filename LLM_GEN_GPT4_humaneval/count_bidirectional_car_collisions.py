def car_race_collision(n: int) -> int:
    # Each of the n cars from the left-to-right group will eventually encounter
    # all n cars from the right-to-left group since they are on a single infinite line.
    # Thus, the total number of collisions is n * n.
    return n * n