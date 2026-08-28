"""Pygame Basic: ใช้ Set เลือกตัวละครไม่ซ้ำและคลิกซ้ำเพื่อนำออก.

Mental model: click → add/remove ใน selected → membership กำหนดสี Card
ก่อน Run ให้เด็กทายทั้งค่าของ Set และสีที่จะเห็น ห้ามตอบเพียงว่า “ปุ่มทำงาน”
พิมพ์ Example การเลือกให้ทำงานก่อน แล้วทำ Your turn/TODO ทีละแนวคิด
"""
from pathlib import Path
import pygame
pygame.init()
screen = pygame.display.set_mode((850, 520))
font = pygame.font.Font(None, 30)
# โหลดแถว Hero จาก asset atlas เพื่อให้เด็กมีภาพตัวเลือกพร้อมใช้
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
hero_picture = atlas.subsurface(pygame.Rect(0, 384, 1024, 384))
hero_picture = pygame.transform.smoothscale(hero_picture, (600, 120))
heroes = ("aqua", "flash", "rock", "sky")
selected = set()
buttons = [pygame.Rect(65, 170, 160, 100), pygame.Rect(260, 170, 160, 100),
           pygame.Rect(455, 170, 160, 100), pygame.Rect(650, 170, 160, 100)]
message = "Choose 3 different heroes"

# --- Your turn 1: Set Data ---
# พิมพ์ตัวอย่างตามก่อน แล้วเปลี่ยนชื่อ heroes เป็นทีมของเราโดยคง 4 คน
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for index in range(4):
                hero = heroes[index]
                button = buttons[index]
                if button.collidepoint(event.pos):
                    if hero in selected:
                        selected.remove(hero)
                    elif len(selected) < 3:
                        selected.add(hero)
                    else:
                        message = "Team is full"

            # --- Your turn 2: add/remove ---
            # ถ้า selected ว่าง ให้ message เป็น "Team is empty"
    screen.fill((25, 35, 65))
    screen.blit(hero_picture, (125, 25))
    for index in range(4):
        hero = heroes[index]
        button = buttons[index]
        color = (95, 115, 155)
        if hero in selected:
            color = (80, 205, 145)
        pygame.draw.rect(screen, color, button, border_radius=15)
        label = font.render(hero.upper(), True, "white")
        screen.blit(label, label.get_rect(center=button.center))
    screen.blit(font.render("Team: " + str(selected), True, "white"), (100, 350))
    screen.blit(font.render(message, True, (255, 220, 100)), (100, 420))

    # --- Your turn 3: Membership กับ UI ---
    # แสดงคำว่า READY เมื่อ len(selected) == 3
    pygame.display.flip()
pygame.quit()

# RUN CHECKPOINT: click เพิ่ม/เอาออก, ไม่ซ้ำ, เต็ม 3 คน และสีอ่านจาก Set

# === Your Turn ===
# TODO 1: สร้างทีมตัวละครของตัวเอง
# TODO 2: เพิ่มปุ่ม CLEAR ที่เรียก selected.clear()
# TODO 3: เปลี่ยนสีของ card ตามการเป็นสมาชิกใน selected

# คำถาม: Set ป้องกันตัวละครซ้ำต่างจาก List อย่างไร?
# Exit ticket: ชี้บรรทัดที่เปลี่ยน DATA และบรรทัดที่อ่าน DATA ไป DRAW
