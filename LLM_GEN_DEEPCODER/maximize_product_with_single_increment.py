t = int(input())
for _ in range(t):
    n = int(input())
    digits = list(map(int, input().split()))
    max_product = 0
    for i in range(n):
        # Create a copy of the original digits
        modified = digits.copy()
        modified[i] += 1
        product = 1
        for d in modified:
            product *= d
        if product > max_product:
            max_product = product
    print(max_product)