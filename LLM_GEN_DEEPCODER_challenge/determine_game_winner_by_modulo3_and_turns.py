t = int(input())
for _ in range(t):
    n = int(input())
    # The key observation is that Vanya wins if (n mod 3) is 1 on his first move,
    # or if the game lasts until the 9th move (since players alternate, 10 moves total).
    # Otherwise, Vova can force a win.
    if n % 3 == 1:
        print("First")
    else:
        # Even if (n mod 3) is not 1 initially, Vanya can win if after his first move,
        # (n ±1) mod 3 is 1, but Vova can counter optimally. The only way Vanya can win
        # is if the total moves reach 9 (his 5th move) without n being divisible by 3.
        # Due to optimal play, Vanya can only win if (n mod 3) is 1 initially, or if after the
        # first move (n mod 3) becomes 1, but Vova can block further attempts.
        # Hence, the result depends solely on initial (n mod 3).
        print("Second")