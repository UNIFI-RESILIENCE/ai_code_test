import sys

# Read input
input = sys.stdin.readline
N = int(input())
H = list(map(int, input().split()))

# Initialize the result list
res = [0] * N

# time: total number of operations
time = 0
# curr: the amount of value currently at A[i]
curr = 0

# Traverse from left to right
for i in range(N):
    # If the current height H[i] is less than the current 'curr', simulate required delays
    # By computing when it can receive first value (i.e., needs to be better than all Hs before)
    if curr <= H[i]:
        # If the current value can be received directly, compute how many pushes needed
        time += H[i] - curr + 1
        curr = H[i] + 1
    else:
        # There's already sufficient flow to push value to A[i]
        time += 1
        curr += 1

    # Store the timestep when A[i+1] received its first >0 value
    res[i] = time

# Print output
print(' '.join(map(str, res)))