"""บทที่ 8.2: Upgrade 06_2_create_your_guessing_game.py เป็น Pygame

เปิด 3 หน้าต่างข้างกัน:
1) 06_2 = เกม Terminal ของเรา  2) 07 และ 08_1 = ตัวอย่างที่พิมพ์ตาม
3) ไฟล์นี้ = พื้นที่ Convert เกมของเรา (ไม่จำเป็นต้องเป็นเกมสัตว์)

COPY ข้อมูลและ if/elif/else จาก 06_2, LOOK รูปแบบปุ่มใน 07/08_1,
TYPE ด้วยมือลงไฟล์นี้ แล้ว RUN CHECKPOINT ทุก STEP
input() เปลี่ยนเป็น click; print() เปลี่ยนเป็น render()/blit()
บทนี้ยังไม่ใช้ List, for หรือ while
"""
from pathlib import Path
import pygame

# STEP 1 — COPY DATA: ใช้ตัวเลือก/คำใบ้/คำตอบจาก 06_2 ของเรา
# LOOK: เปิด 06_2 แล้ววงตัวแปรที่เป็น DATA และเงื่อนไขที่เป็น LOGIC
# TYPE/TODO: พิมพ์ค่าของเกมเราแทนค่าตัวอย่างด้านล่าง
# RUN CHECKPOINT: รันแล้วต้องยังไม่มี SyntaxError
# TODO: เปลี่ยนเป็น animal, food หรือ fantasy ใน assets
choice_1 = "cat"
choice_2 = "rabbit"
choice_3 = "dog"
secret_choice = "rabbit"
message = "Hint: It has long ears"

# STEP 2 — SCREEN + IMAGE: เรื่องนี้พิมพ์ตามมาแล้วในไฟล์ 07
# LOOK: เทียบ pygame.init(), set_mode(), Font และ load image กับไฟล์ 07
# TYPE/TODO: เลือกชื่อหน้าต่าง ขนาด และ asset ที่เข้ากับเกมเรา
# RUN CHECKPOINT: หน้าต่างต้องเปิดและเห็นภาพก่อนสร้างปุ่ม
pygame.init()
screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("My Guessing Game")
font = pygame.font.Font(None, 34)
image_path = Path(__file__).parent / "assets" / "animals" / "animal_choices.png"
picture = pygame.transform.smoothscale(
    pygame.image.load(image_path).convert_alpha(), (600, 338)
)

# STEP 3 — BUTTONS: เขียนทีละปุ่ม เพราะ Loop เรียนใน Chapter 04
# LOOK: ดู Rect และ collidepoint ใน 07/08_1 แล้วพิมพ์เองทีละปุ่ม
# RUN CHECKPOINT: วาดกรอบชั่วคราวและตรวจว่าปุ่มไม่ซ้อนกัน
button_1 = pygame.Rect(125, 470, 190, 60)
button_2 = pygame.Rect(355, 470, 190, 60)
button_3 = pygame.Rect(585, 470, 190, 60)

# STEP 4 — DRAW BEFORE INPUT: ผู้เล่นต้องเห็นตัวเลือกก่อนคลิก
screen.fill((28, 34, 68))
screen.blit(picture, (150, 90))
pygame.draw.rect(screen, (90, 195, 210), button_1, border_radius=10)
pygame.draw.rect(screen, (90, 195, 210), button_2, border_radius=10)
pygame.draw.rect(screen, (90, 195, 210), button_3, border_radius=10)
screen.blit(font.render(choice_1.upper(), True, (20, 30, 45)), (185, 490))
screen.blit(font.render(choice_2.upper(), True, (20, 30, 45)), (405, 490))
screen.blit(font.render(choice_3.upper(), True, (20, 30, 45)), (645, 490))
screen.blit(font.render(message, True, "white"), (120, 580))
pygame.display.flip()

# STEP 5 — EVENT: click แทน input() และ if/elif เลือกคำตอบ
# LOOK: ชี้ให้ได้ว่า event.pos ทำหน้าที่แทนคำตอบจาก input() ตรงไหน
# RUN CHECKPOINT: คลิกทั้งสามบริเวณแล้ว selected_choice ต้องตรงกับปุ่ม
# ทายก่อน Run: selected_choice จะเป็นอะไรเมื่อคลิกปุ่มขวา?
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
selected_choice = ""
event = pygame.event.wait()
if event.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
elif event.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(event.pos):
        selected_choice = choice_1
    elif button_2.collidepoint(event.pos):
        selected_choice = choice_2
    elif button_3.collidepoint(event.pos):
        selected_choice = choice_3

# STEP 6 — COPY LOGIC: เงื่อนไขนี้ควรมาจาก Terminal Version
if selected_choice == secret_choice:
    message = "CORRECT! " + selected_choice.upper()
elif selected_choice == "":
    message = "Click inside one button next time"
else:
    message = "Not " + selected_choice + ". Try again!"

# STEP 7 — DRAW AFTER UPDATE: print(message) กลายเป็น render + blit
pygame.draw.rect(screen, (28, 34, 68), (0, 560, 900, 90))
screen.blit(font.render(message, True, "white"), (120, 580))
pygame.display.flip()
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
pygame.event.wait()
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
pygame.event.wait()
pygame.quit()

# CREATIVE GAME RULES — ออกแบบเกมของเรา ไม่ใช่แค่เปลี่ยนรูป
# TODO: เกมมีเป้าหมายอะไร? ผู้เล่นชนะเมื่อใด และเลือกผิดเกิดอะไรขึ้น?
# TODO: เพิ่มกติกาใหม่ด้วย if/elif/else 1 ข้อ เช่น bonus, trap หรือ secret choice
# TODO: เขียนก่อนลงมือว่าแก้ DATA ___ / LOGIC ___ / UI ___
# Exit ticket: วง DATA, EVENT, game logic และ DRAW อย่างละหนึ่งส่วน
# TEST: [ ] click ครบ 3 ปุ่ม [ ] คำตอบถูกชนะ [ ] คำตอบผิดลองใหม่
# [ ] click นอกปุ่มไม่ crash [ ] ผล if/elif/else เหมือน Terminal Version
# TRANSFER: เปลี่ยน animal เป็น food/fantasy และเพิ่มผลลัพธ์ elif ของเรา 1 แบบ
# อธิบายก่อนเขียนว่าแก้ DATA, logic และ UI บรรทัดใดบ้าง
