t = int(input())
for _ in range(t):
    s = input().strip()
    if s == 'abc':
        print("YES")
    else:
        # Check all possible single swaps
        swapped = False
        # Swap first and second
        temp = list(s)
        temp[0], temp[1] = temp[1], temp[0]
        if ''.join(temp) == 'abc':
            swapped = True
        # Swap first and third
        temp = list(s)
        temp[0], temp[2] = temp[2], temp[0]
        if ''.join(temp) == 'abc':
            swapped = True
        # Swap second and third
        temp = list(s)
        temp[1], temp[2] = temp[2], temp[1]
        if ''.join(temp) == 'abc':
            swapped = True
        print("YES" if swapped else "NO")