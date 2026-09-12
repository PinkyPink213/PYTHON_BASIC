"""บทที่ 11.1: เรียน Basic Pygame ผ่านการสร้าง Adventure Profile Card

ไฟล์นี้ Convert 09_1_profile_generator.py โดยตรง เด็กจะพิมพ์ตามทีละ STEP
รับข้อมูลและคำนวณด้วยโค้ดเดิม แล้วเปลี่ยนเฉพาะ Output จาก print()
เป็น Profile Card บนหน้าต่าง Pygame

ถ้ายังไม่ได้ทำบท 10 ให้ติดตั้งก่อนเรียน
macOS / Linux: python3 -m pip install pygame
Windows:         py -m pip install pygame

ตรวจว่าติดตั้งสำเร็จ
macOS / Linux: python3 -c "import pygame; print(pygame.version.ver)"
Windows:         py -c "import pygame; print(pygame.version.ver)"
ถ้า Windows ไม่มีคำสั่ง py ให้เปลี่ยน py เป็น python

ถ้า Python รุ่นใหม่ติดตั้งไม่ผ่าน ใช้ pygame-ce แทนได้
macOS / Linux: python3 -m pip install pygame-ce
Windows:         py -m pip install pygame-ce
ทั้งสองแบบยังเขียน import pygame เหมือนกัน

คู่มือครู
1. ให้เด็กพิมพ์และ Run เมื่อจบแต่ละ STEP
2. ชี้ความสัมพันธ์ระหว่าง Variables เดิมกับสิ่งที่ปรากฏบนการ์ด
3. บทนี้เป็นหน้าจอแบบ Static จึงไม่ใช้ if, for หรือ while ก่อนลำดับบท
4. พิมพ์ Example ให้ทำงานก่อน แล้วทำ Your turn/TODO สั้น ๆ
5. โปรเจกต์ของเด็กอยู่ใน 11_2 ซึ่งต่อยอดจาก 09_2 โดยตรง
"""

import pygame


# ==================================================
# STEP 1: นำข้อมูลจาก Terminal Profile มาใช้ต่อ
# ==================================================

# COPY จาก 09_1: input และการเตรียม DATA ยังเหมือนเดิมทุกบรรทัด
# Chapter 01 ยังไม่ได้เรียนรับข้อความผ่าน Keyboard Event ในหน้าต่าง
# จึงตอบคำถามใน Terminal ก่อน แล้ว Pygame นำคำตอบไปสร้าง Card
name = input("What is your name? ").strip()
age = int(input("How old are you? "))
favorite_animal = input("What is your favorite animal? ").strip().lower()
lucky_number = int(input("What is your lucky number? "))

# COPY GAME LOGIC: ชื่อตัวแปรและสูตรตรงกับ 09_1
next_age = age + 1
double_lucky_number = lucky_number * 2
hero_name = name + " the " + favorite_animal.title()

# CHECKPOINT: ก่อนเขียน Pygame ให้เทียบ STEP 1 กับ 09_1 ทีละบรรทัด
# DATA/สูตรต้องเหมือนกัน สิ่งที่จะเปลี่ยนมีเพียงวิธีแสดงผล


# ==================================================
# STEP 2: เริ่ม Pygame และสร้างหน้าต่าง
# ==================================================

# pygame.init() เตรียมระบบหน้าต่างและตัวอักษร
pygame.init()

# set_mode() รับเลขสองค่า (width, height) เป็นชุดขนาดของหน้าต่าง
# ตอนนี้จำเพียงรูปแบบวงเล็บนี้ก่อน เราจะเรียนชนิดข้อมูล Tuple ใน Chapter 05
# screen คือพื้นที่สำหรับวาดทุกอย่างในเกม
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Adventure Profile Maker")


# --- Your turn 1: Window ---
# TODO 1: เปลี่ยนข้อความบนหัวหน้าต่างเป็นชื่อเกมของเรา
# เขียน pygame.display.set_caption() อีกครั้งใต้คอมเมนต์นี้
# RUN CHECKPOINT 1: Run แล้วต้องเห็นหน้าต่าง 800×550 และชื่อใหม่บนแถบด้านบน




# ==================================================
# STEP 3: สร้าง Font และสี RGB
# ==================================================

# None หมายถึงใช้ Font มาตรฐาน ตัวเลขคือขนาดตัวอักษร
title_font = pygame.font.Font(None, 52)
text_font = pygame.font.Font(None, 34)

# RGB คือ (red, green, blue) แต่ละค่าอยู่ระหว่าง 0–255
background_color = (26, 31, 68)
card_color = (91, 70, 150)
text_color = (248, 248, 255)
highlight_color = (255, 215, 80)


# --- Your turn 2: RGB Color ---
# TODO 2: สร้างสีใหม่ชื่อ badge_color โดยใช้เลข RGB ที่เราเลือกเอง
# ตัวอย่างรูปแบบ: badge_color = (red, green, blue)
# เขียนโค้ดใต้คอมเมนต์นี้ แล้วนำสีไปใช้ใน Practice 5
# RUN CHECKPOINT 2: ลอง print(badge_color) และตรวจว่าเป็นเลข RGB สามค่า




# ==================================================
# STEP 4: เปลี่ยน String ให้เป็นภาพข้อความ
# ==================================================

# render() สร้างภาพข้อความ แต่ยังไม่ได้วางภาพลง screen
title_image = title_font.render("YOUR ADVENTURE PROFILE", True, highlight_color)

# ข้อความยังอ่านค่าจาก Variables และใช้ str() เหมือนที่เรียนมา
hero_image = text_font.render("Hero name: " + hero_name, True, text_color)
age_image = text_font.render("Age next year: " + str(next_age), True, text_color)
power_image = text_font.render(
    "Super lucky number: " + str(double_lucky_number), True, text_color
)
story_image = text_font.render("Your adventure begins now!", True, highlight_color)
# บทนี้ยังไม่เรียน if เพื่อตรวจปุ่ม จึงใช้ Keyboard ปิด Card อย่างชัดเจน
close_hint_image = text_font.render("Press any key to close", True, text_color)


# --- Your turn 3: render() ---
# TODO 3: สร้าง String ชื่อ creator_name และเก็บชื่อของเรา
# จากนั้นใช้ text_font.render() สร้าง creator_image
# ผลลัพธ์ที่ต้องการบนการ์ด: Created by: ชื่อของเรา
#
# creator_name = ...
# creator_image = ...
# RUN CHECKPOINT 3: Run แล้วต้องไม่มี NameError; ภาพข้อความยังไม่ปรากฏจนกว่า blit()




# ==================================================
# STEP 5: ทบทวนพิกัดก่อนวาด
# ==================================================

# จุด (0, 0) อยู่มุมซ้ายบน
# x เพิ่มเมื่อไปทางขวา และ y เพิ่มเมื่อลงด้านล่าง
# Rect ใช้ (x, y, width, height)
# Circle ใช้จุดศูนย์กลาง (x, y) และรัศมี
# Line ใช้จุดเริ่ม (x1, y1), จุดจบ (x2, y2) และความหนา


# ==================================================
# STEP 6: วาดพื้นหลัง Card และ Avatar
# ==================================================

# บทนี้วาดเพียงหนึ่ง Frame จึงยังไม่ต้องใช้ Game Loop
screen.fill(background_color)
pygame.draw.rect(screen, card_color, (130, 60, 540, 430), border_radius=25)
pygame.draw.circle(screen, highlight_color, (400, 190), 65)
# draw.line(surface, color, start_position, end_position, width)
pygame.draw.line(screen, highlight_color, (180, 245), (620, 245), 4)

# --- Your turn 4: Shape และพิกัด ---
# TODO 4: วาดวงกลมเล็กเป็น badge โดยใช้ badge_color จาก Your turn 2
# RUN CHECKPOINT 4: Run แล้ววงกลมต้องอยู่ใน Card; เปลี่ยน x/y และสังเกตทิศทาง

# --- Your turn 4.1: ออกแบบเส้น ---
# 1. ทายก่อนว่าเส้นจาก (250, 460) ไป (550, 460) จะอยู่บริเวณใด
# 2. พิมพ์ pygame.draw.line() โดยเลือกสี จุดเริ่ม จุดจบ และความหนาเอง
# 3. Run แล้วอธิบายว่าเลขคู่ใดควบคุมตำแหน่ง และเลขใดควบคุมความหนา
# RUN CHECKPOINT 4.1: เห็นเส้นใหม่และอธิบาย start/end/width ได้


# ==================================================
# STEP 7: วางข้อความบน Profile Card
# ==================================================

screen.blit(title_image, title_image.get_rect(center=(400, 105)))
screen.blit(hero_image, hero_image.get_rect(center=(400, 285)))
screen.blit(age_image, age_image.get_rect(center=(400, 330)))
screen.blit(power_image, power_image.get_rect(center=(400, 375)))
screen.blit(story_image, story_image.get_rect(center=(400, 435)))
screen.blit(close_hint_image, close_hint_image.get_rect(center=(400, 520)))

# --- Your turn 5: blit() ---
# TODO 5: นำ creator_image จาก Your turn 3 มาวางที่กึ่งกลาง (400, 470)
# RUN CHECKPOINT 5: เห็น "Created by" ครบ ไม่ซ้อนข้อความ และอยู่ใน Card


# flip() แสดง Profile Card ที่วาดเสร็จแล้ว
pygame.display.flip()

# WINDOW SAFETY PATTERN — ส่วนนี้ทำให้ Card ไม่ดับเอง
# set_blocked(None) ปิด Event ทุกชนิดก่อน
# set_allowed() เปิดเฉพาะปุ่มปิดและ keyboard ที่เราต้องการ
# clear() ล้าง Event เก่าจากตอนเปิดหน้าต่าง
# wait() รอหนึ่ง Event ที่อนุญาต จึงยังไม่ต้องใช้ if/for/while
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.clear()
pygame.event.wait()

pygame.quit()


# ==================================================
# เปรียบเทียบ Terminal กับ Pygame
# ==================================================

# Terminal: print("Hero: " + hero_name)
# Pygame:   font.render() สร้างภาพ และ screen.blit() วางภาพ
#
# Terminal: print("================")
# Pygame:   pygame.draw.rect() วาดกรอบการ์ด
#
# input(), hero_name, next_age และ double_lucky_number มาจาก 09_1 โดยตรง
# เราเปลี่ยนเฉพาะ Interface ที่ใช้แสดงผล


# === คำถามเช็กความเข้าใจ ===
# 1. screen ทำหน้าที่อะไร?
# 2. set_mode((800, 550)) เลขสองตัวหมายถึงอะไร?
# 3. render() และ blit() ต่างกันอย่างไร?
# 4. ถ้าเพิ่มค่า x วัตถุจะไปทางใด? ถ้าเพิ่มค่า y จะไปทางใด?
# 5. ส่วนใดเป็น Game Data และส่วนใดเป็น Interface?
# 6. เพราะอะไรต้องมี pygame.display.flip()?
# 7. draw.line() ต้องรับจุดพิกัดกี่จุด และแต่ละจุดมีค่าอะไร?
# 8. เพราะอะไรบทนี้ใช้ Keyboard ปิด Card แทนการตรวจ Mouse Click?
# 9. บรรทัดใด COPY จาก 09_1 และบรรทัดใดเป็น Pygame ที่เพิ่มใหม่?
