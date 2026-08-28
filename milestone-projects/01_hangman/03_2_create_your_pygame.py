"""สร้าง Pygame Hangman ของเรา — ทำ STEP ตรงกับ 03_1 ทีละส่วน

เปิด 3 ไฟล์ข้างกัน:
- 02_create_your_game.py = DATA และกติกาของเรา
- 03_1_play_pygame.py = Pygame pattern ที่เพิ่งพิมพ์ตาม
- ไฟล์นี้ = พื้นที่ Upgrade ผลงานของเรา

กติกา: COPY DATA/logic ของเรา, LOOK ตัวอย่าง, TYPE ใหม่ด้วยมือ,
REPLACE input/print และ RUN CHECKPOINT หลังทุก STEP
"""
import random
from pathlib import Path
import pygame


# ==================================================
# STEP 1 — CATEGORY DATA (ตรงกับ DATA ใน 03_1)
# ==================================================
# TODO: คัดลอก Nested Dictionary จาก Terminal Version ของเรา
# LOOK: เทียบ STEP 1 ใน 03_1 แต่ใช้ Category/คำ/Hint ของเราเท่านั้น
# อย่างน้อย 3 Categories หมวดละ 3 คำ และทุกคำต้องมี Hint
categories = {
    "my_category": {
        "python": "a programming language",
    },
}
# RUN CHECKPOINT: print categories แล้วตรวจอย่างน้อย 3 หมวด หมวดละ 3 คำ

# เขียน Design Note ก่อนเริ่ม:
# ชื่อเกม: ____________________
# Categories: ____________________
# เรื่องราว/เป้าหมาย: ____________________


# ==================================================
# STEP 2 — make_new_round() (ตรงกับ Function แรกใน 03_1)
# ==================================================
def make_new_round(category, category_data):
    """TODO: สุ่มคำเฉพาะจาก Category ที่ผู้เล่นเลือก."""
    # Pattern ที่เพิ่งเรียน:
    # word_data = category_data[category]
    # secret = random.choice(tuple(word_data))
    # hint = word_data[secret]
    # used = set()
    # lives = จำนวนที่เราออกแบบ
    # return secret, hint, used, lives

    # ค่าเริ่มต้นนี้ทำให้ไฟล์ยัง Run ได้ ให้แทนด้วยโค้ดของเราด้านบน
    secret = "python"
    hint = "a programming language"
    used = set()
    lives = 6
    return secret, hint, used, lives


# RUN CHECKPOINT: Function รับอะไร/return อะไร และสุ่มอยู่ในหมวดที่เลือกหรือไม่?


# ==================================================
# STEP 3 — draw_hangman() (ตรงกับ Function ที่สองใน 03_1)
# ==================================================
def draw_hangman(surface, wrong_guesses):
    """TODO: วาดภาพเพิ่มตาม wrong_guesses โดยใช้ Shapes ที่เคยเรียน."""
    # พิมพ์โครงตะแลงแกงก่อน แล้ว Run ดูตำแหน่ง
    pygame.draw.line(surface, "white", (610, 315), (810, 315), 8)
    pygame.draw.line(surface, "white", (660, 315), (660, 90), 8)

# TODO: เพิ่มคาน เชือก หัว ตัว แขน และขาด้วย if wrong_guesses >= ...
# RUN CHECKPOINT: เรียกด้วย 0–6 แล้วรูปต้องเพิ่มทีละส่วน ไม่โผล่ครบตั้งแต่แรก




# ==================================================
# STEP 4 — SETUP + ASSET (ตรงกับ SETUP ใน 03_1)
# ==================================================
pygame.init()
screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("My Category Hangman")
font = pygame.font.Font(None, 38)
big_font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()

# TODO: เลือก Heart/Star/Pet/Space จาก atlas หรือใช้ภาพที่วาดเอง
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
heart_image = atlas.subsurface(pygame.Rect(341, 1152, 341, 384))
heart_image = pygame.transform.smoothscale(heart_image, (48, 48))
# RUN CHECKPOINT: หน้าต่างและ asset เปิดได้โดยไม่มี FileNotFoundError


# ==================================================
# STEP 5 — GAME STATE + CATEGORY SCREEN
# ==================================================
category = ""
secret = ""
hint = ""
used = set()
lives = 6
message = "Choose a category"
choosing_category = True
game_over = False

# TODO: กำหนด Rect buttons ให้ครบตาม Categories ของเรา
category_button = pygame.Rect(300, 250, 300, 70)
# RUN CHECKPOINT: หน้าเลือก Category ต้องเห็นปุ่มครบก่อนเริ่ม Game Loop


# ==================================================
# STEP 6 — GAME LOOP: EVENT
# ==================================================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TODO 6A: เมื่อเลือก Category
        # 1. ตรวจ category_button.collidepoint(event.pos)
        # 2. เปลี่ยน category เป็น Key จริงจาก categories
        # 3. เรียก make_new_round(category, categories)
        # 4. เปลี่ยน choosing_category = False



        # TODO 6B: เมื่อกด KEYDOWN ระหว่างเล่น
        # ย้าย logic ตรวจหนึ่งตัวอักษร/คำตอบซ้ำ/ถูก/ผิดจาก Terminal Version
        # ใช้ event.unicode.lower() แทน input()



        # TODO 6C: เมื่อกด R หลังจบเกม
        # reset ค่าและกลับหน้าเลือก Category เพื่อเปลี่ยนหัวข้อได้
# RUN CHECKPOINT: ทดสอบเลือกหมวด, กดถูก, กดผิด, กดซ้ำ และ R ทีละกรณี



    # ==================================================
    # STEP 7 — UPDATE WORD + WIN/LOSE
    # ==================================================
    shown = ""
    won = False

    # TODO: ใช้ for letter in secret สร้าง shown จาก used
    # TODO: ตรวจ won และ lives == 0 ด้วย logic เดิม



    # ==================================================
    # STEP 8 — DRAW CATEGORY OR GAME
    # ==================================================
    screen.fill((26, 32, 65))

    if choosing_category:
        # หน้าแรกต้องบอกชัดว่าผู้เล่นเลือกหัวข้ออย่างไร
        title = big_font.render("CHOOSE A CATEGORY", True, (100, 220, 255))
        screen.blit(title, (210, 150))
        pygame.draw.rect(screen, (255, 190, 80), category_button, border_radius=12)
        button_text = font.render("MY CATEGORY", True, (30, 30, 45))
        screen.blit(button_text, button_text.get_rect(center=category_button.center))

        # TODO: วาดปุ่มให้ครบทุก Category โดยใช้ข้อความของเรา


    else:
        # TODO: render/blit Category, Hint, shown, used และ message
        screen.blit(font.render("Category: " + category.upper(), True, "white"), (90, 55))
        screen.blit(font.render("Hint: " + hint, True, "white"), (90, 100))

        wrong_guesses = 6 - lives
        draw_hangman(screen, wrong_guesses)

        # TODO: วาด heart_image ตาม lives ด้วย for loop


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# RUN CHECKPOINT: เล่นได้ถึง Win และ Lose; หน้าต่างไม่ดับก่อนจบ


# ==================================================
# STEP 9 — TEST เทียบ Terminal → Pygame
# ==================================================
# [ ] เลือกได้ทุก Category
# [ ] secret และ hint มาจาก Category ที่เลือกจริง
# [ ] ตัวอักษรถูกเปิดครบทุกตำแหน่ง
# [ ] ตัวอักษรซ้ำไม่ลด lives
# [ ] ตัวผิดลด lives และเพิ่มส่วนของรูป Hangman
# [ ] มี Win และ Game Over
# [ ] กด R กลับหน้า Category และเปลี่ยนหมวดได้
# [ ] ผลการตัดสินเหมือน Terminal Version


# ==================================================
# STEP 10 — CREATIVE STUDIO
# ==================================================
# เลือกอย่างน้อย 2 ข้อหลัง Core ผ่าน:
# [ ] Theme/Category/คำศัพท์และ Hint ที่เด็กแต่งเอง
# [ ] ภาพ Hangman หรือตัวละครแบบใหม่
# [ ] สี ฉาก Heart/Star และข้อความให้เป็นเรื่องเดียวกัน
# [ ] Difficulty ที่เปลี่ยน lives
# [ ] Bonus Hint หรือ Score พร้อมอธิบายกติกาก่อนเขียน
# CREATIVE GAME RULES: เป้าหมาย ___ ผู้เล่นตัดสินใจอะไร ___ ชนะ ___ แพ้ ___
# [ ] ออกแบบกติกาใหม่ 1 ข้อที่มีผลจริง เช่น Hint แลก Life หรือ Bonus Word
# [ ] เขียนก่อนทำว่าแก้ DATA ___ / LOGIC FUNCTION ___ / EVENT ___ / DRAW ___

# อธิบายผลงาน:
# DATA ที่ฉันออกแบบคือ ____________________
# Logic ที่ฉันเพิ่มคือ ____________________
# UI ที่ฉันเปลี่ยนคือ ____________________
# TRANSFER: ให้เพื่อนเล่นโดยไม่อธิบาย แล้วจด 1 จุดที่ผู้เล่นงงและปรับ UI
