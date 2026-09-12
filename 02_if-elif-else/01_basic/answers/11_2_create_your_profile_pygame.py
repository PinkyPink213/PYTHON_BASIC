"""ตัวอย่างเฉลย 11.2 — Convert Space Hero Profile จาก Answer 09.2

รักษา input, Variables, String และสูตรจาก 09_2 ไว้เหมือนเดิม
แล้วเปลี่ยนเฉพาะ Output จาก print() เป็น Pygame โดยยังไม่ใช้ if/for/while
"""

import pygame


# COPY DATA + GAME LOGIC จาก Answer 09.2
name = input("What is your name? ").strip()
planet = input("Choose a home planet: ").strip().title()
power = input("Choose a superpower: ").strip().lower()
age = int(input("How old are you? "))
stars = int(input("How many stars did you collect? "))

# การต่อ String และสูตรยังเป็นกติกาชุดเดิม
hero_name = "Captain " + name
age_next_year = age + 1
bonus_stars = stars * 2


# เพิ่ม PYGAME INTERFACE
pygame.init()
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Space Hero Profile")
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 52)

# สีทั้งหมดเป็น RGB
background_color = (20, 28, 62)
card_color = (82, 68, 148)
star_color = (255, 210, 75)
text_color = (255, 255, 255)


# REPLACE กรอบที่ print() ด้วยพื้นหลังและ Shapes
screen.fill(background_color)
pygame.draw.rect(screen, card_color, (120, 45, 560, 460), border_radius=24)
pygame.draw.circle(screen, star_color, (400, 165), 62)
pygame.draw.circle(screen, background_color, (425, 145), 52)
pygame.draw.line(screen, star_color, (180, 235), (620, 235), 4)
pygame.draw.circle(screen, star_color, (185, 105), 8)
pygame.draw.circle(screen, star_color, (620, 125), 6)
pygame.draw.circle(screen, star_color, (590, 190), 5)


# REPLACE print() แต่ละบรรทัดด้วย render()
title_image = title_font.render("SPACE HERO PROFILE", True, star_color)
hero_image = font.render("Hero: " + hero_name, True, text_color)
planet_image = font.render("Home planet: " + planet, True, text_color)
power_image = font.render("Superpower: " + power, True, text_color)
age_image = font.render("Age next year: " + str(age_next_year), True, text_color)
stars_image = font.render("Bonus stars: " + str(bonus_stars), True, text_color)
close_image = font.render("Press any key to close", True, text_color)

# blit() วางภาพข้อความลงตำแหน่งบน Card
screen.blit(title_image, title_image.get_rect(center=(400, 85)))
screen.blit(hero_image, hero_image.get_rect(center=(400, 275)))
screen.blit(planet_image, planet_image.get_rect(center=(400, 315)))
screen.blit(power_image, power_image.get_rect(center=(400, 355)))
screen.blit(age_image, age_image.get_rect(center=(400, 395)))
screen.blit(stars_image, stars_image.get_rect(center=(400, 435)))
screen.blit(close_image, close_image.get_rect(center=(400, 525)))

pygame.display.flip()


# รอผู้ใช้ก่อนปิด โดยยังไม่ใช้ Conditions หรือ Loops
# click จะไม่ทำให้ Card ปิด เพราะ Chapter 01 ยังไม่เรียน Mouse Event
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.clear()
pygame.event.wait()
pygame.quit()


# === ตรวจ Terminal → Pygame ===
# [x] คำถาม input() เหมือน Answer 09.2 ครบ 5 ข้อ
# [x] hero_name, age_next_year และ bonus_stars ใช้สูตรเดิม
# [x] ข้อความ Hero Card ครบทุกบรรทัด
# [x] เปลี่ยนเฉพาะ Interface จาก print() เป็น Pygame
# [x] ไม่มี if, for หรือ while ก่อนลำดับบท
