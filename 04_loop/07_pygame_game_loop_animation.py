"""Pygame Basic: EVENT → UPDATE → DRAW, FPS และ Animation.

เป้าหมายวันนี้ไม่ใช่จำคำสั่ง แต่เล่าได้ว่า 1 frame ทำ 3 งานอะไรบ้าง
ก่อน Run ทุก Practice: ทายค่าข้อมูล → ทายตำแหน่งภาพ → จึงทดลอง
พิมพ์ Example Game Loop ให้ทำงานก่อน แล้วทำ Your turn/TODO ทีละจุด
"""
from pathlib import Path
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)
x = 80
speed = 4
key_message = "Press SPACE"
# Asset atlas คือรูปใหญ่ที่รวมรูปย่อยหลายช่องไว้ในไฟล์เดียว
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
# Atlas มีฉากทึบจึงใช้ convert(); icon PNG โปร่งใสใน Chapter 02 ใช้ convert_alpha()
atlas = pygame.image.load(atlas_path).convert()

# subsurface(Rect) crop พื้นที่ (x, y, width, height) ออกจาก atlas
# Rect นี้เลือก Hero ช่องซ้ายของแถวที่ 2
hero_image = atlas.subsurface(pygame.Rect(0, 384, 341, 384))
# smoothscale() ย่อรูปที่ crop แล้วให้เหมาะกับหน้าจอเกม
hero_image = pygame.transform.smoothscale(hero_image, (90, 100))

# --- Your turn 1: Asset ---
# TODO 1: หลังพิมพ์ตัวอย่าง Asset ตามแล้ว เปลี่ยน x จาก 0 เป็น 341
# ทายก่อน Run ว่าตัวละครจะเปลี่ยน แต่ animation x จะยังทำงานเหมือนเดิมหรือไม่
# RUN CHECKPOINT 1: ตัวละครเปลี่ยน แต่การเคลื่อนที่ยังเหมือนเดิม

# --- Your turn 2: Animation Data ---
# หลังพิมพ์ DATA ตัวอย่างตาม ให้สร้าง y = 250 และ player_color เป็น RGB ของเรา

running = True
while running:
    # TRACE: ใช้นิ้วตามลำดับ EVENT → UPDATE → DRAW หนึ่งรอบก่อน Run
    # 1) EVENT: รับสิ่งที่เกิดจากผู้เล่น/หน้าต่าง
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYDOWN เกิดหนึ่งครั้งเมื่อเริ่มกดปุ่ม เหมาะกับคำสั่งที่ทำครั้งเดียว
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                key_message = "SPACE pressed"

            # event.unicode คือ String ที่ผู้เล่นพิมพ์ เช่น "a"
            # isalpha() ตรวจว่า String นั้นเป็นตัวอักษรหรือไม่ ใช้ต่อใน Hangman
            typed_letter = event.unicode.lower()
            if typed_letter.isalpha():
                key_message = "Letter: " + typed_letter

            # Your turn 3 — TODO: หลังเข้าใจ KEYDOWN ให้เพิ่ม if event.key == pygame.K_r
            # แล้ว reset x = 80 ทายตำแหน่งก่อนกด Run
    # 2) UPDATE: เปลี่ยนข้อมูลเกม
    x += speed
    if x > 770 or x < 30:
        speed *= -1

    # --- Your turn 4: UPDATE ---
    # เพิ่ม y ทีละ 1 ทุก frame แล้วสังเกตทิศทาง
    # 3) DRAW: วาดข้อมูลล่าสุด
    screen.fill((22, 28, 62))
    pygame.draw.circle(screen, (90, 215, 255), (x, 250), 30)
    screen.blit(hero_image, (x - 45, 200))
    screen.blit(font.render(key_message, True, "white"), (30, 30))

    # --- Your turn 5: DRAW ---
    # วาดวงกลมอีกลูกโดยใช้ y และ player_color จาก Practice 1
    pygame.display.flip()
    clock.tick(60)  # จำกัดประมาณ 60 frames ต่อวินาที
pygame.quit()

# RUN CHECKPOINT 2: ชี้ EVENT/UPDATE/DRAW ได้ วัตถุขยับ กด R reset และปิดได้

# === Your Turn ===
# TODO 1: ใช้ KEYDOWN + K_r reset x เหมือน Practice ที่เรียนแล้ว
# TODO 2: ป้องกันวัตถุออกนอกหน้าจอด้วย if
# TODO 3: วาดดาวหลายดวงด้วย for loop
# TODO 4: เปลี่ยน speed และ FPS แล้วอธิบายผลที่ต่างกัน

# คำถาม: EVENT, UPDATE และ DRAW ต่างกันอย่างไร?
# Exit ticket: ถ้าลบ UPDATE ภาพจะเป็นอย่างไร? ถ้าลบ flip() จะเป็นอย่างไร?
# KEYDOWN, event.key และ event.unicode ให้ข้อมูลต่างกันอย่างไร?
