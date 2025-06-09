n = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    # Find the positions of the two occurrences of color i
    indices = [index for index, color in enumerate(A) if color == i]
    pos1, pos2 = indices
    # Check if there is exactly one element between them
    if abs(pos1 - pos2) == 2:
        count += 1

print(count)