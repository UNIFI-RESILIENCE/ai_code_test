def max_product_after_increment(digits):
    max_product = 0
    for i in range(len(digits)):
        temp = digits[:]
        temp[i] += 1
        product = 1
        for d in temp:
            product *= d
        max_product = max(max_product, product)
    return max_product

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_product_after_increment(a))