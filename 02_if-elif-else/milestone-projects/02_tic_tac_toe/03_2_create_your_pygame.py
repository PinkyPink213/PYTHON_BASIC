"""สร้าง Pygame Tic-Tac-Toe ของเรา — ทำ STEP ตรงกับ 03_1

เปิด 3 หน้าต่าง: 02_create_your_game.py = Terminal ของเรา,
03_1_play_pygame.py = Reference, ไฟล์นี้ = พื้นที่ Convert
COPY board/functions/rules, LOOK ตัวอย่าง, TYPE ใหม่ด้วยมือ,
REPLACE input/print และ RUN CHECKPOINT ทุก STEP
"""
import pygame


# ==================================================
# STEP 1 — make_board() (ตรงกับ Function แรกใน 03_1)
# ==================================================
def make_board():
    """คืน Nested List 3×3; ใช้ DATA รูปแบบเดียวกับ Terminal Version."""
    # TODO: คัดลอก create_board()/new_board() จากไฟล์ 02 ของเรา
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# RUN CHECKPOINT: print board แล้วต้องเป็น 3 แถว แถวละ 3 ช่อง


# ==================================================
# STEP 2 — check_winner() (ตรงกับ Function ที่สองใน 03_1)
# ==================================================
def check_winner(board, player):
    """TODO: ตรวจแนวนอน แนวตั้ง และแนวทแยงจาก logic เดิม."""
    # คัดลอก has_won() หรือ Winning Lines จาก Terminal Version
    # เปลี่ยนชื่อ Function ได้ แต่ห้ามเปลี่ยนกติกาชนะ



    # False ชั่วคราวทำให้ starter Run ได้ ให้แทนด้วย logic ของเรา
    return False
# RUN CHECKPOINT: สร้าง Test Board แนวนอน/ตั้ง/ทแยง แล้วทาย True/False ก่อน Run


# ==================================================
# STEP 3 — board_is_full() (ตรงกับ Function ที่สามใน 03_1)
# ==================================================
def board_is_full(board):
    """TODO: return True เมื่อไม่มีช่องว่าง ใช้ตรวจ Draw."""
    # ใช้ nested for ตรวจ board[row][column]



    return False
# RUN CHECKPOINT: Test Board ว่างต้อง False และ Board เต็มต้อง True


# ==================================================
# STEP 4 — SETUP
# ==================================================
pygame.init()
screen = pygame.display.set_mode((700, 750))
pygame.display.set_caption("My Tic-Tac-Toe")
symbol_font = pygame.font.Font(None, 110)
text_font = pygame.font.Font(None, 34)
clock = pygame.time.Clock()

# TODO: เลือกสี/ชื่อเกมให้ตรงกับ Theme ที่ออกแบบ
background_color = (25, 31, 62)
grid_color = (90, 210, 240)
x_color = (255, 210, 80)
o_color = (245, 120, 170)
# RUN CHECKPOINT: หน้าต่างต้องเปิด สีอ่านง่าย และยังไม่มีเกม logic ใน DRAW


# ==================================================
# STEP 5 — GAME STATE
# ==================================================
board = make_board()
player = "X"
game_over = False
message = "X's turn — click an empty square"
scores = {"X": 0, "O": 0}

# RUN CHECKPOINT: ค่าใด reset ทุกรอบ และค่าใดต้องเก็บหลายรอบ?


# ==================================================
# STEP 6 — GAME LOOP: EVENT + MOUSE → ROW/COLUMN
# ==================================================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TODO 6A: กด R แล้ว reset board/player/game_over/message
        # อย่า reset scores เพราะเป็นคะแนนรวมหลายรอบ



        # TODO 6B: รับ mouse click เมื่อ game_over เป็น False
        # Pattern จาก 03_1:
        # mouse_x = event.pos[0]
        # mouse_y = event.pos[1]
        # column = (mouse_x - 80) // 180
        # row = (mouse_y - 80) // 180



        # TODO 6C: ตรวจขอบเขตและ board[row][column] == " "
        # จากนั้นเขียน player ลง board จุดเดียวกับ Terminal Version



        # TODO 6D: เรียก check_winner(), board_is_full() และสลับ player
        # Win: เพิ่ม scores[player], ตั้ง game_over และ message
        # Draw: ตั้ง game_over และ message
        # ยังไม่จบ: สลับ X/O
# RUN CHECKPOINT: click ใน/นอก/ช่องซ้ำ แล้ว board เปลี่ยนเฉพาะ click ที่ถูกต้อง



    # ==================================================
    # STEP 7 — DRAW GRID (ใช้ draw.line ที่ฝึกใน Chapter 01)
    # ==================================================
    screen.fill(background_color)

    # เส้น 4 แนวนอน + 4 แนวตั้ง สร้างช่อง 3×3
    for index in range(4):
        line_position = 80 + index * 180
        pygame.draw.line(screen, grid_color, (80, line_position), (620, line_position), 5)
        pygame.draw.line(screen, grid_color, (line_position, 80), (line_position, 620), 5)


    # ==================================================
    # STEP 8 — DRAW SYMBOLS + STATUS
    # ==================================================
    # TODO: nested for อ่าน board[row][column]
    # render X/O และวางกลางช่องด้วยสูตร center_x/center_y จาก 03_1



    # TODO: render message และ Score X/O ใต้กระดาน
    status_image = text_font.render(message, True, "white")
    screen.blit(status_image, status_image.get_rect(center=(350, 675)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# RUN CHECKPOINT: เล่น Win ทั้ง 3 แนวและ Draw ได้โดยหน้าต่างไม่ดับก่อนจบ


# ==================================================
# STEP 9 — TEST เทียบ Terminal → Pygame
# ==================================================
# [ ] click แต่ละช่องแล้วได้ row/column ถูก
# [ ] ช่องเดิมถูกปฏิเสธและไม่สลับ player
# [ ] click นอกกระดานไม่ทำให้ Error
# [ ] X/O สลับหลังเดินสำเร็จเท่านั้น
# [ ] ชนะครบแนวนอน แนวตั้ง และแนวทแยง
# [ ] กระดานเต็มไม่มีผู้ชนะเป็น Draw
# [ ] กด R reset กระดาน แต่ scores ยังอยู่
# [ ] ผลการตัดสินเหมือน Terminal Version


# ==================================================
# STEP 10 — CREATIVE STUDIO
# ==================================================
# เขียนก่อนทำ: เกมชื่อ ______ ผู้เล่นคือ ______ จุดเด่นคือ ______
# เลือกอย่างน้อย 2 ข้อหลัง Core ผ่าน:
# [ ] เปลี่ยน X/O เป็นทีม สัตว์ เวทมนตร์ หรือสัญลักษณ์ของเรา
# [ ] ใช้ asset, palette และข้อความให้เป็น Theme เดียวกัน
# [ ] รับชื่อผู้เล่นและแสดง Scoreboard
# [ ] highlight เส้นที่ชนะ
# [ ] เพิ่มกติกาพิเศษ พร้อมบอกว่าแก้ DATA/logic/UI ส่วนใด
# CREATIVE GAME RULES: เป้าหมาย ___ ผู้เล่นตัดสินใจอะไร ___ ความเสี่ยง ___
# [ ] กติกาใหม่ต้องมีผลต่อการเล่นจริง เช่น Block 1 ช่อง หรือ Bonus Turn 1 ครั้ง
# [ ] เขียนก่อนทำว่าแก้ DATA ___ / LOGIC FUNCTION ___ / EVENT ___ / DRAW ___

# อธิบายผลงาน:
# DATA ที่ฉันออกแบบคือ ____________________
# Logic ที่ฉันเพิ่มคือ ____________________
# UI ที่ฉันเปลี่ยนคือ ____________________
# TRANSFER: ให้เพื่อนเล่นโดยไม่อธิบาย แล้วปรับข้อความ/Reaction จากสิ่งที่เพื่อนงง
