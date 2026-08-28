"""Upgrade 11_1_dice_battle_game.py เป็น Dice Battle Pygame.

เก็บ roll/battle Functions, player_name, rounds และ wins จาก Terminal ครบ;
input ชื่อ/จำนวนรอบยังถามใน Terminal ส่วนการเล่นแต่ละรอบใช้ ROLL button;
print ผลแต่ละรอบกลายเป็น draw_text() โดยไม่เขียนกติกาซ้ำ
"""
import random
from pathlib import Path
import pygame

# COPY input() จาก Terminal Version ก่อนเปิดหน้าต่าง
player_name = input("Hero name: ").strip()
try:
    rounds = int(input("How many rounds? "))
except ValueError:
    print("Rounds must be a whole number.")
    raise SystemExit

pygame.init()
screen = pygame.display.set_mode((850, 560))
font = pygame.font.Font(None, 34)
big_font = pygame.font.Font(None, 88)
roll_button = pygame.Rect(325, 410, 200, 65)
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
monster_image = atlas.subsurface(pygame.Rect(0, 1152, 341, 384))
monster_image = pygame.transform.smoothscale(monster_image, (150, 170))

def roll_dice():
    """Game logic: สุ่มและ return ผล โดยไม่รู้จักหน้าจอ."""
    return random.randint(1, 6)

def battle(player_name, monster_name="Dragon"):
    """Game logic เดิม: รับชื่อและ return ลูกเต๋าทั้งสองกับผลหนึ่งค่า."""
    player, monster = roll_dice(), roll_dice()
    if player > monster:
        result = "YOU WIN!"
    elif player < monster:
        result = "MONSTER WINS!"
    else:
        result = "DRAW!"
    return player, monster, result

def draw_text(text, center, used_font=font, color="white"):
    """UI logic: วาดข้อความโดยไม่ทำให้ค่าของเกมเปลี่ยน."""
    image = used_font.render(text, True, color)
    screen.blit(image, image.get_rect(center=center))

player_roll, monster_roll = 0, 0
round_number = 0
wins = 0
message = "Click ROLL to start round 1"
running = True
while running:
    # EVENT เปลี่ยนข้อมูลโดยเรียก game logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if roll_button.collidepoint(event.pos) and round_number < rounds:
                round_number += 1
                player_roll, monster_roll, result = battle(player_name)
                if result == "YOU WIN!":
                    wins += 1
                message = result
                if round_number == rounds:
                    message = result + "  BATTLE COMPLETE"
    # DRAW อ่านข้อมูลและแสดงผลเท่านั้น
    screen.fill((30, 33, 66))
    draw_text("DICE BATTLE", (425, 65))
    draw_text(str(player_roll), (240, 230), big_font, (90, 215, 255))
    draw_text(str(monster_roll), (610, 230), big_font, (255, 110, 110))
    screen.blit(monster_image, (650, 170))
    draw_text(player_name.upper(), (240, 320))
    draw_text("DRAGON", (610, 320))
    pygame.draw.rect(screen, (245, 185, 70), roll_button, border_radius=12)
    draw_text("ROLL", roll_button.center, font, (25, 30, 40))
    draw_text("Round: " + str(round_number) + "/" + str(rounds), (220, 370))
    draw_text("Wins: " + str(wins), (630, 370))
    draw_text(message, (425, 520), pygame.font.Font(None, 28))
    pygame.display.flip()
pygame.quit()

# TEST Terminal → Pygame: ชื่อ, จำนวนรอบ, ผล battle และ wins ต้องใช้กติกาเดิม
# Creative Challenge: เพิ่ม reset_game() โดยไม่แก้ battle() ของเดิม
