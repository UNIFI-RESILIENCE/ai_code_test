def car_race_collision(n: int):
    # Each car moving left to right will collide with each car moving right to left.
    # Hence, the total number of collisions is n * n.
    return n * n

# Metadata dictionary, as specified in the prompt
METADATA = {}

# Function to check the correctness of the car_race_collision function
def check(candidate):
    assert candidate(2) == 4, "Test case 1 failed"
    assert candidate(3) == 9, "Test case 2 failed"
    assert candidate(4) == 16, "Test case 3 failed"
    assert candidate(8) == 64, "Test case 4 failed"
    assert candidate(10) == 100, "Test case 5 failed"
    print("All test cases passed!")

# Uncomment the line below to run the check function
# check(car_race_collision)