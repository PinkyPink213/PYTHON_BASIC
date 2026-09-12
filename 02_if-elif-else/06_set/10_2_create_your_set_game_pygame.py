"""Upgrade 08_2_create_your_set_game.py ของเราเป็น Pygame.

เปิด 3 หน้าต่าง: 08_2 = เกม Terminal ของเรา, 09/10_1 = Reference,
ไฟล์นี้ = พื้นที่ Convert
COPY Sets/operations, LOOK Card click, TYPE ด้วยมือ, REPLACE input/print
และ RUN CHECKPOINT ทุก STEP ห้ามสร้าง List/Dictionary ไว้จำสิ่งที่เลือก
"""
import pygame

# STEP 1 COPY: Sets, สมาชิก, required values และกติกาจาก 08_2
# TODO/RUN CHECKPOINT: print Set แล้วข้อมูลต้องตรง Terminal
# STEP 2 LOOK/TYPE: ดู Card/Rect ใน 09/10_1 แล้วสร้าง Card ของเรา
# RUN CHECKPOINT: เห็น Card ครบโดยยังไม่ต้องคลิกได้
# STEP 3 TYPE: click เพื่อ add()/discard() และอ่านสีจาก membership
# RUN CHECKPOINT: click ซ้ำเอาออกและไม่มีสมาชิกซ้ำ
# STEP 4 COPY LOGIC: ใช้ union/intersection/difference เดิมตรวจผล
# RUN CHECKPOINT: ผลทุกกรณีตรง Terminal
# ห้ามใช้ Dictionary เพราะจะเรียนใน Chapter 07

pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 34)
# TODO: คัดลอก candidates และ selected จาก 08_2
candidates = ("one", "two", "three")
selected = set()
message = "Click cards to add unique members"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: ใช้ click กับ add()/discard() จากกติกาเดิม
    screen.fill((25, 35, 65))
    screen.blit(font.render(message, True, "white"), (180, 260))
    screen.blit(font.render("Selected: " + str(selected), True, "white"), (180, 330))
    pygame.display.flip()
pygame.quit()

# CHECKPOINT: สีของ Card ต้องอ่านจาก membership ใน selected ไม่ใช่ข้อมูลซ้ำอีกชุด
# TEST: [ ] add [ ] click ซ้ำเอาออก [ ] ไม่ซ้ำ [ ] union/difference เดิมถูกต้อง
# DONE: selected ชุดเดียวควบคุมทั้งผลเกมและสี Card
# TRANSFER: ออกแบบทีม/collection ใหม่และภารกิจที่ต้องใช้ intersection/difference
# CREATIVE GAME RULES: ผู้เล่นต้องรวบรวมอะไร ___ ห้ามมีอะไร ___ ชนะเมื่อ ___
# TODO: สร้างกติกาใหม่ด้วย Set operation 1 ข้อ และให้ UI แสดงผลกติกานั้น
# ระบุ SET DATA ___ / OPERATION ___ / EVENT ___ / DRAW ___ ก่อนทำ
# DESIGN NOTE: Set ป้องกัน ___ และกติกาใหม่ใช้ operation ___
