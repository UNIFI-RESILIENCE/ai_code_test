def theMaximumAchievableX(num: int, t: int) -> int:
    # The goal is to determine the maximum achievable value of x such that x equals num
    # after performing up to t operations.
    # Each operation allows us to either increase or decrease x and num simultaneously by 1.

    # The key insight is that since both x and num are allowed to move, the value of x can diverge
    # from num by at most 2 units per operation (x increases by 1 while num decreases by 1, and vice versa).

    # Hence, the furthest x can be from num and still reach it in t steps is 2 * t.

    return num + 2 * t  # Maximum x such that x can become equal to num after t operations.