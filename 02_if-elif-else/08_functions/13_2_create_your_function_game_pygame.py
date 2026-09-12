"""Upgrade 11_2_create_your_function_game.py ของเราเป็น Pygame.

เปิด 3 หน้าต่าง: 11_2 = เกม Terminal ของเรา, 12/13_1 = Reference,
ไฟล์นี้ = พื้นที่ Convert
COPY game-logic Functions โดยไม่แก้ก่อน, LOOK UI Functions, TYPE ด้วยมือ,
REPLACE input ด้วย event และ print ด้วย draw Function แล้ว RUN CHECKPOINT ทุก STEP
"""
import pygame

# STEP 1 COPY: game logic Functions จาก 11_2 โดยยังไม่แก้
# TODO/RUN CHECKPOINT: เรียก Function ด้วย test values แล้ว return ต้องตรง Terminal
# STEP 2 LOOK/TYPE: ดู 12/13_1 แล้วเปลี่ยน input เป็น event/button Function
# RUN CHECKPOINT: click หนึ่งครั้งเรียก logic หนึ่งครั้ง
# STEP 3 LOOK/TYPE: เปลี่ยน print เป็น draw_text()/draw_button()
# RUN CHECKPOINT: UI แสดง return ล่าสุดโดยไม่เปลี่ยน logic
# STEP 4 TYPE: แยก Function ที่ update ข้อมูลออกจาก Function ที่ draw
# RUN CHECKPOINT: เปลี่ยนสี UI ได้โดยผลเกมไม่เปลี่ยน
# STEP 5 COPY: เชื่อม Creative Features เดิมของเกมเราเข้ากับ UI
# RUN CHECKPOINT: เล่นทุกเส้นทางจนจบและปิดหน้าต่างได้

pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 34)

def draw_text(text, position, color="white"):
    """UI function: วาดข้อความ แต่ไม่เปลี่ยนกติกาเกม."""
    screen.blit(font.render(text, True, color), position)

message = "Move logic functions from 11_2 here"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: เรียก game logic Function เดิมเมื่อผู้เล่นคลิก
    screen.fill((25, 35, 65))
    draw_text(message, (150, 280))
    pygame.display.flip()
pygame.quit()

# CHECKPOINT: Function ใดเปลี่ยน DATA และ Function ใด DRAW อย่างเดียว?
# TEST: [ ] เรียก logic แล้ว return ถูก [ ] click เรียกครั้งเดียว [ ] UI อ่านผลล่าสุด
# DONE: เปลี่ยนหน้าตาได้โดยไม่แก้ logic และเปลี่ยนกติกาได้โดยไม่แก้ draw Function
# TRANSFER: เพิ่ม game mechanic หนึ่ง Function และ UI component หนึ่ง Function
# CREATIVE GAME RULES: เป้าหมาย ___ ผู้เล่นตัดสินใจอะไร ___ ชนะ/แพ้อย่างไร ___
# TODO: ออกแบบ mechanic ใหม่ 1 Function: รับค่า ___ return ___ เปลี่ยนเกมอย่างไร ___
# TODO: ออกแบบ UI Function 1 ตัวเพื่อทำให้ผู้เล่นมองเห็นผลของ mechanic นั้น
# DESIGN NOTE: logic Function รับ ___ return ___; UI Function แสดง ___
