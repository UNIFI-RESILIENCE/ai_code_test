import sys

def max_product_after_increment(t, test_cases):
    results = []
    for case in test_cases:
        n, digits = case
        max_product = 0
        
        # Iterate through each digit, increment it by 1, compute product, and track max
        for i in range(n):
            temp_digits = digits.copy()
            temp_digits[i] += 1
            
            product = 1
            for d in temp_digits:
                product *= d
            
            if product > max_product:
                max_product = product
        
        results.append(max_product)
    return results

def main():
    input_lines = sys.stdin.read().split()
    ptr = 0
    t = int(input_lines[ptr])
    ptr += 1
    test_cases = []
    
    for _ in range(t):
        n = int(input_lines[ptr])
        ptr += 1
        digits = list(map(int, input_lines[ptr:ptr + n]))
        ptr += n
        test_cases.append((n, digits))
    
    results = max_product_after_increment(t, test_cases)
    for res in results:
        print(res)

if __name__ == '__main__':
    main()