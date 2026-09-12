"""บทที่ 8.1: Upgrade Mystery Animal Shop จาก Terminal เป็น Pygame

เกมเดิมยังใช้ choice, price และ if/elif/else ชุดเดิม
เราเปลี่ยน input เป็น click และ print เป็นข้อความ/ภาพบนจอเท่านั้น
Chapter 02 ยังไม่เรียน List/Loop จึงเขียน 3 ปุ่มทีละปุ่มและเล่นหนึ่งรอบ
"""
from pathlib import Path
import pygame

# DATA — คัดลอกมาจาก Terminal Version
secret_animal = "rabbit"
secret_price = 500
message = "Hint: It has long ears"

pygame.init()
screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Mystery Animal Shop")
title_font = pygame.font.Font(None, 52)
font = pygame.font.Font(None, 31)

image_path = Path(__file__).parent / "assets" / "animals" / "animal_choices.png"
picture = pygame.image.load(image_path).convert_alpha()
picture = pygame.transform.smoothscale(picture, (600, 338))

cat_button = pygame.Rect(125, 455, 190, 55)
rabbit_button = pygame.Rect(355, 455, 190, 55)
dog_button = pygame.Rect(585, 455, 190, 55)

# DRAW รอบแรก — แสดงคำใบ้และตัวเลือกก่อนรับ EVENT
screen.fill((25, 31, 65))
screen.blit(title_font.render("MYSTERY ANIMAL", True, (255, 220, 95)), (250, 25))
screen.blit(picture, (150, 80))
pygame.draw.rect(screen, (92, 190, 210), cat_button, border_radius=10)
pygame.draw.rect(screen, (92, 190, 210), rabbit_button, border_radius=10)
pygame.draw.rect(screen, (92, 190, 210), dog_button, border_radius=10)
screen.blit(font.render("CAT", True, (20, 30, 45)), (195, 473))
screen.blit(font.render("RABBIT", True, (20, 30, 45)), (405, 473))
screen.blit(font.render("DOG", True, (20, 30, 45)), (650, 473))
screen.blit(font.render(message, True, "white"), (270, 560))
pygame.display.flip()

# EVENT 1 — click แทน input("animal?")
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
selected_animal = ""
event = pygame.event.wait()
if event.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
elif event.type == pygame.MOUSEBUTTONDOWN:
    if cat_button.collidepoint(event.pos):
        selected_animal = "cat"
    elif rabbit_button.collidepoint(event.pos):
        selected_animal = "rabbit"
    elif dog_button.collidepoint(event.pos):
        selected_animal = "dog"

# กิน MOUSEBUTTONUP ของ click สัตว์ก่อนเปิดฉากราคา
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
pygame.event.wait()
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

# LOGIC เดิม — Pygame ไม่ได้มาแทน if/elif/else
if selected_animal == secret_animal:
    message = "Correct! Now choose a price"
else:
    message = "Not this animal — run and try again"

# หากทายสัตว์ถูก จึงวาดปุ่มราคาสำหรับ EVENT ที่ 2
if selected_animal == secret_animal:
    price_300 = pygame.Rect(215, 535, 140, 50)
    price_500 = pygame.Rect(380, 535, 140, 50)
    price_700 = pygame.Rect(545, 535, 140, 50)
    pygame.draw.rect(screen, (255, 190, 70), price_300, border_radius=10)
    pygame.draw.rect(screen, (255, 190, 70), price_500, border_radius=10)
    pygame.draw.rect(screen, (255, 190, 70), price_700, border_radius=10)
    screen.blit(font.render("300", True, (35, 30, 45)), (260, 552))
    screen.blit(font.render("500", True, (35, 30, 45)), (425, 552))
    screen.blit(font.render("700", True, (35, 30, 45)), (590, 552))
    pygame.display.flip()

    # EVENT 2 — click ราคา แล้วใช้ if/elif/else เปรียบเทียบตัวเลข
    selected_price = 0
    price_event = pygame.event.wait()
    if price_event.type == pygame.QUIT:
        pygame.quit()
        raise SystemExit
    elif price_event.type == pygame.MOUSEBUTTONDOWN:
        if price_300.collidepoint(price_event.pos):
            selected_price = 300
        elif price_500.collidepoint(price_event.pos):
            selected_price = 500
        elif price_700.collidepoint(price_event.pos):
            selected_price = 700

    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
    pygame.event.wait()
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    pygame.event.clear()

    if selected_price == secret_price:
        message = "PERFECT PRICE! YOU WIN!"
    elif selected_price < secret_price:
        message = "The price is too low"
    else:
        message = "The price is too high"

# DRAW RESULT — render/blit แทน print ตอนจบ
pygame.draw.rect(screen, (25, 31, 65), (0, 590, 900, 60))
screen.blit(font.render(message, True, "white"), (220, 610))
pygame.display.flip()
pygame.event.wait()
pygame.quit()

# Exit ticket: วง DATA, EVENT, LOGIC และ DRAW อย่างละหนึ่งส่วน
