import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = map(int, input[ptr:ptr + 2])
        ptr += 2
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        total_mod = 1
        min_operations = float('inf')
        
        # If k == 2, we need any even number
        if k == 2:
            has_even = False
            for num in a:
                if num % 2 == 0:
                    has_even = True
                    break
            if has_even:
                print(0)
            else:
                # Find minimal steps to make any number even (steps = 1 for odd)
                operations = []
                for num in a:
                    if num % 2 != 0:
                        ops = 2 - (num % 2)
                        operations.append(ops)
                min_op = min(operations) if operations else 0
                print(min_op)
        
        elif k == 3:
            # We need at least one number divisible by 3
            min_ops = float('inf')
            for num in a:
                if num % 3 == 0:
                    min_ops = 0
                    break
                else:
                    ops = 3 - (num % 3)
                    if ops < min_ops:
                        min_ops = ops
            print(min_ops)
        
        elif k == 4:
            # Need either:
            # 1. At least two even numbers OR
            # 2. One number divisible by 4 OR
            # Determine minimal steps to satisfy either condition
            count_even = 0
            ops_to_div4 = []
            ops_to_even = []
            min_ops_div4 = float('inf')
            for num in a:
                mod = num % 2
                if mod == 0:
                    count_even += 1
                ops_even = (2 - mod) if mod != 0 else 0
                ops_to_even.append(ops_even)
                
                mod4 = num % 4
                ops_div4 = (4 - mod4) if mod4 != 0 else 0
                ops_to_div4.append(ops_div4)
                if ops_div4 < min_ops_div4:
                    min_ops_div4 = ops_div4
            # Condition 1: need at least two evens
            if count_even >= 2:
                print(0)
            else:
                # Need to make up to two evens
                needed = 2 - count_even
                # Find the smallest ops_to_even to add
                # must sort to get top 'needed' smallest ops
                ops_to_even_sorted = sorted(ops_to_even)
                total_ops = sum(ops_to_even_sorted[:needed])
                # Compare with condition 2: one divisible by 4
                min_total = min(total_ops, min_ops_div4)
                print(min_total)
        
        elif k == 5:
            # Need at least one number divisible by 5
            min_ops = float('inf')
            for num in a:
                if num % 5 == 0:
                    min_ops = 0
                    break
                else:
                    ops = 5 - (num % 5)
                    if ops < min_ops:
                        min_ops = ops
            print(min_ops)

if __name__ == '__main__':
    solve()