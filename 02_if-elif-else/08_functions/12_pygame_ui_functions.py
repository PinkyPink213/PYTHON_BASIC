"""Pygame Basic: แยก UI เป็น Functions ที่เรียกซ้ำได้.

Function รับข้อมูลผ่าน arguments และวาดลง surface; return Rect ให้ event ใช้ต่อ

Mental model: game-logic Function เปลี่ยน DATA; draw Function แสดง DATA
ก่อน Run ให้เด็กพูดชื่อ Function, input, output/effect แล้วจึงเรียกใช้
พิมพ์ Example Function ให้ทำงานก่อน แล้วทำ Your turn/TODO ที่ตามมา
"""
from pathlib import Path
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
font = pygame.font.Font(None, 34)
# เลือกช่อง Dice Monster จาก atlas; UI Function ด้านล่างนำไปวางซ้ำได้
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
monster_image = atlas.subsurface(pygame.Rect(0, 1152, 341, 384))
monster_image = pygame.transform.smoothscale(monster_image, (150, 170))

def draw_text(surface, text, center, color="white"):
    """สร้างภาพข้อความและวางกึ่งกลางตำแหน่งที่รับมา."""
    image = font.render(text, True, color)
    surface.blit(image, image.get_rect(center=center))

# --- Your turn 1: หลังพิมพ์ Function ตัวอย่างตาม ให้ลองเรียก Function ---
# เรียก draw_text() ในส่วน DRAW เพื่อเพิ่มชื่อผู้สร้างที่ (400, 170)

def draw_button(surface, text, rect, color=(245, 180, 70)):
    """วาดปุ่มหนึ่งปุ่มและ return Rect สำหรับตรวจ click."""
    pygame.draw.rect(surface, color, rect, border_radius=10)
    draw_text(surface, text, rect.center, (25, 30, 40))
    return rect

# --- Your turn 2: สร้าง Function หลังเข้าใจ draw_button ตัวอย่าง ---
# เขียน draw_panel(surface, rect, color) สำหรับวาดกรอบมน

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((25, 34, 65))
    screen.blit(monster_image, (40, 280))
    draw_text(screen, "REUSABLE UI FUNCTIONS", (400, 120))
    draw_button(screen, "PLAY", pygame.Rect(300, 230, 200, 65))
    draw_button(screen, "RESET", pygame.Rect(300, 320, 200, 65), (90, 200, 155))

    # --- Your turn 3: Reuse ---
    # เรียก draw_button() เพิ่มปุ่ม QUIT โดยไม่คัดลอกโค้ดใน Function
    pygame.display.flip()
pygame.quit()

# RUN CHECKPOINT: เปลี่ยน Arguments แล้ว UI เปลี่ยนโดยไม่แก้โค้ดใน Function

# === Your Turn ===
# TODO 1: สร้าง draw_title() ที่มี Default Argument
# TODO 2: สร้าง draw_score() ที่รับ score
# TODO 3: วาดหน้าจอโดยไม่มีคำสั่ง render() ซ้ำอยู่นอก Functions

# คำถาม: Parameters ทำให้ Function เดียวสร้าง UI ที่ต่างกันได้อย่างไร?
# Exit ticket: Function ใดควรทดสอบได้โดยไม่ต้องเปิดหน้าต่าง Pygame?
