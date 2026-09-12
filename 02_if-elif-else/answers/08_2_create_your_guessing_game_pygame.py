"""ตัวอย่างคำตอบ Creative Theme: Food Guessing Game — ไม่มี Loop ก่อน Chapter 04."""
from pathlib import Path
import pygame

choice_1 = "pizza"
choice_2 = "cupcake"
choice_3 = "sushi"
secret_choice = "sushi"

pygame.init()
screen = pygame.display.set_mode((900, 650))
font = pygame.font.Font(None, 34)
path = Path(__file__).parent.parent / "assets" / "food"
image_1 = pygame.transform.smoothscale(pygame.image.load(path / "pizza.png").convert_alpha(), (150, 150))
image_2 = pygame.transform.smoothscale(pygame.image.load(path / "cupcake.png").convert_alpha(), (150, 150))
image_3 = pygame.transform.smoothscale(pygame.image.load(path / "sushi.png").convert_alpha(), (150, 150))
button_1 = pygame.Rect(125, 430, 190, 60)
button_2 = pygame.Rect(355, 430, 190, 60)
button_3 = pygame.Rect(585, 430, 190, 60)

screen.fill((55, 35, 65))
screen.blit(image_1, (145, 180))
screen.blit(image_2, (375, 180))
screen.blit(image_3, (605, 180))
pygame.draw.rect(screen, (255, 190, 90), button_1, border_radius=10)
pygame.draw.rect(screen, (255, 190, 90), button_2, border_radius=10)
pygame.draw.rect(screen, (255, 190, 90), button_3, border_radius=10)
screen.blit(font.render(choice_1.upper(), True, (30, 30, 40)), (175, 450))
screen.blit(font.render(choice_2.upper(), True, (30, 30, 40)), (390, 450))
screen.blit(font.render(choice_3.upper(), True, (30, 30, 40)), (645, 450))
screen.blit(font.render("Hint: rice and seaweed", True, "white"), (280, 550))
pygame.display.flip()

pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
answer = ""
event = pygame.event.wait()
if event.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(event.pos):
        answer = choice_1
    elif button_2.collidepoint(event.pos):
        answer = choice_2
    elif button_3.collidepoint(event.pos):
        answer = choice_3

if answer == secret_choice:
    message = "CORRECT!"
else:
    message = "TRY AGAIN"
screen.blit(font.render(message, True, (255, 230, 100)), (350, 600))
pygame.display.flip()
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
pygame.event.wait()
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
pygame.event.wait()
pygame.quit()
