# Read the number of strings
N = int(input())

# Initialize a counter for "Takahashi" occurrences
count = 0

# Iterate through each string
for _ in range(N):
    S = input().strip()
    if S == "Takahashi":
        count += 1

# Output the count
print(count)