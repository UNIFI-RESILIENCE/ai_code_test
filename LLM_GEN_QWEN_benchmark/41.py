def car_race_collision(n: int) -> int:
    # Since each car moving left to right will collide with each car moving right to left,
    # the total number of collisions is simply the product of the number of cars in each direction.
    return n * n

# Example usage:
# n = 3
# There are 3 cars moving left to right and 3 cars moving right to left.
# Each car from one direction will collide with each car from the opposite direction.
# Total collisions = 3 * 3 = 9

# print(car_race_collision(3))  # Output: 9