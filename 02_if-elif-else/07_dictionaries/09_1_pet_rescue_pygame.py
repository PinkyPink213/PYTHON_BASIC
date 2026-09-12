"""Upgrade 07_1_pet_rescue_game.py เป็น Pet Rescue Pygame.

pets เป็นแหล่ง DATA จุดเดียว; Card อ่าน value และ click update status
input ชื่อ pet/item กลายเป็น Card click; print ผลช่วยเหลือกลายเป็น message
"""
from pathlib import Path
import pygame
pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 28)
atlas_path = Path(__file__).parent / "assets" / "game_asset_choices.png"
atlas = pygame.image.load(atlas_path).convert()
cat_image = pygame.transform.smoothscale(atlas.subsurface(pygame.Rect(0, 768, 341, 384)), (100, 110))
dog_image = pygame.transform.smoothscale(atlas.subsurface(pygame.Rect(341, 768, 341, 384)), (100, 110))
rabbit_image = pygame.transform.smoothscale(atlas.subsurface(pygame.Rect(682, 768, 342, 384)), (100, 110))
pet_images = (cat_image, dog_image, rabbit_image)
# DATA: nested Dictionary เก็บรายละเอียดและกติกา pet
pets = {"milo": {"animal": "cat", "age": 3, "needs": "milk"},
        "lucky": {"animal": "dog", "age": 5, "needs": "ball"},
        "snow": {"animal": "rabbit", "age": 2, "needs": "carrot"}}
pet_buttons = [pygame.Rect(60, 90, 240, 250), pygame.Rect(340, 90, 240, 250),
               pygame.Rect(620, 90, 240, 250)]
items = ("milk", "ball", "carrot")
item_buttons = [pygame.Rect(165, 410, 170, 55), pygame.Rect(365, 410, 170, 55),
                pygame.Rect(565, 410, 170, 55)]
selected_pet, message = "", "Choose a pet"
running = True
while running:
    # EVENT + UPDATE: เลือก key แล้วอ่าน/เปลี่ยน value
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pet_index = 0
            for name in pets:
                button = pet_buttons[pet_index]
                if button.collidepoint(event.pos):
                    selected_pet, message = name, "What does " + name.title() + " need?"
                pet_index += 1
            if selected_pet:
                for item_index in range(3):
                    item = items[item_index]
                    button = item_buttons[item_index]
                    if button.collidepoint(event.pos):
                        pet = pets[selected_pet]
                        if item == pet["needs"]:
                            pet["status"] = "happy"
                            message = selected_pet.title() + " IS HAPPY!"
                        else:
                            pet["status"] = "waiting"
                            message = "Needs " + pet["needs"] + ", not " + item
    # DRAW: สร้าง Card จาก Dictionary ปัจจุบัน
    screen.fill((27, 41, 65))
    pet_index = 0
    for name in pets:
        button = pet_buttons[pet_index]
        color = (83, 105, 145)
        if name == selected_pet:
            color = (75, 190, 145)
        pygame.draw.rect(screen, color, button, border_radius=16)
        screen.blit(pet_images[pet_index], (button.x + 70, button.y + 15))
        data = pets[name]
        lines = (name.title(), data["animal"], "Age " + str(data["age"]))
        for i in range(3):
            line = lines[i]
            screen.blit(font.render(line, True, "white"), (button.x + 60, button.y + 135 + i * 32))
        pet_index += 1
    for item_index in range(3):
        item = items[item_index]
        button = item_buttons[item_index]
        pygame.draw.rect(screen, (245, 180, 70), button, border_radius=10)
        label = font.render(item.upper(), True, (25, 30, 40))
        screen.blit(label, label.get_rect(center=button.center))
    screen.blit(font.render(message, True, "white"), (100, 525))
    pygame.display.flip()
pygame.quit()

# จุดสอน: UI อ่าน key เดิม และเพิ่ม status กลับเข้า chosen pet dictionary
