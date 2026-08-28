"""Pygame Basic: Tuple เหมาะกับข้อมูลพิกัดคงที่และการตรวจ click.

แผนภาพก่อนพิมพ์: planet tuple → unpack name/x/y/color → draw ที่ (x, y)
เด็กต้องทายว่าการแก้ tuple หนึ่งค่าจะเปลี่ยนอะไรบนจอก่อน Run
พิมพ์ Example แผนที่ให้ทำงานก่อน แล้วทำ Your turn/TODO ใต้แนวคิดนั้น
"""
from pathlib import Path
import pygame
pygame.init()
screen = pygame.display.set_mode((850, 520))
font = pygame.font.Font(None, 30)

# Atlas คือรูปตัวเลือกหลายภาพในไฟล์เดียว Rect นี้เลือกช่องรูปดวงจันทร์
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
moon_icon = atlas.subsurface(pygame.Rect(0, 0, 341, 384))
moon_icon = pygame.transform.smoothscale(moon_icon, (90, 90))

# แต่ละ nested tuple รวมชื่อ, x, y และสีของดาวหนึ่งดวง
planets = (("moon", 180, 220, "white"), ("mars", 425, 150, "coral"),
           ("saturn", 680, 290, "gold"))

# --- Your turn 1: Nested Tuple ---
# พิมพ์ Tuple ตัวอย่างตามก่อน แล้วเพิ่มดาวดวงที่ 4 พร้อม name, x, y และ color
# RUN CHECKPOINT 1: ดาวใหม่วาดจาก Tuple โดยไม่คัดลอก DRAW เพิ่ม
message = "Click a planet"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for name, x, y, color in planets:  # unpack tuple
                if pygame.Rect(x - 45, y - 45, 90, 90).collidepoint(event.pos):
                    message = "Destination: " + name.title()

            # --- Your turn 2: Click ---
            # ถ้าคลิก mars ให้ message เพิ่มคำว่า "Red Planet"
    screen.fill((15, 20, 50))
    for name, x, y, color in planets:
        pygame.draw.circle(screen, color, (x, y), 45)
        screen.blit(font.render(name, True, "white"), (x - 35, y + 60))
    # วาง icon ทับวงกลม moon เพื่อเห็นว่ารูปกับ Shape ใช้พิกัดชุดเดียวกัน
    screen.blit(moon_icon, (135, 175))

    # --- Your turn 3: Unpack และ Draw ---
    # ใช้ for/unpack วาดวงกลมเล็กที่พิกัดดาวทุกดวง
    screen.blit(font.render(message, True, "white"), (310, 450))
    pygame.display.flip()
pygame.quit()

# RUN CHECKPOINT 2: click ทุกดาวและนอกดาวได้โดยไม่ crash; message ตรง DATA

# === Your Turn ===
# TODO 1: สร้างแผนที่อย่างน้อย 4 จุด
# TODO 2: ทำให้ทุกจุดคลิกได้
# TODO 3: ใช้ข้อมูล Tuple กำหนดสีและขนาด

# คำถาม: เหตุใดพิกัดตั้งต้นจึงเหมาะกับ Tuple มากกว่า List?
# Exit ticket: วงข้อมูลของดาวหนึ่งดวง และวง UI ที่วาดข้อมูลนั้น
