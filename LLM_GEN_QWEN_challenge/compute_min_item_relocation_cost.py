import sys

def main():
    # Read input
    n = int(sys.stdin.readline())
    boxes = list(map(int, sys.stdin.readline().split()))
    weights = list(map(int, sys.stdin.readline().split()))
    
    # Dictionary to hold items per box along with its weights
    box_contents = {}
    
    for i in range(n):
        if boxes[i] not in box_contents:
            box_contents[boxes[i]] = []
        box_contents[boxes[i]].append(weights[i])
    
    # Calculate the minimum cost to move items such that each box contains exactly one item
    min_cost = 0
    
    # Iterate through all the boxes with multiple items
    for box, items in box_contents.items():
        if len(items) > 1:
            # Sort the items in ascending order of their weights
            items.sort()
            # Keep the lightest item in the box and add the weights of the rest to min_cost
            for weight in items[1:]:
                min_cost += weight
    
    # Print the result
    print(min_cost)

if __name__ == "__main__":
    main()