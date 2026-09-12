"""บทที่ 7: Pygame Basic — ทำ Inventory จาก List โดยยังไม่ใช้ Loop

เป้าหมาย: เห็นว่า List คือ DATA ส่วนปุ่มและรูปเป็น UI ที่อ่านค่าจาก List
ทุก STEP ใช้จังหวะ พิมพ์ → ทายผล → Run → อธิบาย
Chapter 04 จะนำโค้ดวาดซ้ำไปย่อด้วย Loop
แต่ละ Example เป็นโค้ดสมบูรณ์ ให้พิมพ์ตามก่อนทำ Your turn/TODO ที่อยู่ถัดไป
"""
from pathlib import Path
import pygame

# --- Example 1: List is game DATA ---
items = ["rope", "water", "fruit"]
backpack = []
# --- Your turn 1 ---
# TODO 1: เปลี่ยน items[1] และทายว่าปุ่มใดจะเปลี่ยน
# RUN CHECKPOINT 1: UI ต้องอ่านค่าใหม่จาก List โดยไม่แก้ข้อความซ้ำใน DRAW

# STEP 2 — SETUP: เปิดหน้าต่างและสร้าง Font
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("List Inventory")
font = pygame.font.Font(None, 34)

# --- Example 2: Load one image ทีละคำสั่ง ---
asset_folder = Path(__file__).parent / "assets" / "items"

# 3A image.load() อ่านไฟล์ PNG แล้วคืน Surface (ภาพที่ Pygame ใช้วาดได้)
rope_image = pygame.image.load(asset_folder / "rope.png")
# ทายก่อน Run: ตอนนี้รูปถูกอ่านแล้ว แต่ถูกวางบน screen หรือยัง? (ยัง)

# 3B convert_alpha() เตรียมภาพให้วาดเร็วและเก็บส่วนโปร่งใส
rope_image = rope_image.convert_alpha()

# 3C smoothscale() รับภาพเดิมกับ Tuple (width, height) แล้วคืนภาพขนาดใหม่
rope_image = pygame.transform.smoothscale(rope_image, (110, 110))

# --- Your turn 2 ---
# TODO 2: หลังเข้าใจรูปแรก ให้พิมพ์ 3A → 3B → 3C เองกับ water และ fruit
water_image = pygame.image.load(asset_folder / "water_bottle.png")
water_image = water_image.convert_alpha()
water_image = pygame.transform.smoothscale(water_image, (110, 110))
fruit_image = pygame.image.load(asset_folder / "fruit.png")
fruit_image = fruit_image.convert_alpha()
fruit_image = pygame.transform.smoothscale(fruit_image, (110, 110))
# TODO 3: เปลี่ยนขนาดรูปหนึ่งรูป แล้วทายผลก่อน Run
# RUN CHECKPOINT 2: รูปครบสามรูป ขนาดตามที่ทาย และไม่มี Asset/Path Error

# STEP 4 — RECT: Rect ยังไม่ใช่ปุ่มจนกว่า EVENT จะนำไปตรวจ click
# รูปแบบคือ pygame.Rect(x, y, width, height)
button_1 = pygame.Rect(105, 310, 200, 70)
button_2 = pygame.Rect(350, 310, 200, 70)
button_3 = pygame.Rect(595, 310, 200, 70)

# --- Example 3: DRAW ตามลำดับ ---
screen.fill((28, 40, 65))

# render() สร้าง Surface ข้อความ; blit() นำ Surface ไปวางที่ (x, y)
title_image = font.render("CHOOSE AN ITEM", True, "white")
screen.blit(title_image, (325, 55))

# blit(image, position) จึงเป็นขั้นตอนที่ทำให้รูปที่ load ไว้มาอยู่บน screen
screen.blit(rope_image, (150, 150))
screen.blit(water_image, (395, 150))
screen.blit(fruit_image, (640, 150))

# draw.rect() วาดรูปสี่เหลี่ยมตามตำแหน่ง/ขนาดที่ Rect เก็บไว้
pygame.draw.rect(screen, (245, 185, 75), button_1, border_radius=12)
pygame.draw.rect(screen, (245, 185, 75), button_2, border_radius=12)
pygame.draw.rect(screen, (245, 185, 75), button_3, border_radius=12)
screen.blit(font.render(items[0].upper(), True, (25, 30, 40)), (165, 332))
screen.blit(font.render(items[1].upper(), True, (25, 30, 40)), (405, 332))
screen.blit(font.render(items[2].upper(), True, (25, 30, 40)), (655, 332))
# flip() นำ frame ที่วาดเสร็จทั้งหมดขึ้นจอพร้อมกัน
pygame.display.flip()
# --- Your turn 3 ---
# TODO 4: หลังพิมพ์ DRAW ตามแล้ว เปลี่ยนตำแหน่งรูป/ปุ่มหนึ่งคู่
# RUN CHECKPOINT 3: รูป ปุ่ม และชื่อ item เดียวกันต้องยังจับคู่กัน
# ชี้ว่ารูปใดและข้อความใดอ่านจาก items[1]

# STEP 6 — EVENT + UPDATE: click ทำให้ backpack เปลี่ยน
# ทายก่อน: คลิก Card ซ้ายแล้ว backpack จะเก็บ String ใด?
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
event = pygame.event.wait()
if event.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
elif event.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(event.pos):
        backpack.append(items[0])
    elif button_2.collidepoint(event.pos):
        backpack.append(items[1])
    elif button_3.collidepoint(event.pos):
        backpack.append(items[2])

# STEP 7 — DRAW RESULT: UI อ่าน List หลังเปลี่ยนค่า
message = "Backpack: " + str(backpack) + "   Used: " + str(len(backpack)) + "/3"
screen.blit(font.render(message, True, (110, 230, 175)), (225, 470))
pygame.display.flip()
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
pygame.event.wait()
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
pygame.event.wait()
pygame.quit()

# RUN CHECKPOINT 4: click แต่ละปุ่มแล้ว backpack ต้องได้ items[index] ที่ตรงกัน

# คำถามเช็กความเข้าใจ / Exit ticket
# 1. items กับ backpack มีหน้าที่ต่างกันอย่างไร?
# 2. append() เปลี่ยน DATA ตรงไหน และ DRAW แสดงผลตรงไหน?
# 3. เหตุใดบทนี้จึงต้องเขียน Card ซ้ำ และ Chapter 04 จะช่วยอย่างไร?
