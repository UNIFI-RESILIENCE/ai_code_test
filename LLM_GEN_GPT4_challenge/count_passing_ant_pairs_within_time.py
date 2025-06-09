import sys
import bisect

# Read input from standard input
input = sys.stdin.readline

# Read number of ants N and time T
N, T = map(int, input().split())

# Read direction string S
S = input().strip()

# Read positions of the ants
X = list(map(int, input().split()))

# Create list of tuples: (position, direction)
# direction is True if facing right (1), False if facing left (0)
ants = [(X[i], S[i] == '1') for i in range(N)]

# Sort the ants by position to ensure correct left-to-right traversal
ants.sort()

# Lists to store positions of ants facing left and right
# right_moving will be maintained as a running list to perform binary search
right_moving = []

# Result counter
result = 0

# Preprocess positions into separate lists for quicker processing
# We process from left to right so that for an ant moving left at position xi,
# it may intersect with any ant moving right at xj if xi - xj <= 2 * T
for pos, is_right in ants:
    if is_right:
        # Add the current position to sorted right_moving list
        bisect.insort(right_moving, pos)
    else:
        # For a left-moving ant at pos, find how many right-moving ants are
        # within distance 2 * T behind it (i.e., xj >= pos - 2T)
        left_bound = pos - 2 * T
        index = bisect.bisect_left(right_moving, left_bound)
        valid_pairs = len(right_moving) - index
        result += valid_pairs

# Print the final result
print(result)