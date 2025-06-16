def is_prime(num: int) -> bool:
    """Helper function to determine if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci_generator():
    """Generator function to yield Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_fib(n: int) -> int:
    """Main function to find the n-th prime Fibonacci number."""
    # Initialize a counter for prime Fibonacci numbers
    prime_fib_count = 0
    # Initialize the Fibonacci generator
    fib_gen = fibonacci_generator()
    
    while True:
        # Get the next Fibonacci number
        fib_num = next(fib_gen)
        # Check if the Fibonacci number is prime and non-trivial
        if fib_num > 1 and is_prime(fib_num):
            # Increment the prime Fibonacci number counter
            prime_fib_count += 1
            # If we've found the n-th prime Fibonacci number, return it
            if prime_fib_count == n:
                return fib_num

# Example usage:
# print(prime_fib(1))  # Output: 2
# print(prime_fib(2))  # Output: 3
# print(prime_fib(3))  # Output: 5
# print(prime_fib(4))  # Output: 13
# print(prime_fib(5))  # Output: 89