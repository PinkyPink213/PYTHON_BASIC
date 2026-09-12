"""Upgrade 06_1_mystery_animal_while_game.py เป็น Mystery Animal Pygame.

DATA/เงื่อนไขมาจาก Terminal; Pygame เพิ่ม EVENT, UPDATE และ DRAW ต่อ frame
while ถามซ้ำเดิมกลายเป็น Game Loop; input กลายเป็น Rect click; print เป็น message
"""
from pathlib import Path
import pygame

pygame.init()
screen = pygame.display.set_mode((850, 560))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 34)
mystery_font = pygame.font.Font(None, 150)
# ใช้ Pet row จาก asset atlas ที่ฝึก crop ในไฟล์ 07
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
rabbit_image = atlas.subsurface(pygame.Rect(682, 768, 342, 384))
rabbit_image = pygame.transform.smoothscale(rabbit_image, (170, 190))
animals = ["cat", "rabbit", "dog"]
hints = ["It has long ears.", "Choose cat, rabbit, or dog.", "Starts with R."]
buttons = [pygame.Rect(115, 380, 180, 60), pygame.Rect(335, 380, 180, 60),
           pygame.Rect(555, 380, 180, 60)]
attempts = 0
message = hints[0]
bob_y = 0
bob_speed = 1
game_over = False
show_answer = False
rescued_count = 0
story = "Find the mystery animal before 3 attempts!"

running = True
while running:
    # EVENT: รับการปิดหน้าต่างและ click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # เริ่มรอบใหม่ แต่เก็บ rescued_count เป็นคะแนนรวม
            attempts = 0
            message = hints[0]
            story = "A new animal is hiding in the forest."
            game_over = False
            show_answer = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            for index in range(3):
                animal = animals[index]
                button = buttons[index]
                if button.collidepoint(event.pos):
                    attempts += 1
                    if animal == "rabbit":
                        message = "YOU FOUND THE RABBIT!"
                        story = "You rescue it from the forest! Press R for a new mission."
                        attempts = 3
                        rescued_count += 1
                        game_over = True
                        show_answer = True
                    elif attempts < 3:
                        message = hints[attempts]
                    else:
                        message = "GAME OVER — IT WAS RABBIT"
                        story = "The rabbit escaped. Press R and use the hints again."
                        game_over = True
                        show_answer = True
    # UPDATE: ทำให้หน้ากระต่ายลอยขึ้นลง
    bob_y += bob_speed
    if bob_y > 12 or bob_y < -12:
        bob_speed *= -1
    # DRAW: อ่าน DATA ล่าสุดแล้วสร้างภาพใหม่
    screen.fill((31, 35, 73))
    if not game_over:
        # GUESSING SCREEN: ซ่อนรูปจริง ไม่เช่นนั้นภาพจะเฉลยทันที
        mystery_card = pygame.Rect(340, 105 + bob_y, 170, 190)
        pygame.draw.rect(screen, (70, 82, 125), mystery_card, border_radius=28)
        question_image = mystery_font.render("?", True, (255, 220, 100))
        screen.blit(question_image, question_image.get_rect(center=mystery_card.center))
        for index in range(3):
            animal = animals[index]
            button = buttons[index]
            pygame.draw.rect(screen, (245, 185, 75), button, border_radius=10)
            label = font.render(animal.upper(), True, (25, 30, 40))
            screen.blit(label, label.get_rect(center=button.center))
        screen.blit(font.render(message, True, "white"), (100, 475))
        screen.blit(font.render(story, True, (150, 220, 245)), (100, 515))
    else:
        # RESULT SCREEN: รอบจบแล้วจึง reveal รูปและเฉลย
        result_title = font.render("MYSTERY ANSWER: RABBIT", True, (255, 220, 100))
        screen.blit(result_title, result_title.get_rect(center=(425, 65)))
        screen.blit(rabbit_image, (340, 115 + bob_y))
        screen.blit(font.render(message, True, "white"), (250, 350))
        screen.blit(font.render(story, True, (150, 220, 245)), (115, 405))
        restart_text = font.render("Press R to play a new mystery", True, (255, 220, 100))
        screen.blit(restart_text, restart_text.get_rect(center=(425, 485)))

    score_text = "Animals rescued: " + str(rescued_count)
    screen.blit(font.render(score_text, True, (255, 220, 100)), (560, 35))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

# attempts เป็นทั้งตัวนับครั้งและ index ของ hints เหมือน Terminal Version
# หลังพบสัตว์ เกมมีผลลัพธ์ คะแนน และ Restart ไม่หยุดอยู่แค่ข้อความ "YOU FOUND IT"
