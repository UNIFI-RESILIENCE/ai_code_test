import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        arr = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        if n == 1:
            print(arr[0])
            continue
        
        max_sum = arr[0]
        current_sum = arr[0]
        
        for i in range(1, n):
            # Check if current element has different parity than previous
            if (arr[i] % 2) != (arr[i-1] % 2):
                current_sum = max(arr[i], current_sum + arr[i])
            else:
                current_sum = arr[i]
            max_sum = max(max_sum, current_sum)
        
        print(max_sum)

solve()