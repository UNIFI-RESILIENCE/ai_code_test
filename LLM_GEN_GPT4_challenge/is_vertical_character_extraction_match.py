S, T = input().split()

n = len(S)
found = False

# Try all possible values of w from 1 to n - 1
for w in range(1, n):
    # For each w, try all c such that 1 <= c <= w
    for c in range(1, w + 1):
        parts = [S[i:i + w] for i in range(0, n, w)]  # Split S into substrings of length w
        chars = []

        for part in parts:
            if len(part) >= c:
                chars.append(part[c - 1])  # Extract the c-th character (1-based index)

        if ''.join(chars) == T:
            print("Yes")
            found = True
            break
    if found:
        break

if not found:
    print("No")