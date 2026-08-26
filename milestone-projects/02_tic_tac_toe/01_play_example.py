"""เกมตัวอย่างสมบูรณ์: Tic-Tac-Toe"""

# ==================================================
# เกมนี้คืออะไร?
# ==================================================
# Tic-Tac-Toe เป็นเกมกระดาน 3×3 สำหรับผู้เล่น 2 คน
# ผู้เล่น X และ O ผลัดกันเลือกแถวและคอลัมน์เพื่อวางสัญลักษณ์
# คนแรกที่เรียงสัญลักษณ์ครบ 3 ช่องในแนวนอน แนวตั้ง หรือแนวทแยงชนะ
# ถ้ากระดานเต็มโดยไม่มีใครเรียงครบ เกมจะจบแบบเสมอ

# เป้าหมาย:
# วางสัญลักษณ์ของตัวเองให้ครบ 3 ช่องใน Winning Line ก่อนอีกฝ่าย


# ==================================================
# Features ของเกม
# ==================================================
# - กระดาน 3×3 ที่แสดงหมายเลขแถวและคอลัมน์
# - ผู้เล่น X และ O ผลัดกันเล่นอัตโนมัติ
# - ป้องกันการเลือกตำแหน่งเดิมซ้ำ
# - ตรวจตำแหน่งนอกกระดานและ Input ที่ไม่ใช่ตัวเลข
# - ตรวจ Winning Lines ทั้ง 8 แบบ
# - ตรวจผลชนะและผลเสมอ
# - เก็บคะแนนผู้ชนะใน Dictionary


# ==================================================
# Flow ของเกม
# ==================================================
# START -> สร้างกระดานว่างและเริ่มด้วย Player X
#   |
#   v
# แสดงกระดาน -> รับ row และ column
#   |-- ไม่ใช่เลข ------> แจ้ง Error แล้วถามใหม่
#   |-- นอกกระดาน -----> แจ้งเตือน แล้วถามใหม่
#   |-- ช่องถูกใช้แล้ว -> แจ้งเตือน แล้วถามใหม่
#   +-- ช่องว่าง -------> วาง X หรือ O
#                           |
#                           v
#                เรียงครบ 3? -> WIN
#                กระดานเต็ม? -> DRAW
#                ยังไม่จบ? --> เปลี่ยนผู้เล่นและเล่นต่อ


# ==================================================
# ความรู้จาก 8 Chapters ที่ใช้
# ==================================================
# Basic: Variables, Input, Casting และ String Manipulation
# If-Elif-Else: ตรวจตำแหน่ง ผู้ชนะ และเปลี่ยนผู้เล่น
# Lists: Nested List เป็นกระดาน 3×3
# Loops: for วาด/ตรวจกระดาน และ while ควบคุมเกม
# Tuples: เก็บพิกัด Winning Lines ที่ไม่ต้องเปลี่ยน
# Sets: เก็บตำแหน่งที่ถูกใช้แล้วโดยไม่ซ้ำ
# Dictionaries: เก็บคะแนนของ X และ O
# Functions: แยกสร้างกระดาน แสดงกระดาน ตรวจผู้ชนะ และเล่นเกม
# Error Handling: try-except รับมือ Input ที่ไม่ใช่จำนวนเต็ม

WINNING_LINES = (
    ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
)


def create_board():
    return [[" " for column in range(3)] for row in range(3)]


def show_board(board):
    print("\n    1   2   3")
    for index, row in enumerate(board):
        print(str(index + 1) + " | " + " | ".join(row) + " |")
        if index < 2:
            print("  |---+---+---|")


def has_won(board, symbol):
    for line in WINNING_LINES:
        if all(board[row][column] == symbol for row, column in line):
            return True
    return False


def play_game():
    board = create_board()
    current_player = "X"
    used_positions = set()
    scores = {"X": 0, "O": 0}

    print("╔══════════════════════╗")
    print("║    TIC-TAC-TOE       ║")
    print("╚══════════════════════╝")

    while len(used_positions) < 9:
        show_board(board)
        try:
            row = int(input("Player " + current_player + " row (1-3): ")) - 1
            column = int(input("Player " + current_player + " column (1-3): ")) - 1

            if row not in range(3) or column not in range(3):
                print("Choose numbers from 1 to 3.")
            elif (row, column) in used_positions:
                print("That square is already used.")
            else:
                board[row][column] = current_player
                used_positions.add((row, column))

                if has_won(board, current_player):
                    scores[current_player] += 1
                    show_board(board)
                    print("★ PLAYER " + current_player + " WINS! ★")
                    print("Scores: " + str(scores))
                    return

                current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Please enter whole numbers.")

    show_board(board)
    print("DRAW! The board is full.")


play_game()
