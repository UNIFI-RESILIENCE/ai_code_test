t = int(input())

for _ in range(t):
    n = int(input())

    # Vanya starts first. Each player alternates moves.
    # A move consists of incrementing or decrementing the current number by 1.
    # Vanya wins if the number is divisible by 3 after any of his moves,
    # within the first 10 moves (i.e., 5 moves for Vanya since players alternate).
    
    found_win = False
    current = n

    # Each move pair constitutes Vanya's and Vova's turn
    for move in range(5):  # Vanya can only make 5 moves (turns 1, 3, 5, 7, 9)
        # Set of possible values after Vanya's move
        possible_values = {current - 1, current + 1}

        # Check if any leads to a win for Vanya
        if any(x % 3 == 0 for x in possible_values):
            found_win = True
            break

        # Vova's optimal move is to avoid Vanya winning by next move
        best_next = []
        # Try all Vova's moves to find one that prevents Vanya from winning next turn
        for vova_move in possible_values:
            next_after_vova = {vova_move - 1, vova_move + 1}
            # If all possible next moves make Vanya lose, it's good for Vova
            if not any(x % 3 == 0 for x in next_after_vova):
                best_next.append(vova_move)

        if best_next:
            # Vova picks a move that stalls Vanya
            current = best_next[0]
        else:
            # No available safe move for Vova, choose arbitrarily (Vanya likely wins soon)
            current = possible_values.pop()

    if found_win:
        print("First")  # Vanya wins
    else:
        print("Second")  # Vova wins after 10 moves without Vanya winning