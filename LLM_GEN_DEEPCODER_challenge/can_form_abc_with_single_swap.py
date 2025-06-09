t = int(input())
for _ in range(t):
    s = input().strip()
    # The target is 'abc'
    if s == 'abc':
        print("YES")
    else:
        # Check if swapping any two characters can result in 'abc'
        # There are 3 possible swaps for a 3-letter string
        swapped1 = s[1] + s[0] + s[2]  # swap first and second
        swapped2 = s[0] + s[2] + s[1]  # swap second and third
        swapped3 = s[2] + s[1] + s[0]  # swap first and third
        if swapped1 == 'abc' or swapped2 == 'abc' or swapped3 == 'abc':
            print("YES")
        else:
            print("NO")