# Read the number of strings
N = int(input())

# Initialize a counter for the number of occurrences of "Takahashi"
count = 0

# Iterate over each line of input
for _ in range(N):
    name = input().strip()
    if name == "Takahashi":
        count += 1  # Increment the count if the string is "Takahashi"

# Output the final count
print(count)