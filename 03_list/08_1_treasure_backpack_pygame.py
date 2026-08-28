"""บทที่ 8.1: Upgrade 06_1 Treasure Backpack เป็น Pygame

DATA และเงื่อนไขตอนจบมาจาก Terminal Version; click แทน input และ UI แทน print
บทนี้ยังไม่ใช้ Loop จึงรับ click 3 ครั้งแบบเขียนซ้ำ แล้ว Chapter 04 จะย่อส่วนนี้
"""
from pathlib import Path
import pygame

# COPY DATA จาก Terminal Version: ตัวเลือกเริ่มต้นต้องเหมือน 06_1
items = ["rope", "water", "fruit", "flashlight", "blanket"]
backpack = []

pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 29)
asset_folder = Path(__file__).parent / "assets" / "items"

# โหลดภาพทีละไฟล์เพื่อให้เห็นว่า index เดียวกันเชื่อมชื่อ รูป และปุ่ม
image_1 = pygame.transform.smoothscale(pygame.image.load(asset_folder / "rope.png").convert_alpha(), (90, 90))
image_2 = pygame.transform.smoothscale(pygame.image.load(asset_folder / "water_bottle.png").convert_alpha(), (90, 90))
image_3 = pygame.transform.smoothscale(pygame.image.load(asset_folder / "fruit.png").convert_alpha(), (90, 90))
image_4 = pygame.transform.smoothscale(pygame.image.load(asset_folder / "flashlight.png").convert_alpha(), (90, 90))
image_5 = pygame.transform.smoothscale(pygame.image.load(asset_folder / "blanket.png").convert_alpha(), (90, 90))
# radio/coconut เป็นของที่พบระหว่างผจญภัย ไม่ใช่ตัวเลือกเริ่มต้น
radio_image = pygame.transform.smoothscale(pygame.image.load(asset_folder / "radio.png").convert_alpha(), (100, 100))
coconut_image = pygame.transform.smoothscale(pygame.image.load(asset_folder / "coconut.png").convert_alpha(), (100, 100))

button_1 = pygame.Rect(35, 260, 150, 60)
button_2 = pygame.Rect(205, 260, 150, 60)
button_3 = pygame.Rect(375, 260, 150, 60)
button_4 = pygame.Rect(545, 260, 150, 60)
button_5 = pygame.Rect(715, 260, 150, 60)

# STORY SCREEN — สร้างเหตุผลว่าทำไมผู้เล่นต้องเลือกของ
screen.fill((25, 48, 63))
screen.blit(font.render("STRANDED ISLAND ADVENTURE", True, (255, 220, 100)), (280, 70))
screen.blit(font.render("A giant storm pushes your boat toward a mysterious island.", True, "white"), (135, 165))
screen.blit(font.render("The rescue team will arrive at sunset — if you can call them.", True, "white"), (135, 210))
screen.blit(font.render("Your backpack has room for only 3 different items.", True, "white"), (170, 255))
start_button = pygame.Rect(300, 360, 300, 70)
pygame.draw.rect(screen, (90, 200, 155), start_button, border_radius=14)
start_text = font.render("START ADVENTURE", True, (20, 40, 35))
screen.blit(start_text, start_text.get_rect(center=start_button.center))
screen.blit(font.render("Click START and prepare before the storm arrives!", True, (150, 215, 235)), (180, 485))
pygame.display.flip()

# กรอง Event ก่อนหน้า Story Screen เพื่อไม่ให้ Event เบื้องหลังข้ามฉากเอง
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

start_event = pygame.event.wait()
if start_event.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit

# รอปล่อยเมาส์ เพื่อไม่ให้ click START กลายเป็นการเลือก Item ชิ้นแรก
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
start_release = pygame.event.wait()
if start_release.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

# ITEM SCREEN — ตอนนี้ผู้เล่นรู้ภารกิจแล้วจึงเลือกของ
screen.fill((25, 48, 63))
screen.blit(font.render("CLICK 3 DIFFERENT ITEMS", True, "white"), (285, 35))
screen.blit(image_1, (65, 120))
screen.blit(image_2, (235, 120))
screen.blit(image_3, (405, 120))
screen.blit(image_4, (575, 120))
screen.blit(image_5, (745, 120))
pygame.draw.rect(screen, (230, 175, 70), button_1, border_radius=10)
pygame.draw.rect(screen, (230, 175, 70), button_2, border_radius=10)
pygame.draw.rect(screen, (230, 175, 70), button_3, border_radius=10)
pygame.draw.rect(screen, (230, 175, 70), button_4, border_radius=10)
pygame.draw.rect(screen, (230, 175, 70), button_5, border_radius=10)
screen.blit(font.render(items[0], True, (25, 35, 40)), (82, 280))
screen.blit(font.render(items[1], True, (25, 35, 40)), (245, 280))
screen.blit(font.render(items[2], True, (25, 35, 40)), (420, 280))
screen.blit(font.render(items[3], True, (25, 35, 40)), (585, 280))
screen.blit(font.render(items[4], True, (25, 35, 40)), (745, 280))
pygame.display.flip()

# EVENT 1 — โค้ดนี้คือ input ครั้งที่ 1 ใน Terminal Version
event_1 = pygame.event.wait()
clicked_button = ""
if event_1.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit  # จบโปรแกรมทันที ไม่ปล่อยให้คำสั่งวาดหลังปิดหน้าต่างทำงาน
elif event_1.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(event_1.pos):
        backpack.append(items[0])
        clicked_button = button_1
    elif button_2.collidepoint(event_1.pos):
        backpack.append(items[1])
        clicked_button = button_2
    elif button_3.collidepoint(event_1.pos):
        backpack.append(items[2])
        clicked_button = button_3
    elif button_4.collidepoint(event_1.pos):
        backpack.append(items[3])
        clicked_button = button_4
    elif button_5.collidepoint(event_1.pos):
        backpack.append(items[4])
        clicked_button = button_5

# BUTTON REACTION: เปลี่ยนสีทันทีตอน MOUSEBUTTONDOWN
if clicked_button != "":
    pygame.draw.rect(screen, (75, 205, 145), clicked_button, border_radius=10)
    reaction = font.render("SELECTED", True, (20, 40, 35))
    screen.blit(reaction, reaction.get_rect(center=clicked_button.center))
    pygame.display.flip()

# รอให้ผู้เล่นปล่อยเมาส์ก่อนเริ่มรับ Item ถัดไป
# ป้องกัน Trackpad ส่ง click เดิมติดกันจนถูกนับหลาย Item
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
release_1 = pygame.event.wait()
if release_1.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

# แสดงความคืบหน้า เพื่อให้รู้ว่าเกมยังรอเลือก Item ที่ 2
pygame.draw.rect(screen, (25, 48, 63), (0, 360, 900, 100))
progress_1 = font.render("Selected 1/3: " + str(backpack), True, "white")
screen.blit(progress_1, (100, 390))
pygame.display.flip()

# EVENT 2 — not in ป้องกันของซ้ำเหมือนการตรวจ input เดิม
event_2 = pygame.event.wait()
selected_item = ""
clicked_button = ""
if event_2.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
elif event_2.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(event_2.pos):
        selected_item = items[0]
        clicked_button = button_1
    elif button_2.collidepoint(event_2.pos):
        selected_item = items[1]
        clicked_button = button_2
    elif button_3.collidepoint(event_2.pos):
        selected_item = items[2]
        clicked_button = button_3
    elif button_4.collidepoint(event_2.pos):
        selected_item = items[3]
        clicked_button = button_4
    elif button_5.collidepoint(event_2.pos):
        selected_item = items[4]
        clicked_button = button_5
already_selected = selected_item in backpack
if selected_item != "" and not already_selected:
    backpack.append(selected_item)

if clicked_button != "":
    reaction_color = (75, 205, 145)
    reaction_text = "SELECTED"
    if already_selected:
        reaction_color = (235, 105, 105)
        reaction_text = "ALREADY!"
    pygame.draw.rect(screen, reaction_color, clicked_button, border_radius=10)
    reaction = font.render(reaction_text, True, (20, 40, 35))
    screen.blit(reaction, reaction.get_rect(center=clicked_button.center))
    pygame.display.flip()

pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
release_2 = pygame.event.wait()
if release_2.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

# ถ้าคลิกของซ้ำ backpack จะยังมี 1 ชิ้น และข้อความจะบอกให้เลือกชิ้นใหม่
progress_text = "Selected " + str(len(backpack)) + "/3: " + str(backpack)
pygame.draw.rect(screen, (25, 48, 63), (0, 360, 900, 100))
screen.blit(font.render(progress_text, True, "white"), (100, 390))
pygame.display.flip()

# EVENT 3 — หลังบท Loop โค้ดสามส่วนนี้จะรวมเป็น Loop เดียว
event_3 = pygame.event.wait()
selected_item = ""
clicked_button = ""
if event_3.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
elif event_3.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(event_3.pos):
        selected_item = items[0]
        clicked_button = button_1
    elif button_2.collidepoint(event_3.pos):
        selected_item = items[1]
        clicked_button = button_2
    elif button_3.collidepoint(event_3.pos):
        selected_item = items[2]
        clicked_button = button_3
    elif button_4.collidepoint(event_3.pos):
        selected_item = items[3]
        clicked_button = button_4
    elif button_5.collidepoint(event_3.pos):
        selected_item = items[4]
        clicked_button = button_5
already_selected = selected_item in backpack
if selected_item != "" and not already_selected:
    backpack.append(selected_item)

if clicked_button != "":
    reaction_color = (75, 205, 145)
    reaction_text = "SELECTED"
    if already_selected:
        reaction_color = (235, 105, 105)
        reaction_text = "ALREADY!"
    pygame.draw.rect(screen, reaction_color, clicked_button, border_radius=10)
    reaction = font.render(reaction_text, True, (20, 40, 35))
    screen.blit(reaction, reaction.get_rect(center=clicked_button.center))
    pygame.display.flip()

pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
release_3 = pygame.event.wait()
if release_3.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

# เก็บผลหน้าผาตอนนี้ เพราะภายหลังผู้เล่นอาจนำ rope ออกจากกระเป๋า
had_rope_at_cliff = "rope" in backpack

# CAMP SCENE — ตรงกับส่วน "ABANDONED CAMP" ใน Terminal Version
screen.fill((25, 48, 63))
screen.blit(font.render("ABANDONED CAMP", True, (255, 220, 100)), (330, 45))
screen.blit(radio_image, (400, 75))
screen.blit(font.render("You find a rescue radio, but your backpack is full.", True, "white"), (160, 190))
screen.blit(font.render("Click one item in your backpack to replace, or KEEP it.", True, "white"), (155, 225))

# วาดชื่อของเดิมทั้ง 5 ชิ้น เพื่อให้เลือกเฉพาะชิ้นที่อยู่ใน backpack
pygame.draw.rect(screen, (90, 115, 145), button_1, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_2, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_3, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_4, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_5, border_radius=10)
screen.blit(font.render(items[0], True, "white"), (82, 280))
screen.blit(font.render(items[1], True, "white"), (245, 280))
screen.blit(font.render(items[2], True, "white"), (420, 280))
screen.blit(font.render(items[3], True, "white"), (575, 280))
screen.blit(font.render(items[4], True, "white"), (755, 280))
keep_button = pygame.Rect(300, 390, 300, 65)
pygame.draw.rect(screen, (245, 180, 70), keep_button, border_radius=12)
keep_text = font.render("KEEP MY BACKPACK", True, (30, 35, 40))
screen.blit(keep_text, keep_text.get_rect(center=keep_button.center))
screen.blit(font.render("Backpack: " + str(backpack), True, (130, 225, 190)), (150, 500))
pygame.display.flip()

camp_event = pygame.event.wait()
if camp_event.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit

item_to_remove = ""
if camp_event.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(camp_event.pos):
        item_to_remove = items[0]
    elif button_2.collidepoint(camp_event.pos):
        item_to_remove = items[1]
    elif button_3.collidepoint(camp_event.pos):
        item_to_remove = items[2]
    elif button_4.collidepoint(camp_event.pos):
        item_to_remove = items[3]
    elif button_5.collidepoint(camp_event.pos):
        item_to_remove = items[4]

# COPY LOGIC: remove ของที่เลือกจริง แล้ว append radio
if item_to_remove in backpack:
    backpack.remove(item_to_remove)
    backpack.append("radio")

pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
camp_release = pygame.event.wait()
if camp_release.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

# COCONUT SCENE — ตรงกับส่วน "COCONUT TREE" ใน Terminal Version
screen.fill((25, 48, 63))
screen.blit(font.render("COCONUT TREE", True, (255, 220, 100)), (350, 45))
screen.blit(coconut_image, (400, 75))
screen.blit(font.render("You find a coconut with food and fresh water.", True, "white"), (185, 190))
screen.blit(font.render("Click an item in your backpack to replace, or KEEP it.", True, "white"), (155, 225))
pygame.draw.rect(screen, (90, 115, 145), button_1, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_2, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_3, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_4, border_radius=10)
pygame.draw.rect(screen, (90, 115, 145), button_5, border_radius=10)
screen.blit(font.render(items[0], True, "white"), (82, 280))
screen.blit(font.render(items[1], True, "white"), (245, 280))
screen.blit(font.render(items[2], True, "white"), (420, 280))
screen.blit(font.render(items[3], True, "white"), (575, 280))
screen.blit(font.render(items[4], True, "white"), (755, 280))
pygame.draw.rect(screen, (245, 180, 70), keep_button, border_radius=12)
screen.blit(keep_text, keep_text.get_rect(center=keep_button.center))
screen.blit(font.render("Backpack: " + str(backpack), True, (130, 225, 190)), (150, 500))
pygame.display.flip()

coconut_event = pygame.event.wait()
if coconut_event.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit

item_to_remove = ""
if coconut_event.type == pygame.MOUSEBUTTONDOWN:
    if button_1.collidepoint(coconut_event.pos):
        item_to_remove = items[0]
    elif button_2.collidepoint(coconut_event.pos):
        item_to_remove = items[1]
    elif button_3.collidepoint(coconut_event.pos):
        item_to_remove = items[2]
    elif button_4.collidepoint(coconut_event.pos):
        item_to_remove = items[3]
    elif button_5.collidepoint(coconut_event.pos):
        item_to_remove = items[4]

if item_to_remove in backpack:
    item_index = backpack.index(item_to_remove)
    backpack[item_index] = "coconut"

pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
coconut_release = pygame.event.wait()
if coconut_release.type == pygame.QUIT:
    pygame.quit()
    raise SystemExit
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()

# COPY LOGIC — เงื่อนไขตอนจบจาก 06_1 ไม่ต้องเขียนใหม่
if len(backpack) != 3:
    message = "Choose 3 different items next time"
elif "radio" in backpack and ("water" in backpack or "coconut" in backpack):
    message = "A RESCUE BOAT FINDS YOU!"
elif "radio" in backpack:
    message = "Rescued, but very thirsty!"
elif "water" in backpack or "coconut" in backpack:
    message = "Safe tonight, but cannot call for help"
else:
    message = "No radio and no water — try again"

# สถานการณ์ระหว่างเดินทางเปลี่ยนตามของที่ผู้เล่นเลือก
if had_rope_at_cliff:
    cliff_story = "CLIFF: You use the rope and climb to high ground safely."
else:
    cliff_story = "CLIFF: No rope — you must take the long and tiring path."

if "radio" in backpack:
    camp_story = "CAMP: You turn on the radio and call the rescue team."
else:
    camp_story = "CAMP: You find no way to contact the rescue team."

# ENDING SCREEN — เปลี่ยนฉากใหม่ทั้งหมด ไม่ให้ภาพ Coconut/Camp ค้างด้านหลัง
screen.fill((25, 48, 63))
ending_title = font.render("SUNSET ON THE ISLAND", True, (255, 220, 100))
screen.blit(ending_title, ending_title.get_rect(center=(450, 70)))

final_count = "Selected " + str(len(backpack)) + "/3"
final_backpack = "Backpack: " + str(backpack)
screen.blit(font.render(final_count, True, (110, 230, 175)), (70, 145))
screen.blit(font.render(final_backpack, True, "white"), (70, 195))
screen.blit(font.render(cliff_story, True, (170, 220, 245)), (70, 280))
screen.blit(font.render(camp_story, True, (170, 220, 245)), (70, 330))
screen.blit(font.render(message, True, (255, 220, 100)), (70, 430))
screen.blit(font.render("Click once to finish the adventure", True, "white"), (250, 520))
pygame.display.flip()
# รอ click สุดท้ายเพื่อให้เด็กอ่านข้อความผลลัพธ์ก่อนปิดเกม
pygame.event.wait()
pygame.quit()

# Exit ticket: ส่วนใด COPY จาก Terminal และส่วนใด REPLACE เพื่อเป็น Pygame?
