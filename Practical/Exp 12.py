board = [" "] * 9
def display():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
def check_winner(p):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(
        all(board[i] == p for i in line)
        for line in wins
    )
player = "X"
moves = 0
while moves < 9:
    display()
    pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position!")
        continue
    board[pos] = player
    moves += 1
    if check_winner(player):
        display()
        print("Player", player, "wins!")
        break
    player = "O" if player == "X" else "X"
else:
    display()
    print("It's a draw!")
