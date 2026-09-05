"""เฉลยบทที่ 11.1: Adventure Profile Generator ด้วย Pygame"""

import pygame


# ==================================================
# STEP 1: รับข้อมูลและคำนวณเหมือนเวอร์ชัน Terminal
# ==================================================

name = input("What is your name? ").strip()
age = int(input("How old are you? "))
favorite_animal = input("What is your favorite animal? ").strip().lower()
lucky_number = int(input("What is your lucky number? "))

next_age = age + 1
double_lucky_number = lucky_number * 2
hero_name = name + " the " + favorite_animal.title()


# ==================================================
# STEP 2: เริ่ม Pygame และสร้างหน้าต่าง
# ==================================================

pygame.init()
screen = pygame.display.set_mode((800, 550))

# เฉลย Your turn 1: ตั้งชื่อเกมของเรา
pygame.display.set_caption("My Adventure Profile")


# ==================================================
# STEP 3: สร้าง Font และสี RGB
# ==================================================

title_font = pygame.font.Font(None, 52)
text_font = pygame.font.Font(None, 34)

background_color = (26, 31, 68)
card_color = (91, 70, 150)
text_color = (248, 248, 255)
highlight_color = (255, 215, 80)

# เฉลย Your turn 2: สร้างสีสำหรับ badge
badge_color = (80, 220, 170)


# ==================================================
# STEP 4: เปลี่ยน String ให้เป็นภาพข้อความ
# ==================================================

title_image = title_font.render("YOUR ADVENTURE PROFILE", True, highlight_color)
hero_image = text_font.render("Hero name: " + hero_name, True, text_color)
age_image = text_font.render("Age next year: " + str(next_age), True, text_color)
power_image = text_font.render(
    "Super lucky number: " + str(double_lucky_number), True, text_color
)
story_image = text_font.render("Your adventure begins now!", True, highlight_color)
close_hint_image = text_font.render("Press any key to close", True, text_color)

# เฉลย Your turn 3: สร้างชื่อผู้สร้างและภาพข้อความ
creator_name = "Python Explorer"
creator_image = text_font.render("Created by: " + creator_name, True, text_color)


# ==================================================
# STEP 5-6: วาดพื้นหลัง Card, Avatar และของตกแต่ง
# ==================================================

screen.fill(background_color)
pygame.draw.rect(screen, card_color, (130, 60, 540, 430), border_radius=25)
pygame.draw.circle(screen, highlight_color, (400, 190), 65)
pygame.draw.line(screen, highlight_color, (180, 245), (620, 245), 4)

# เฉลย Your turn 4: วาด badge ให้อยู่ภายใน Card
pygame.draw.circle(screen, badge_color, (610, 105), 18)

# เฉลย Your turn 4.1: วาดเส้นตกแต่งอีกหนึ่งเส้น
pygame.draw.line(screen, badge_color, (250, 455), (550, 455), 3)


# ==================================================
# STEP 7: วางข้อความบน Profile Card
# ==================================================

screen.blit(title_image, title_image.get_rect(center=(400, 105)))
screen.blit(hero_image, hero_image.get_rect(center=(400, 285)))
screen.blit(age_image, age_image.get_rect(center=(400, 330)))
screen.blit(power_image, power_image.get_rect(center=(400, 375)))
screen.blit(story_image, story_image.get_rect(center=(400, 420)))

# เฉลย Your turn 5: วางชื่อผู้สร้างไว้กึ่งกลางด้านล่างของ Card
screen.blit(creator_image, creator_image.get_rect(center=(400, 475)))
screen.blit(close_hint_image, close_hint_image.get_rect(center=(400, 525)))

pygame.display.flip()


# รอให้ผู้ใช้กด Keyboard หรือปิดหน้าต่าง โดยยังไม่ใช้ if/for/while
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.clear()
pygame.event.wait()

pygame.quit()
