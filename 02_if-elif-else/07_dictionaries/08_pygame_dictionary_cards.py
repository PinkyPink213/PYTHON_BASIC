"""Pygame Basic: สร้าง Character Cards จาก Dictionary โดยไม่เขียน UI ซ้ำ.

Mental model: Dictionary เป็นแหล่งข้อมูลจริงเพียงชุดเดียว; Card แค่อ่านมาแสดง
ก่อน Run ให้เปลี่ยน value หนึ่งค่าและทายว่าข้อความใดบน Card จะเปลี่ยน
พิมพ์ Example Card ให้ทำงานก่อน แล้วทำ Your turn/TODO ใต้ตัวอย่าง
"""
from pathlib import Path
import pygame
pygame.init()
screen = pygame.display.set_mode((900, 540))
font = pygame.font.Font(None, 28)
# รูปหนึ่งแถวมี pet 3 ตัว ตำแหน่งซ้าย/กลาง/ขวาตรงกับ Card ด้านล่าง
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
pet_picture = atlas.subsurface(pygame.Rect(0, 768, 1024, 384))
pet_picture = pygame.transform.smoothscale(pet_picture, (720, 135))

pets = {"milo": {"animal": "cat", "age": 3, "color": "orange"},
        "lucky": {"animal": "dog", "age": 5, "color": "gold"},
        "snow": {"animal": "rabbit", "age": 2, "color": "white"}}

# --- Your turn 1: Nested Dictionary ---
# พิมพ์ Dictionary ตัวอย่างตามก่อน แล้วเพิ่ม key "favorite_food" ให้ pet ทุกตัว

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((28, 38, 67))
    screen.blit(pet_picture, (90, 35))
    # items() ให้ทั้งชื่อ pet และ nested dictionary สำหรับสร้าง card หนึ่งใบ
    index = 0
    for name in pets:
        data = pets[name]
        card = pygame.Rect(65 + index * 280, 180, 240, 300)
        pygame.draw.rect(screen, (82, 102, 145), card, border_radius=18)
        lines = [name.title(), data["animal"].title(), "Age: " + str(data["age"]), data["color"].title()]

        # --- Your turn 2: อ่าน Value ---
        # เพิ่ม data["favorite_food"] ลงใน lines เพื่อแสดงบน card
        line_index = 0
        for line in lines:
            image = font.render(line, True, "white")
            screen.blit(image, image.get_rect(center=(card.centerx, 245 + line_index * 50)))
            line_index += 1
        index += 1
    pygame.display.flip()
pygame.quit()

# RUN CHECKPOINT: แก้ value จุดเดียวแล้ว Card ต้องอ่านค่าล่าสุดจาก Dictionary

# === Your Turn ===
# TODO 1: เพิ่ม pet ตัวที่ 4 โดยไม่เขียนคำสั่งวาด card ซ้ำ
# TODO 2: เพิ่มข้อมูลใหม่อย่างน้อย 2 keys แล้วแสดงบน card
# TODO 3: ออกแบบสี card จาก Value ใน Dictionary

# คำถาม: ทำไม data-driven UI จึงเพิ่มตัวละครได้ง่าย?
# Exit ticket: ถ้าลบ Card แต่ Dictionary ยังอยู่ เกมสูญเสีย DATA หรือ UI?
