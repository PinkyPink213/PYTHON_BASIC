"""Upgrade 07_2_create_your_tuple_game.py ของเราเป็น Pygame.

เปิด 3 หน้าต่าง: 07_2 = เกม Terminal ของเรา, 08/09_1 = Reference,
ไฟล์นี้ = พื้นที่ Convert
COPY Tuple/conditions, LOOK click/draw, TYPE ด้วยมือ, REPLACE input/print
และ RUN CHECKPOINT ทุก STEP
"""
import pygame

# STEP 1 COPY: Tuple ข้อมูลคงที่และเงื่อนไขจาก 07_2
# TODO/RUN CHECKPOINT: print Tuple แล้วข้อมูลต้องตรง Terminal
# STEP 2 LOOK/TYPE: ดูพิกัดใน 08/09_1 แล้วเพิ่ม (x, y) ให้จุดของเรา
# RUN CHECKPOINT: วาดจุดครบและทายตำแหน่งก่อนดูหน้าจอ
# STEP 3 TYPE: unpack แล้ววาดแต่ละจุดใน Game Loop
# RUN CHECKPOINT: เปลี่ยน Tuple หนึ่งค่าแล้วภาพเปลี่ยนจากแหล่งข้อมูลเดียว
# STEP 4 LOOK/TYPE: ใช้ Rect/collidepoint ตรวจจุดที่คลิก
# RUN CHECKPOINT: click โดน/พลาดไม่ crash
# STEP 5 COPY LOGIC: เปลี่ยน print ตอนจบเดิมเป็นข้อความบนหน้าจอ
# RUN CHECKPOINT: ผลทุกเส้นทางตรงกับ Terminal

pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 34)
# TODO: แทนที่ด้วย Tuple จาก 07_2 และเพิ่มพิกัด (x, y)
places = (("place 1", (220, 280)), ("place 2", (450, 180)), ("place 3", (680, 330)))
message = "Click a place from your tuple"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # TODO: ใช้ for/unpack ตรวจตำแหน่ง แล้วใช้ตอนจบเดิมจาก 07_2
            message = "Mouse: " + str(event.pos)
    screen.fill((20, 28, 60))
    for name, position in places:
        pygame.draw.circle(screen, (105, 205, 245), position, 45)
        screen.blit(font.render(name, True, "white"), (position[0] - 45, position[1] + 60))
    screen.blit(font.render(message, True, "white"), (220, 520))
    pygame.display.flip()
pygame.quit()

# CHECKPOINT: Tuple คือ DATA; วงกลม/ข้อความคือ DRAW ของข้อมูลชุดเดิม
# TEST: [ ] ทุกจุดเห็นได้ [ ] click ตรง [ ] click พลาดไม่ crash [ ] ตอนจบเดิม
# DONE: เปลี่ยน Tuple หนึ่งค่าแล้ว UI เปลี่ยนโดยไม่แก้ข้อมูลซ้ำ
# TRANSFER: ออกแบบแผนที่ใหม่ 3–4 จุดและตอนจบพิเศษจากพิกัดหนึ่งจุด
# CREATIVE GAME RULES: ภารกิจ ___ อุปสรรค ___ ชนะ ___ แพ้ ___
# TODO: เพิ่มกติกาจากตำแหน่ง 1 ข้อ เช่น เขตอันตราย/จุดลับ/เส้นชัย
# ระบุ Tuple DATA ___ / click LOGIC ___ / DRAW ___ ก่อนลงมือ
# DESIGN NOTE: Tuple ของฉันเก็บ ___ และ click จุด ___ ทำให้ ___
