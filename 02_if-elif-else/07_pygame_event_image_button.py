"""บทที่ 7: Pygame Basic — โหลดรูป รับ Event และสร้างปุ่มคลิก

ต่อจาก Chapter 01: เรารู้จัก window, color, shape และ text แล้ว
เรื่องใหม่ของบทนี้คือ image, Rect, MOUSEBUTTONDOWN และ collidepoint()

เรียนเหมือนไฟล์ 01_if_elif_else.py: พิมพ์ Example ตามและอธิบายผลก่อน
จากนั้นทำ Your turn/TODO ใต้ตัวอย่าง แล้วเปลี่ยนค่าเล็กน้อยก่อน Run ตรวจ
"""

from pathlib import Path
import pygame

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Pygame Image and Button")
font = pygame.font.Font(None, 38)

# RUN CHECKPOINT 1: ต้องเห็นหน้าต่าง 900×600 และไม่มี ModuleNotFoundError

# --- Example 1: Load and resize an image ---
# Path(__file__).parent คือโฟลเดอร์ที่ไฟล์ Python นี้อยู่
# จึงหา asset เจอแม้ Run โปรแกรมจาก working directory อื่น
asset_path = Path(__file__).parent / "assets" / "animals" / "animal_choices.png"

# image.load() อ่านรูป ส่วน convert_alpha() เตรียม Surface และเก็บพื้นหลังโปร่งใส
# ถ้ารูปเป็นฉากทึบใช้ convert(); ถ้าเป็น icon โปร่งใสใช้ convert_alpha()
animal_image = pygame.image.load(asset_path).convert_alpha()
animal_image = pygame.transform.smoothscale(animal_image, (720, 405))

# --- Your turn 1: Image + smoothscale ---
# TODO 1: ดู Example 1 แล้วสร้าง picture_small ขนาด (600, 338)
#
# รูปแบบที่ต้องพิมพ์:
# picture_small = pygame.transform.smoothscale(____, (____, ____))
#
# จากนั้นเปลี่ยน screen.blit(animal_image, ...) ด้านล่างเป็น picture_small
# RUN CHECKPOINT 2: รูปต้องเล็กลงแต่สัดส่วนไม่บิด และไม่มี NameError

# Rect เก็บตำแหน่งและขนาดของปุ่ม และใช้ตรวจการคลิกได้
button = pygame.Rect(325, 510, 250, 60)
message = "Click PLAY once"

# --- Example 2: Rect stores a button area ---
# Rect รับ (x, y, width, height)
# --- Your turn 2: Create another Rect ---
# TODO 2: พิมพ์ reset_button ที่ตำแหน่ง (40, 510) ขนาด 220×60
# reset_button = pygame.Rect(____, ____, ____, ____)
# TODO 3: พิมพ์ pygame.draw.rect() ในส่วน DRAW เพื่อให้เห็นปุ่มนี้
# RUN CHECKPOINT 3: PLAY กับ RESET ต้องไม่ซ้อนกัน ชี้ x/y/width/height ได้


# --- Example 3 / Your turn 3: ทดลอง collidepoint ก่อนรับ Mouse จริง ---
# จุดกลาง PLAY คือ (450, 540) ให้ทายก่อนว่า collidepoint() คืน True หรือ False
# TODO 4: พิมพ์สองบรรทัดนี้ด้วยตัวเอง แล้ว Run ดูผลใน Terminal
# test_position = (450, 540)
# print(button.collidepoint(test_position))
# RUN CHECKPOINT 4: เปลี่ยนเป็น (50, 50) แล้วผลต้องเปลี่ยนจาก True เป็น False

# DRAW ครั้งแรก: ผู้เล่นเห็นภาพและปุ่มก่อน
screen.fill((25, 30, 60))
screen.blit(animal_image, (90, 45))
pygame.draw.rect(screen, (255, 195, 70), button, border_radius=12)
label = font.render(message, True, (25, 30, 45))
screen.blit(label, label.get_rect(center=button.center))
pygame.display.flip()

# --- Example 4: Mouse Event replaces input() ---
# EVENT หนึ่งครั้ง: Chapter 02 ยังไม่เรียน Loop จึงใช้ event.wait()
# ทายก่อน Run: คลิกในปุ่มกับนอกปุ่มจะได้ข้อความต่างกันอย่างไร?
# พิมพ์ Event Pattern ชุดนี้ตามทีละบรรทัด
# ระหว่างพิมพ์ ให้พูดว่า EVENT ใดแทน input() และ DATA ตัวใดถูกเปลี่ยน
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
event = pygame.event.wait()
if event.type == pygame.QUIT:
    # pygame.quit() ปิดระบบ Pygame และ SystemExit จบไฟล์ทันที
    # เป็น Window Safety Pattern สำหรับไฟล์แบบไม่มี Game Loop
    pygame.quit()
    raise SystemExit
elif event.type == pygame.MOUSEBUTTONDOWN:
    if button.collidepoint(event.pos):
        message = "You clicked PLAY!"
    else:
        message = "That was outside the button"

# RUN CHECKPOINT 5: Run สองครั้ง—ครั้งแรกคลิกใน PLAY ครั้งที่สองคลิกนอกปุ่ม
# ต้องเห็นข้อความต่างกัน และหน้าต่างต้องไม่ดับทันทีหลัง click แรก

# --- Example 5: Draw again after DATA changes ---
# DRAW อีกครั้งหลัง DATA (message) เปลี่ยน
# เปลี่ยนเฉพาะสิ่งที่อ่านจาก message ห้ามเขียนผล click ตายตัวใน UI
screen.fill((25, 30, 60))
screen.blit(animal_image, (90, 45))
pygame.draw.rect(screen, (255, 195, 70), button, border_radius=12)
label = font.render(message, True, (25, 30, 45))
screen.blit(label, label.get_rect(center=button.center))
pygame.display.flip()

# หนึ่ง click มี 2 Event: DOWN ตอนกด และ UP ตอนปล่อย
# ต้องรอ UP ของ click แรกให้จบก่อน จึงเปิดรับ DOWN ใหม่สำหรับปิดหน้าผลลัพธ์
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
pygame.event.wait()
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.clear()
pygame.event.wait()

pygame.quit()

# RUN CHECKPOINT 6: ผลลัพธ์ต้องค้างให้อ่านได้ แล้ว click อีกครั้งจึงปิด

# === Your turn 4: สร้างปุ่มของเราเอง ===
# TODO 5: ตั้งชื่อปุ่มใหม่และเลือกสีที่สื่อหน้าที่ของปุ่ม
# TODO 6: สร้าง Rect ใหม่โดยไม่ทับ PLAY
# TODO 7: ใช้ collidepoint() และ if/elif/else ให้ปุ่มใหม่เปลี่ยน message
# TODO 8: วาด Reaction หลัง click เช่น สีใหม่หรือข้อความ "BUTTON PRESSED"
# TEST: [ ] click PLAY [ ] click ปุ่มใหม่ [ ] click นอกปุ่ม [ ] ปิดหน้าต่าง
# TRANSFER: เขียนก่อนทำว่า DATA ___ / EVENT ___ / LOGIC ___ / DRAW ___

# คำถามเช็กความเข้าใจ:
# 1. Path ช่วยป้องกันปัญหาใด?
# 2. Rect ใช้ทั้งวาดปุ่มและตรวจ click ได้อย่างไร?
# 3. event.wait() ทำให้บทนี้ยังไม่ต้องใช้ Loop ได้อย่างไร?
# 4. MOUSEBUTTONDOWN และ MOUSEBUTTONUP เกิดตอนไหน?
# 5. เพราะอะไรไฟล์แบบไม่มี Loop ต้องจบโปรแกรมทันทีเมื่อได้รับ QUIT?
