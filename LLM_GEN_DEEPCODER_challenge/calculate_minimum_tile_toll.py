Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

a = Sx + Sy
b = Sx - Sy
c = Tx + Ty
d = Tx - Ty

if a == c and b == d:
    print(0)
else:
    if (abs(a - c) + abs(b - d)) <= 3 or abs(a - c) == abs(b - d):
        print(1)
    else:
        if (a + b + c - d) % 2 == 0 or (a - b + c + d) % 2 == 0:
            print(2)
        else:
            if abs(a - c) + abs(b - d) <= 6 or abs((a - c) - (b - d)) <= 3 or abs((a - c) + (b - d)) <= 3 or abs(a - c) <= 5 or abs(b - d) <= 5:
                print(2)
            else:
                print(3)