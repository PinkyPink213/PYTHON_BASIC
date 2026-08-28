"""Upgrade 07_2_create_your_dictionary_game.py ของเราเป็น Pygame.

เปิด 3 หน้าต่าง: 07_2 = เกม Terminal ของเรา, 08/09_1 = Reference,
ไฟล์นี้ = พื้นที่ Convert
COPY Dictionary/conditions, LOOK Card, TYPE ด้วยมือ, REPLACE input/print
และ RUN CHECKPOINT ทุก STEP ให้ Dictionary เป็นข้อมูลจริงชุดเดียว
"""
import pygame

# STEP 1 COPY: Nested Dictionary และเงื่อนไขจาก 07_2
# TODO/RUN CHECKPOINT: print แล้ว keys/values ต้องตรง Terminal
# STEP 2 LOOK/TYPE: ดู 08/09_1 แล้วสร้าง Card จาก keys/values
# RUN CHECKPOINT: แก้ value จุดเดียวแล้ว Card เปลี่ยน
# STEP 3 TYPE: click key แล้วอ่านรายละเอียดจาก Dictionary
# RUN CHECKPOINT: ทุก Card อ่าน character ถูกตัว
# STEP 4 COPY LOGIC: update status/score กลับตามกติกาเดิม
# RUN CHECKPOINT: click หนึ่งครั้งเปลี่ยนค่าหนึ่งครั้ง
# STEP 5 TYPE DRAW: แสดงตอนจบเดิมด้วย render()/blit()
# RUN CHECKPOINT: เล่นทุกเส้นทางจนจบและผลตรง Terminal

pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 34)
# TODO: คัดลอก Dictionary จริงจาก 07_2
characters = {"my character": {"power": "change me", "score": 0}}
message = "Dictionary is the single source of truth"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: คลิก key แล้วอ่าน/เปลี่ยน value ตาม logic เดิม
    screen.fill((25, 35, 65))
    screen.blit(font.render(message, True, "white"), (170, 260))
    pygame.display.flip()
pygame.quit()

# CHECKPOINT: เปลี่ยน value หนึ่งค่า แล้วทายว่าส่วนใดของ Card ต้องเปลี่ยน
# TEST: [ ] ทุก key มี Card [ ] click อ่านตัวถูก [ ] update value [ ] ตอนจบเดิม
# DONE: เพิ่ม character จาก Dictionary โดยไม่คัดลอกคำสั่งวาดทั้งก้อน
# TRANSFER: ออกแบบ Character keys ใหม่ 3 ตัวและเพิ่ม value ที่มีผลต่อ logic
# CREATIVE GAME RULES: เป้าหมาย ___ ความสามารถแต่ละตัวมีผลอย่างไร ___ ชนะเมื่อ ___
# TODO: เพิ่ม key/value ใหม่ที่เปลี่ยนกติกาจริง 1 ค่า ไม่ใช่แค่ข้อความตกแต่ง
# ระบุ DICTIONARY DATA ___ / LOGIC ___ / CARD UI ___ ก่อนทำ
# DESIGN NOTE: value ใหม่คือ ___ Card แสดงที่ ___ และกติกาอ่านที่ ___
