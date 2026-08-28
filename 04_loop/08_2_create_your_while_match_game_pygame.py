"""Upgrade 06_3_create_your_while_match_game.py ของเราเป็น Pygame.

เปิด 3 หน้าต่าง: 06_3 = เกม Terminal ของเรา, 07/08_1 = Reference,
ไฟล์นี้ = พื้นที่ Convert ของเรา
COPY data/conditions, LOOK EVENT→UPDATE→DRAW, TYPE ใหม่ลงไฟล์นี้,
REPLACE input/print และ RUN CHECKPOINT ทุก STEP
"""
import pygame

# STEP 1 COPY DATA: theme, choices, hints, secret, attempts จาก 06_3
# TODO: พิมพ์ DATA ของเราลงก่อน | RUN CHECKPOINT: print แล้วค่าตรง Terminal
# STEP 2 LOOK/TYPE UI: ดู Rect ใน 08_1 แล้วสร้างปุ่มให้ตรง choices
# RUN CHECKPOINT: เห็นทุกปุ่มและข้อความไม่ซ้อน
# STEP 3 LOOK/TYPE EVENT: ใช้ for event + collidepoint แทน input()
# RUN CHECKPOINT: click หนึ่งครั้งเปลี่ยนคำตอบหนึ่งครั้ง และปิดหน้าต่างได้
# STEP 4 COPY LOGIC: วาง if/elif เดิมหลัง click ห้ามเปลี่ยนกติกาเดิมก่อน
# RUN CHECKPOINT: ผลถูก/ผิด/หมดโอกาสตรง Terminal ทุกกรณี
# STEP 5 TYPE DRAW: เปลี่ยน print เป็น message แล้ว render/blit
# RUN CHECKPOINT: เล่นได้จนจบ แล้วกดเริ่มใหม่ได้ตามแบบ 08_1

pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 34)
message = "Copy the goal and choices from 06_3"
running = True
while running:
    # EVENT: รับการปิดหน้าต่าง/การคลิก
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: ตรวจปุ่มด้วย if/elif แล้วใช้ logic เดิมจาก 06_3

    # UPDATE: TODO ขยับวัตถุหรือเปลี่ยน attempts ตรงนี้

    # DRAW: วาดจากค่าปัจจุบันทุก frame
    screen.fill((25, 35, 65))
    screen.blit(font.render(message, True, "white"), (130, 280))
    pygame.display.flip()
pygame.quit()

# CHECKPOINT: ชี้ EVENT, UPDATE, DRAW และบอกว่าแต่ละส่วนทำงานอะไร
# TEST: [ ] click ถูก [ ] click ผิด [ ] ครบ attempts [ ] ปิดหน้าต่างได้
# DONE: เล่นสองเวอร์ชันแล้วผลการตัดสินต้องเหมือนกัน
# TRANSFER: เปลี่ยน animation ให้สื่อธีม และเปลี่ยนกติกา attempts หนึ่งอย่าง
# CREATIVE GAME RULES: เป้าหมาย ___ / การเลือก ___ / ชนะ ___ / แพ้ ___
# TODO: เพิ่มกติกาที่ใช้ Loop จริง 1 ข้อ เช่น เวลา การเคลื่อนที่ หรือหลายรอบ
# ก่อนทำ ระบุ DATA ___ / UPDATE ___ / LOGIC ___ / DRAW ___ ที่ต้องแก้
# DESIGN NOTE: ภาพเคลื่อนที่เพราะ ___ กติกาใหม่แก้ UPDATE ตรง ___
