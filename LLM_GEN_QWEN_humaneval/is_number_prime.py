def is_prime(n):
    # Handle cases for numbers less than or equal to 1
    if n <= 1:
        return False
    # Handle the special case for 2, which is the only even prime number
    if n == 2:
        return True
    # Eliminate even numbers greater than 2
    if n % 2 == 0:
        return False
    # Check for factors up to the square root of n
    # This is because a larger factor of n must be a multiple of a smaller factor that is less than or equal to the square root of n
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

# Metadata dictionary (not used in the function but included as per the prompt)
METADATA = {}

# Check function to validate the correctness of the is_prime function
def check(candidate):
    assert candidate(6) == False, "6 is not a prime number"
    assert candidate(101) == True, "101 is a prime number"
    assert candidate(11) == True, "11 is a prime number"
    assert candidate(13441) == True, "13441 is a prime number"
    assert candidate(61) == True, "61 is a prime number"
    assert candidate(4) == False, "4 is not a prime number"
    assert candidate(1) == False, "1 is not a prime number"
    assert candidate(5) == True, "5 is a prime number"
    assert candidate(11) == True, "11 is a prime number"
    assert candidate(17) == True, "17 is a prime number"
    assert candidate(5 * 17) == False, "85 is not a prime number"
    assert candidate(11 * 7) == False, "77 is not a prime number"
    assert candidate(13441 * 19) == False, "255379 is not a prime number"

# Run the check function to validate the implementation
check(is_prime)