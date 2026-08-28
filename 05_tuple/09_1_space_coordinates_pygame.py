"""Upgrade 07_1_space_coordinates_game.py เป็น Space Coordinates Pygame.

Tuple คือ DATA คงที่; EVENT เลือกพิกัด; DRAW unpack ข้อมูลเดิมมาวาดแผนที่
input ชื่อจุดกลายเป็น click; print ผลภารกิจกลายเป็น message บนหน้าจอ
"""
from pathlib import Path
import pygame
pygame.init()
screen = pygame.display.set_mode((850, 520))
font = pygame.font.Font(None, 32)
# Crop รูปดาวสามช่องจาก atlas; ลำดับตรงกับ destinations
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
moon_image = pygame.transform.smoothscale(atlas.subsurface(pygame.Rect(0, 0, 341, 384)), (96, 96))
mars_image = pygame.transform.smoothscale(atlas.subsurface(pygame.Rect(341, 0, 341, 384)), (96, 96))
saturn_image = pygame.transform.smoothscale(atlas.subsurface(pygame.Rect(682, 0, 342, 384)), (110, 96))
planet_images = (moon_image, mars_image, saturn_image)
# DATA: หนึ่ง nested Tuple เก็บชื่อและ (x, y) ของทุกจุด
destinations = (("moon", 180, 220), ("mars", 425, 150), ("saturn", 680, 290))
message = "MISSION: LAND ON MARS"
running = True
while running:
    # EVENT: ตรวจว่า click อยู่ใน Rect รอบพิกัดดาวใด
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for planet, x, y in destinations:
                if pygame.Rect(x - 50, y - 50, 100, 100).collidepoint(event.pos):
                    message = "LANDED ON MARS!" if planet == "mars" else "WRONG COORDINATES!"
    # DRAW: unpack Tuple แล้ววาดดาวจากข้อมูลชุดเดียวกัน
    screen.fill((15, 20, 50))
    image_index = 0
    for planet, x, y in destinations:
        screen.blit(planet_images[image_index], (x - 48, y - 48))
        screen.blit(font.render(planet.upper(), True, "white"), (x - 40, y + 60))
        image_index += 1
    screen.blit(font.render(message, True, "white"), (270, 455))
    pygame.display.flip()
pygame.quit()

# Creative Challenge: เปลี่ยน destination tuples เป็น treasure map ของตัวเอง
