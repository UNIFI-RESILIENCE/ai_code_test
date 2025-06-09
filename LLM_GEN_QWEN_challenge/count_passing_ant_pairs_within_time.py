import sys
import bisect

# Read input from standard input
input = sys.stdin.read().split()
N = int(input[0])
T = int(input[1])
S = input[2]
X = list(map(int, input[3:]))

# Convert direction string to a list of integers for easier processing
directions = [1 if s == '1' else -1 for s in S]

# Create a list of tuples (x, d) where x is the position and d is the direction
ants = [(X[i], directions[i]) for i in range(N)]

# Sort the ants based on their initial positions
ants.sort()

# Initialize a counter for the number of pairs
count_pairs = 0

# Use a list to keep track of ants moving to the right (direction 1)
right_moving_ants = []

# Iterate through each ant
for i in range(N):
    x, d = ants[i]
    
    if d == 1:
        # If the ant is moving to the right, add its position to the list
        bisect.insort(right_moving_ants, x)
    else:
        # Count how many right-moving ants this left-moving ant will meet
        # A left-moving ant at position x meets all right-moving ants with positions < (x + T)
        meet_count = bisect.bisect_left(right_moving_ants, x + T)
        count_pairs += meet_count

# Output the number of pairs
print(count_pairs)