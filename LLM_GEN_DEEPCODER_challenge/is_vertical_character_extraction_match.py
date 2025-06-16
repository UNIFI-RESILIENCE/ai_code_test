S, T = input().split()
len_S = len(S)
len_T = len(T)
found = False

for w in range(1, len_S):  # w must be < |S|
    for c in range(1, w + 1):  # 1 <= c <= w
        parts = []
        # Split S into parts of length w
        for i in range(0, len_S, w):
            part = S[i:i + w]
            parts.append(part)
        
        # Extract c-th character from each part with length >= c
        generated_T = []
        for part in parts:
            if len(part) >= c:
                generated_T.append(part[c - 1])
        
        # Compare generated string with T
        if ''.join(generated_T) == T:
            found = True
            break
    if found:
        break

print("Yes" if found else "No")