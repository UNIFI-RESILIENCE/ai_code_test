import sys

input = sys.stdin.read

# Read all input at once for efficiency
data = input().split()

index = 0
t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    
    # Compute the total weight of all boxes
    total_weight = sum(a)
    
    # If all boxes have the same weight, all truck loads will be equal
    # So the maximum weight difference between any two trucks is 0
    if min(a) == max(a):
        results.append(0)
        continue

    # To maximize the absolute weight difference between two trucks,
    # group the largest weights together in one truck and the smallest weights in another
    min_sum = sum(a[i] for i in range(n // 2))
    max_sum = sum(a[i] for i in range(n // 2, n))
    
    # Sort box weights to group smallest and largest elements
    a.sort()
    
    # Compute the maximum absolute difference of total weights between trucks
    weight_diff = sum(a[-(n // 2):]) - sum(a[:n // 2])
    
    results.append(weight_diff)

# Output all results
for res in results:
    print(res)