"""Milestone: Upgrade Hangman จาก Terminal เป็น Pygame

DATA/logic เดิม: words, secret, hint, used, lives และการตรวจคำตอบ
เปลี่ยน Interface: input() → KEYDOWN, print() → render/blit และรูปหัวใจ
อ่านทีละส่วนแล้วชี้ DATA → EVENT → UPDATE → DRAW ให้ได้ก่อนดัดแปลง
"""
import random
from pathlib import Path
import pygame


def make_new_round(category, categories):
    """สุ่มคำจาก Category ที่ผู้เล่นเลือก แล้วคืนข้อมูลรอบใหม่."""
    word_data = categories[category]
    secret = random.choice(tuple(word_data))
    hint = word_data[secret]
    used = set()
    lives = 6
    return secret, hint, used, lives


def draw_hangman(surface, wrong_guesses):
    """วาดตะแลงแกงและเพิ่มส่วนตัวละครตามจำนวนครั้งที่ทายผิด 0–6."""
    line_color = (235, 240, 255)
    # โครงตะแลงแกงอยู่ตลอด เพื่อให้ผู้เล่นเห็นพื้นที่ของภาพ
    pygame.draw.line(surface, line_color, (610, 315), (810, 315), 8)
    pygame.draw.line(surface, line_color, (660, 315), (660, 90), 8)
    pygame.draw.line(surface, line_color, (660, 90), (770, 90), 8)
    pygame.draw.line(surface, line_color, (770, 90), (770, 125), 6)

    # แต่ละ if เพิ่มภาพหนึ่งส่วนเมื่อ wrong_guesses ถึงค่านั้น
    if wrong_guesses >= 1:
        pygame.draw.circle(surface, (255, 210, 100), (770, 155), 30, 5)
    if wrong_guesses >= 2:
        pygame.draw.line(surface, (255, 210, 100), (770, 185), (770, 255), 6)
    if wrong_guesses >= 3:
        pygame.draw.line(surface, (255, 210, 100), (770, 200), (730, 225), 6)
    if wrong_guesses >= 4:
        pygame.draw.line(surface, (255, 210, 100), (770, 200), (810, 225), 6)
    if wrong_guesses >= 5:
        pygame.draw.line(surface, (255, 210, 100), (770, 255), (735, 295), 6)
    if wrong_guesses >= 6:
        pygame.draw.line(surface, (255, 210, 100), (770, 255), (805, 295), 6)


# SETUP — ทำครั้งเดียว: หน้าต่าง Font และ asset
pygame.init()
screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Hangman Pygame")
font = pygame.font.Font(None, 38)
big_font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()

atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
# Rect เลือกช่อง Heart จาก atlas แล้ว scale ให้พอดีกับแถบชีวิต
heart_image = atlas.subsurface(pygame.Rect(341, 1152, 341, 384))
heart_image = pygame.transform.smoothscale(heart_image, (48, 48))

# DATA — Nested Dictionary: Category → Word → Hint
categories = {
    "animals": {"rabbit": "long ears", "tiger": "orange and black stripes"},
    "food": {"pizza": "cheese on a round base", "sushi": "rice and seaweed"},
    "space": {"saturn": "has rings", "rocket": "travels beyond Earth"},
}
category = ""
secret = ""
hint = ""
used = set()
lives = 6
message = "Choose: 1 ANIMALS   2 FOOD   3 SPACE"
choosing_category = True
game_over = False

running = True
while running:
    # EVENT — รับการปิดหน้าต่าง, Restart และตัวอักษร
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Restart กลับมาให้เลือกหมวดใหม่ ไม่สุ่มหมวดแทนผู้เล่น
            category = ""
            secret = ""
            hint = ""
            used = set()
            lives = 6
            message = "Choose: 1 ANIMALS   2 FOOD   3 SPACE"
            choosing_category = True
            game_over = False

        elif event.type == pygame.KEYDOWN and choosing_category:
            # ปุ่ม 1/2/3 ทำหน้าที่แทน input("Choose a category")
            if event.key == pygame.K_1:
                category = "animals"
            elif event.key == pygame.K_2:
                category = "food"
            elif event.key == pygame.K_3:
                category = "space"

            if category != "":
                secret, hint, used, lives = make_new_round(category, categories)
                message = "Type one English letter"
                choosing_category = False

        elif event.type == pygame.KEYDOWN and not game_over:
            # event.unicode เป็น String ของปุ่มที่พิมพ์; lower() ทำให้เทียบง่าย
            letter = event.unicode.lower()

            # รับเฉพาะหนึ่งตัวอักษรและไม่เคยอยู่ใน Set used
            valid_letter = len(letter) == 1 and letter.isalpha()
            if not valid_letter:
                message = "Please type one English letter"
            elif letter in used:
                message = "You already tried " + letter.upper()
            else:
                used.add(letter)
                if letter in secret:
                    message = "Good guess!"
                else:
                    lives -= 1
                    message = "Not in the word"

    # UPDATE — สร้างข้อความคำที่เปิดแล้วจาก secret และ used
    shown = ""
    won = False
    if not choosing_category:
        won = True
        for letter in secret:
            if letter in used:
                shown += letter + " "
            else:
                shown += "_ "
                won = False

    # ตรวจตอนจบหลัง update เพื่อให้ตัวอักษรล่าสุดมีผลทันที
    if won and not choosing_category:
        message = "YOU WIN! Press R for a new word"
        game_over = True
    elif lives == 0:
        message = "GAME OVER: " + secret.upper() + " — Press R"
        game_over = True

    # CHECKPOINT: ชี้ค่าของ used/lives/shown ก่อนดูภาพบนจอ

    # DRAW — อ่าน DATA ล่าสุดแล้ววาดหนึ่ง frame
    screen.fill((26, 32, 65))
    if choosing_category:
        screen.blit(big_font.render("CHOOSE A CATEGORY", True, (100, 220, 255)), (210, 160))
        screen.blit(font.render("1  ANIMALS", True, "white"), (330, 260))
        screen.blit(font.render("2  FOOD", True, "white"), (330, 310))
        screen.blit(font.render("3  SPACE", True, "white"), (330, 360))
    else:
        screen.blit(font.render("Category: " + category.upper(), True, (255, 215, 90)), (90, 55))
        screen.blit(font.render("Hint: " + hint, True, "white"), (90, 100))
    screen.blit(big_font.render(shown.upper(), True, (100, 220, 255)), (170, 245))
    screen.blit(font.render("Used: " + str(used), True, "white"), (90, 370))

    # lives ลดลงเมื่อทายผิด จึงคำนวณจำนวนส่วนของรูปได้โดยไม่เก็บ DATA ซ้ำ
    wrong_guesses = 6 - lives
    if not choosing_category:
        draw_hangman(screen, wrong_guesses)

    # จำนวนรูปหัวใจมาจาก lives โดยตรง จึงไม่ต้องเก็บ UI state ซ้ำอีกชุด
    if not choosing_category:
        for heart_number in range(lives):
            heart_x = 90 + heart_number * 55
            screen.blit(heart_image, (heart_x, 430))

    screen.blit(font.render(message, True, (255, 215, 90)), (90, 535))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Exit ticket
# 1. KEYDOWN แทน input() อย่างไร และ render/blit แทน print() อย่างไร?
# 2. เพราะอะไร used เหมาะกับ Set?
# 3. กด R แล้วค่าใดถูกสร้างใหม่ และ asset ใดยังคงใช้เดิม?
# 4. Creative idea ของเราจะเปลี่ยน DATA, logic หรือ UI ส่วนใด?
