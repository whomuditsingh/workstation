import numpy as np

# --- GLOBAL DATA TRACKING ---
# 4 Players, 3 Columns: [Wins, Losses, Draws]
scoreboard = np.zeros((4, 3), dtype=int)

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    # Row/Col check
    if np.any(np.all(board == player, axis=1)) or \
       np.any(np.all(board == player, axis=0)):
        return True
    # Diagonal checks
    if np.all(np.diag(board) == player) or \
       np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def update_stats(p1_idx, p2_idx, winner_symbol, is_draw):
    global scoreboard
    if is_draw:
        scoreboard[[p1_idx, p2_idx], 2] += 1
    else:
        # If 'X' won, p1 gets a win, p2 gets a loss. vice versa.
        if winner_symbol == 'X':
            scoreboard[p1_idx, 0] += 1
            scoreboard[p2_idx, 1] += 1
        else:
            scoreboard[p2_idx, 0] += 1
            scoreboard[p1_idx, 1] += 1

def play_game():
    print("--- LEAGUE SELECTION ---")
    print("Available Player IDs: 0, 1, 2, 3")
    try:
        p1 = int(input("Enter Player ID for X: "))
        p2 = int(input("Enter Player ID for O: "))
    except ValueError:
        print("Invalid ID. Defaulting to 0 and 1.")
        p1, p2 = 0, 1

    board = np.full((3, 3), " ", dtype='U1')
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter move (row col): ").split()
            r, c = map(int, move)
            if board[r, c] != " ":
                print("Occupied!")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Use 0, 1, or 2.")
            continue

        board[r, c] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Tournament Update: Player {current_player} Wins!")
            update_stats(p1, p2, current_player, False)
            break
        
        if not np.any(board == " "):
            print_board(board)
            print("It's a Draw!")
            update_stats(p1, p2, None, True)
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        play_game()
        print("\n--- CURRENT LEAGUE STANDINGS ---")
        print("ID | Wins | Losses | Draws")
        for i, row in enumerate(scoreboard):
            print(f"{i}  | {row[0]}    | {row[1]}      | {row[2]}")
        
        cont = input("\nPlay another match? (y/n): ").lower()
        if cont != 'y':
            print("Goodbye!")
            break