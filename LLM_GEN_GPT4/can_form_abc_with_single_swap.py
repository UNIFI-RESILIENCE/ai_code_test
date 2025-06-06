t = int(input())
for _ in range(t):
    s = input().strip()
    if s == "abc" or s in ["acb", "bac", "cba"]:
        print("YES")
    else:
        print("NO")