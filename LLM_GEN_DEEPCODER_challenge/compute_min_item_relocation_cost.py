def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N
    W = list(map(int, data[idx:idx+N]))
    
    # Create a dictionary to map each box to the list of items it contains
    box_items = {}
    for i in range(N):
        box = A[i]
        if box not in box_items:
            box_items[box] = []
        box_items[box].append(W[i])
    
    total_cost = 0
    
    for box in box_items:
        items = box_items[box]
        if len(items) > 1:
            # To leave the lightest item in the box and move the rest
            items_sorted = sorted(items)
            total_cost += sum(items_sorted[:-1])  # sum all except the lightest
    
    print(total_cost)

solve()