"""Upgrade 08_1_rescue_team_game.py เป็น Rescue Team Pygame.

Set/required skills/operations คือ logic เดิม; input กลายเป็น Card click;
print ผลภารกิจกลายเป็น message และยังไม่ใช้ Dictionary ก่อน Chapter 07
"""
from pathlib import Path
import pygame

pygame.init()
screen = pygame.display.set_mode((900, 570))
font = pygame.font.Font(None, 28)
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
hero_banner = atlas.subsurface(pygame.Rect(0, 384, 1024, 384))
hero_banner = pygame.transform.smoothscale(hero_banner, (600, 105))

heroes = ("aqua", "flash", "rock", "sky")
aqua_skills = {"swim", "heal"}
flash_skills = {"run", "electricity"}
rock_skills = {"strength", "shield"}
sky_skills = {"fly", "see far"}
selected = set()

hero_buttons = [pygame.Rect(55, 120, 175, 75), pygame.Rect(260, 120, 175, 75),
                pygame.Rect(465, 120, 175, 75), pygame.Rect(670, 120, 175, 75)]
flood_button = pygame.Rect(170, 330, 160, 60)
mountain_button = pygame.Rect(370, 330, 160, 60)
city_button = pygame.Rect(570, 330, 160, 60)
message = "Choose heroes, then choose a mission"

running = True
while running:
    # EVENT + UPDATE: click เปลี่ยน selected หรือเริ่มตรวจภารกิจ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # ใช้ index เชื่อม Tuple ชื่อกับ List ปุ่ม โดยไม่ต้องใช้ zip()
            for index in range(4):
                hero = heroes[index]
                if hero_buttons[index].collidepoint(event.pos):
                    if hero in selected:
                        selected.remove(hero)
                    else:
                        selected.add(hero)

            # รวม skills ของสมาชิกที่เลือกด้วย update() ของ Set
            team_skills = set()
            for hero in selected:
                if hero == "aqua":
                    team_skills.update(aqua_skills)
                elif hero == "flash":
                    team_skills.update(flash_skills)
                elif hero == "rock":
                    team_skills.update(rock_skills)
                else:
                    team_skills.update(sky_skills)

            required_skills = set()
            if flood_button.collidepoint(event.pos):
                required_skills = {"swim", "heal"}
            elif mountain_button.collidepoint(event.pos):
                required_skills = {"fly", "strength"}
            elif city_button.collidepoint(event.pos):
                required_skills = {"run", "shield"}

            # Terminal Version ยอมเริ่มภารกิจเมื่อเลือกครบ 3 คนเท่านั้น
            # UI จึงต้องรักษากติกานี้ ไม่ใช่ให้ทีม 1–2 คนข้ามไปได้
            if len(required_skills) > 0 and len(selected) != 3:
                message = "Choose exactly 3 different heroes first"
            elif len(required_skills) > 0:
                missing = required_skills - team_skills
                if len(missing) == 0:
                    message = "MISSION COMPLETE!"
                else:
                    message = "Missing: " + str(missing)

    # DRAW: สี Hero อ่านจาก membership ใน selected
    screen.fill((24, 37, 65))
    screen.blit(hero_banner, (150, 5))
    for index in range(4):
        hero = heroes[index]
        button = hero_buttons[index]
        color = (90, 110, 145)
        if hero in selected:
            color = (75, 195, 140)
        pygame.draw.rect(screen, color, button, border_radius=12)
        label = font.render(hero.upper(), True, "white")
        screen.blit(label, label.get_rect(center=button.center))

    pygame.draw.rect(screen, (245, 180, 70), flood_button, border_radius=10)
    pygame.draw.rect(screen, (245, 180, 70), mountain_button, border_radius=10)
    pygame.draw.rect(screen, (245, 180, 70), city_button, border_radius=10)
    screen.blit(font.render("FLOOD", True, (25, 30, 40)), (215, 352))
    screen.blit(font.render("MOUNTAIN", True, (25, 30, 40)), (395, 352))
    screen.blit(font.render("CITY", True, (25, 30, 40)), (625, 352))
    screen.blit(font.render(message, True, "white"), (120, 480))
    pygame.display.flip()

pygame.quit()

# Exit ticket: update() ทำ union และ required_skills - team_skills ทำ difference อย่างไร?
