from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    # Start with the smallest prime number
    divisor = 2
    
    # Continue dividing n by the current divisor until n becomes 1
    while n > 1:
        # Check if the current divisor divides n without a remainder
        while n % divisor == 0:
            factors.append(divisor)  # Add the divisor to the factors list
            n //= divisor          # Divide n by the current divisor
        divisor += 1  # Move to the next potential divisor
    
    return factors