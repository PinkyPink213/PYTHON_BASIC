"""บทที่ 11.2: ลงมือ Upgrade Profile ของเราเป็น Pygame

เปิด 3 ไฟล์ข้างกัน:
1. 09_2_create_your_profile.py — DATA, input, สูตร และเรื่องราวของเรา
2. 11_1_profile_generator_pygame.py — ตัวอย่าง Pygame Pattern ที่พิมพ์ตามแล้ว
3. ไฟล์นี้ — พื้นที่ทำ Profile Pygame ของเรา

วิธีทำ: COPY ของเราออกจาก 09_2 → LOOK ที่ STEP เดียวกันใน 11_1 →
TYPE Pygame Pattern ด้วยตัวเอง → ทายผล → Run → Check

ห้ามเปลี่ยนกลับเป็น Mina/Rabbit และบทนี้ยังไม่ใช้ if, for หรือ while
"""
import pygame


# ==================================================
# STEP 1: COPY input ข้อความจาก 09_2
# ==================================================

# LOOK: ดู STEP 1 ใน 11_1 ว่า input เดิมถูกเก็บไว้อย่างไร
# TODO: เปลี่ยนชื่อตัวแปรและคำถามให้ตรงกับ 09_2 ของเรา
name = input("What is your name? ").strip()
world = input("What world will you explore? ").strip()
special_power = input("What is your special power? ").strip()

# RUN CHECKPOINT 1: Run แล้ว Terminal ต้องถามครบ 3 คำถาม


# ==================================================
# STEP 2: COPY int(input()) จาก 09_2
# ==================================================

# LOOK: ดูว่า age/lucky_number ใน STEP 1 ของ 11_1 ใช้ int() ตรงไหน
# TODO: เปลี่ยนคำถามและตัวแปรให้เป็นตัวเลขจากเกมเดิมของเรา
age = int(input("How old are you? "))
collected_items = int(input("How many items did you collect? "))

# RUN CHECKPOINT 2: ใส่เลขแล้วโปรแกรมต้องไม่เกิด ValueError


# ==================================================
# STEP 3: COPY สูตรเดิมอย่างน้อย 2 สูตร
# ==================================================

# TODO: ใช้สูตรเดียวกับ 09_2 ห้ามเปลี่ยนเป็นสูตรของ Example 11_1
age_next_year = age + 1
bonus_items = collected_items * 2

# RUN CHECKPOINT 3: คำนวณด้วยมือก่อน แล้วเทียบค่ากับ Terminal Version


# ==================================================
# STEP 4: COPY String ที่เราต่อไว้ใน 09_2
# ==================================================

# TODO: สร้างชื่อ Profile ด้วย String เดิมของเรา
profile_name = name + " the Explorer"

# CHECK: ห้ามคัดลอก "the Rabbit" จาก 11_1 ให้ใช้เรื่องราวของเรา
# RUN CHECKPOINT 4: print(profile_name) แล้วต้องเป็นชื่อจากเรื่องของเรา


# ==================================================
# STEP 5: TYPE Pygame SETUP โดยดู STEP 2–3 ใน 11_1
# ==================================================

pygame.init()
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("My Pygame Profile")

title_font = pygame.font.Font(None, 52)
text_font = pygame.font.Font(None, 34)

# TODO: เลือก RGB อย่างน้อย 4 สีให้เข้ากับโลกใน 09_2
background_color = (30, 35, 70)
card_color = (80, 75, 145)
text_color = (255, 255, 255)
highlight_color = (255, 215, 80)

# RUN CHECKPOINT 5: ตอบ input แล้วต้องเห็นหน้าต่าง 800×550


# ==================================================
# STEP 6: REPLACE print() ด้วย render() โดยดู STEP 4 ใน 11_1
# ==================================================

# TODO: เปลี่ยนข้อความให้ตรงกับบรรทัดที่เรา print() ใน 09_2
title_image = title_font.render("MY ADVENTURE PROFILE", True, highlight_color)
name_image = text_font.render("Hero: " + profile_name, True, text_color)
world_image = text_font.render("World: " + world, True, text_color)
power_image = text_font.render("Power: " + special_power, True, text_color)
age_image = text_font.render("Next age: " + str(age_next_year), True, text_color)
bonus_image = text_font.render("Bonus items: " + str(bonus_items), True, text_color)
close_hint_image = text_font.render("Press any key to close", True, text_color)

# RUN CHECKPOINT 6: render() สร้าง Surface แล้ว แต่ยังไม่เห็นจนกว่าจะ blit()


# ==================================================
# STEP 7: REPLACE กรอบ Terminal ด้วย Shapes โดยดู STEP 5–6 ใน 11_1
# ==================================================

screen.fill(background_color)
pygame.draw.rect(screen, card_color, (120, 55, 560, 440), border_radius=24)

# TODO: วาด Avatar หรือสัญลักษณ์จาก Shapes อย่างน้อย 3 รูป
pygame.draw.circle(screen, highlight_color, (400, 175), 60)

# TODO: เพิ่ม Shape/Line ของตัวเองอย่างน้อย 2 รูป และทายพิกัดก่อน Run
# RUN CHECKPOINT 7: Shapes ต้องอยู่ใน Card และไม่บังข้อความสำคัญ


# ==================================================
# STEP 8: TYPE blit()/flip() โดยดู STEP 7 ใน 11_1
# ==================================================

# เขียนทีละบรรทัดเพราะ Chapter 01 ยังไม่เรียน Loop
screen.blit(title_image, title_image.get_rect(center=(400, 100)))
screen.blit(name_image, name_image.get_rect(center=(400, 275)))
screen.blit(world_image, world_image.get_rect(center=(400, 315)))
screen.blit(power_image, power_image.get_rect(center=(400, 355)))
screen.blit(age_image, age_image.get_rect(center=(400, 395)))
screen.blit(bonus_image, bonus_image.get_rect(center=(400, 435)))
screen.blit(close_hint_image, close_hint_image.get_rect(center=(400, 520)))

pygame.display.flip()
pygame.event.clear()
# Chapter 01 ยังไม่ตรวจ Mouse Button: click จึงไม่ปิด Card
# Card จะปิดเมื่อกด Keyboard หรือปุ่มปิดหน้าต่างเท่านั้น
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.wait()
pygame.quit()

# RUN CHECKPOINT 8: click ต้องไม่ปิด Card; กด Keyboard จึงปิด


# === Checklist: ตรวจเทียบกับ 09_2 ของเรา ===
# [ ] ข้อมูลข้อความอย่างน้อย 3 ค่ามาจาก 09_2
# [ ] ข้อมูลตัวเลขอย่างน้อย 2 ค่ามาจาก 09_2
# [ ] สูตรคำนวณอย่างน้อย 2 สูตรเหมือน 09_2
# [ ] String ที่ต่อไว้ยังคงแนวคิดเดิม
# [ ] print() ถูกเปลี่ยนเป็น render() และ blit()
# [ ] มีสีอย่างน้อย 4 สี และ Shapes อย่างน้อย 3 รูป
# [ ] ไม่มี if, for หรือ while ก่อนลำดับบท

# === TEST เทียบ Terminal → Pygame ===
# [ ] ชื่อ/โลก/พลังตรงกับ 09_2
# [ ] สูตร next age/bonus ให้ผลตัวเลขเหมือน Terminal
# [ ] ข้อความทุกบรรทัดเห็นครบและไม่ออกนอก Card
# [ ] เปิดและปิดหน้าต่างได้โดยไม่มี Error

# === TRANSFER CHALLENGE: ประยุกต์เป็นของเรา ===
# เลือกโลกใหม่ 1 ธีม แล้วเปลี่ยน DATA, สี/Shapes ใน UI และข้อความเรื่องราว
# อธิบาย: สิ่งที่แก้ใน DATA คือ ___ สิ่งที่แก้เฉพาะ UI คือ ___

# === CREATIVE DESIGN: พื้นที่คิดผลงานเอง ===
# Chapter นี้ยังไม่มี if/else จึงยังไม่สร้างกติกาชนะ–แพ้
# TODO: Card นี้เล่าเรื่องใคร ___ อยู่โลกไหน ___ มีเป้าหมายอะไร ___
# TODO: สูตร 2 สูตรสื่อความหมายกับเรื่องอย่างไร ___
# TODO: เลือก Shapes/สีที่ช่วยเล่าเรื่อง ไม่ใช่แค่ตกแต่ง แล้วอธิบายเหตุผล ___
# Chapter 02 เป็นต้นไป เราจะนำข้อมูลแบบนี้ไปสร้าง "กติกาเกม" ด้วย if/else
