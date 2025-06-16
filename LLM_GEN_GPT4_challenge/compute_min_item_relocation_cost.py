import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    W = list(map(int, input().split()))

    # Adjust indices to 0-based
    A = [a - 1 for a in A]

    # Build item -> current box mapping
    position = [-1] * N  # item i is currently in box position[i]
    for item_id in range(N):
        position[item_id] = A[item_id]

    # Create a permutation of which item needs to go to which box
    # dest[i] = j means item i is in box j
    dest = [-1] * N
    for item in range(N):
        dest[position[item]] = item

    visited = [False] * N
    min_global = min(W)  # globally minimum weight for strategy 2
    total_cost = 0

    for i in range(N):
        if visited[i]:
            continue

        # Discover one cycle
        cycle = []
        current = i
        cycle_weight_sum = 0
        cycle_min_weight = float('inf')
        cycle_size = 0

        while not visited[current]:
            visited[current] = True
            item = dest[current]
            cycle.append(item)
            cycle_weight_sum += W[item]
            cycle_min_weight = min(cycle_min_weight, W[item])
            current = item
            cycle_size += 1

        if cycle_size <= 1:
            continue

        # Strategy 1: Rotate within the cycle
        cost1 = cycle_weight_sum + (cycle_size - 2) * cycle_min_weight

        # Strategy 2: Use global minimum item as helper
        cost2 = cycle_weight_sum + cycle_min_weight + (cycle_size + 1) * min_global

        total_cost += min(cost1, cost2)

    print(total_cost)

if __name__ == '__main__':
    main()