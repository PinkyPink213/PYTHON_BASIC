"""Milestone: Upgrade Tic-Tac-Toe จาก Terminal เป็น Pygame

สิ่งที่ยังเหมือนเกมเดิม:
- ``board`` เก็บ X/O, ``player`` เก็บคนที่กำลังเล่น และ Functions ตรวจผลเกม

สิ่งที่เปลี่ยนเป็น Pygame:
- input row/column → ตำแหน่ง mouse click
- print board/status → เส้น ตาราง ตัวอักษร และข้อความบนหน้าจอ

ให้นักเรียนหยุดที่ CHECKPOINT ทายค่าก่อน Run แล้วชี้ DATA/EVENT/DRAW ให้ได้
"""
import pygame


def make_board():
    """คืนกระดานว่าง 3 แถว แต่ละแถวมี 3 ช่อง."""
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def check_winner(board, player):
    """ตรวจ 8 เส้นที่ชนะ แล้วคืน True เมื่อ player เรียงครบสามช่อง."""
    # แนวนอน 3 แถว
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    # แนวตั้ง 3 คอลัมน์
    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True

    # แนวทแยงมีเพียง 2 เส้น จึงเขียนให้เห็นตำแหน่งชัด ๆ
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def board_is_full(board):
    """คืน True เมื่อหา space ไม่เจอเลย ใช้ตรวจผลเสมอ."""
    for row in range(3):
        for column in range(3):
            if board[row][column] == " ":
                return False
    return True


# SETUP — ทำครั้งเดียวก่อนเข้า Game Loop
pygame.init()
screen = pygame.display.set_mode((700, 750))
pygame.display.set_caption("Tic-Tac-Toe Pygame")
symbol_font = pygame.font.Font(None, 110)
text_font = pygame.font.Font(None, 34)
clock = pygame.time.Clock()

# DATA — ค่าที่บอกสถานะจริงของเกมในขณะนี้
board = make_board()
player = "X"
game_over = False
message = "X's turn — click an empty square"
scores = {"X": 0, "O": 0}

running = True
while running:
    # EVENT — รับคำสั่งจากผู้เล่น แต่ยังไม่วาดอะไร
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # กด R สร้างข้อมูลรอบใหม่ คะแนนรวมยังอยู่
            board = make_board()
            player = "X"
            game_over = False
            message = "New round — X's turn"

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # ตารางเริ่มที่ (80, 80) และหนึ่งช่องกว้าง/สูง 180 pixels
            # ลบขอบ 80 ก่อน แล้ว // 180 เปลี่ยน pixel เป็นเลข 0, 1 หรือ 2
            column = (mouse_x - 80) // 180
            row = (mouse_y - 80) // 180

            # ตรวจว่าคลิกอยู่ในกระดานและช่องนั้นยังว่าง ก่อนบันทึก X/O
            inside_board = row in range(3) and column in range(3)
            if inside_board and board[row][column] == " ":
                board[row][column] = player

                # ต้องตรวจคนปัจจุบันก่อนสลับ player ไม่เช่นนั้นจะตรวจผิดคน
                if check_winner(board, player):
                    scores[player] += 1
                    message = player + " WINS! Press R to restart"
                    game_over = True
                elif board_is_full(board):
                    message = "DRAW! Press R to restart"
                    game_over = True
                elif player == "X":
                    player = "O"
                    message = "O's turn"
                else:
                    player = "X"
                    message = "X's turn"

    # CHECKPOINT: ก่อนอ่านต่อ ลองบอกค่า board, player และ game_over ตอนนี้

    # DRAW — อ่าน DATA ล่าสุดแล้วสร้างภาพหนึ่ง frame
    screen.fill((25, 31, 62))

    # วาดเส้น 4 แนวนอนและ 4 แนวตั้งเป็นตาราง 3×3
    for index in range(4):
        line_position = 80 + index * 180
        pygame.draw.line(screen, (90, 210, 240), (80, line_position), (620, line_position), 5)
        pygame.draw.line(screen, (90, 210, 240), (line_position, 80), (line_position, 620), 5)

    # วาดค่าจาก nested List ลงกลางช่องที่ตรงกัน
    for row in range(3):
        for column in range(3):
            symbol = board[row][column]
            color = (255, 210, 80)
            if symbol == "O":
                color = (245, 120, 170)
            symbol_image = symbol_font.render(symbol, True, color)
            center_x = 170 + column * 180
            center_y = 170 + row * 180
            screen.blit(symbol_image, symbol_image.get_rect(center=(center_x, center_y)))

    status_image = text_font.render(message, True, "white")
    score_text = "Score  X: " + str(scores["X"]) + "   O: " + str(scores["O"])
    score_image = text_font.render(score_text, True, (255, 220, 100))
    screen.blit(status_image, status_image.get_rect(center=(350, 665)))
    screen.blit(score_image, score_image.get_rect(center=(350, 710)))

    # flip() นำ frame ที่วาดเสร็จขึ้นจอ; tick() จำกัดความเร็ว Loop
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Exit ticket
# 1. board คือ Game Data หรือ Interface?
# 2. เพราะอะไรต้องตรวจช่องว่างก่อนเขียน board[row][column]?
# 3. ถ้าสลับ player ก่อน check_winner จะเกิด bug อย่างไร?
# 4. กด R แล้วค่าใด reset และค่าใดยังคงอยู่?
