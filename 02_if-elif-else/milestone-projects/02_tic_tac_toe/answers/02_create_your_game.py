"""ตัวอย่างผลงาน: Magic Tic-Tac-Toe"""

WINNING_LINES = (
    ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
)


def new_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def draw(board):
    print("\n    1   2   3")
    for row_number in range(3):
        print(str(row_number + 1) + "   " + " | ".join(board[row_number]))
        if row_number < 2:
            print("   ---+---+---")


def winner(board, symbol):
    for line in WINNING_LINES:
        line_complete = True
        for row, column in line:
            if board[row][column] != symbol:
                line_complete = False
        if line_complete:
            return True
    return False


def play():
    board = new_board()
    used = set()
    player = "★"
    names = {"★": "Star Wizard", "☾": "Moon Wizard"}

    print("╔════════════════════════╗")
    print("║  MAGIC TIC-TAC-TOE     ║")
    print("╚════════════════════════╝")

    while len(used) < 9:
        draw(board)
        try:
            row = int(input(names[player] + " row: ")) - 1
            column = int(input(names[player] + " column: ")) - 1

            if row not in range(3) or column not in range(3):
                print("Use numbers 1–3.")
            elif (row, column) in used:
                print("That square is taken.")
            else:
                board[row][column] = player
                used.add((row, column))
                if winner(board, player):
                    draw(board)
                    print("✨ " + names[player] + " WINS! ✨")
                    return
                player = "☾" if player == "★" else "★"
        except ValueError:
            print("Enter whole numbers.")

    draw(board)
    print("DRAW — The magic is balanced!")


play()
