"""Upgrade 06_2_create_your_list_game.py ของเราเป็น Pygame

เปิด 3 หน้าต่างข้างกัน: 06_2_create_your_list_game.py = เกม Terminal ของเรา,
07_pygame_list_inventory.py / 08_1_treasure_backpack_pygame.py = Reference,
ไฟล์นี้ = พื้นที่ Convert
- COPY: โลก, items, เหตุการณ์, การเพิ่ม/เปลี่ยนของ และตอนจบจาก 06_2
- LOOK: image/button/event pattern ที่พิมพ์ตามใน 07 และเห็นครบใน 08_1
- TYPE: พิมพ์ Pattern ใหม่ด้วยมือ ห้ามคัดลอกธีมของตัวอย่าง
- REPLACE: input → click และ print → story screen

STEP ด้านล่างตรงกับ Flow ของ 08_1 แต่ข้อมูลและเรื่องราวต้องเป็นของเด็กเอง
บทนี้ยังไม่ใช้ Loop จึงเขียน click แต่ละช่วงแยกกันอย่างตั้งใจ
"""
from pathlib import Path
import pygame


# ==================================================
# STEP 1 — COPY GAME DESIGN จาก 06_2
# ==================================================
# LOOK: วง List, เหตุการณ์ และเงื่อนไขตอนจบใน 06_2
# TODO: เติมคำตอบจากเกม Terminal ของเรา
game_title = "MY LIST ADVENTURE"
place = "My World"
mission = "Describe the mission"
problem = "Describe the danger"

# ต้องมี 5 ตัวเลือกเริ่มต้นเหมือนเกม Terminal ของเรา
available_items = ["item 1", "item 2", "item 3", "item 4", "item 5"]
backpack = []

# ของใหม่สองชิ้นต้องมาจาก TODO 7–8 ใน 06_2 ไม่บังคับเป็น radio/coconut
new_item_1 = "new item 1"
new_item_2 = "new item 2"
# RUN CHECKPOINT: print ตัวแปรชั่วคราวได้ แล้วนับว่ามีตัวเลือก 5 ชิ้นจริง


# ==================================================
# STEP 2 — SETUP + STORY SCREEN
# ==================================================
# LOOK: เปิด Story Screen ใน 08_1 แล้วชี้ DATA ที่ถูกส่งไป DRAW
# TYPE: พิมพ์ setup และข้อความจากเรื่องของเราเอง
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption(game_title)
font = pygame.font.Font(None, 30)
asset_folder = Path(__file__).parent / "assets" / "items"

# TODO: render ชื่อสถานที่ ภารกิจ และปัญหาจาก STEP 1
# TODO: สร้าง START button ให้ผู้เล่นรู้เหตุผลก่อนเลือกของ
screen.fill((25, 40, 65))
screen.blit(font.render(game_title, True, (255, 220, 100)), (300, 100))
screen.blit(font.render("Build the Story Screen from your 06_2 game", True, "white"), (180, 260))
pygame.display.flip()
# RUN CHECKPOINT: ต้องอ่านสถานที่ ภารกิจ และปัญหาได้โดยข้อความไม่ซ้อนกัน


# ==================================================
# STEP 3 — LOAD 5 ITEM IMAGES
# ==================================================
# LOOK: ทบทวน load → convert_alpha → smoothscale ใน 07 ก่อนใช้
# ใช้ Pattern ที่เรียนใน 07 แยกเป็น load → convert_alpha → smoothscale
# TODO: จับคู่ image_1 ถึง image_5 กับ available_items index 0 ถึง 4
# หากธีมไม่ตรงกับรูปที่มี ให้วาดรูปเองหรือใช้ Shapes ก่อน
# RUN CHECKPOINT: แสดงรูปทีละรูปก่อนทำปุ่ม และ path ต้องไม่ error




# ==================================================
# STEP 4 — CHOOSE 3 DIFFERENT ITEMS
# ==================================================
# LOOK: เทียบ Event และ Button Reaction กับ 08_1 ทีละบรรทัด
# TYPE: ทำปุ่มแรกให้สำเร็จก่อน แล้วจึงทำปุ่ม 2–5
# TODO 4A: สร้าง Rect 5 ปุ่มและวาดชื่อจาก available_items[0] ... [4]
# TODO 4B: กรอง Event ให้รับ MOUSEBUTTONDOWN/MOUSEBUTTONUP
# TODO 4C: รับ click ครั้งที่ 1 → append item → Button Reaction → รอปล่อยเมาส์
# TODO 4D: ทำซ้ำครั้งที่ 2 และ 3 พร้อมใช้ not in ป้องกันของซ้ำ
# TODO 4E: แสดง Selected 1/3, 2/3 และ 3/3
# RUN CHECKPOINT: เลือกซ้ำไม่เพิ่ม และเกมยังไม่ปิดหลังคลิกครั้งแรก




# ==================================================
# STEP 5 — FIRST SITUATION จาก TODO 6 ใน 06_2
# ==================================================
# LOOK: คัดลอก "กติกา" จาก 06_2 แต่เปลี่ยนเฉพาะ print เป็น DRAW
# เก็บผลของสถานการณ์ตอนนี้ ก่อนที่ผู้เล่นอาจเปลี่ยนของภายหลัง
# ตัวอย่าง Pattern: passed_first_problem = "required item" in backpack
# TODO: สร้าง Story Screen และใช้ if/in เปลี่ยนผลลัพธ์
# RUN CHECKPOINT: ทดลองทั้งกรณีมีและไม่มีของจำเป็น




# ==================================================
# STEP 6 — FIND new_item_1 จาก TODO 7 ใน 06_2
# ==================================================
# TODO: แสดงภาพ/ข้อความของใหม่ และปุ่ม KEEP BAG
# TODO: ให้ click ของที่อยู่ใน backpack เพื่อ remove ของเดิมและ append ของใหม่
# ต้องอนุญาตให้ผู้เล่นเก็บกระเป๋าเดิมเหมือนคำตอบ no ใน Terminal
# RUN CHECKPOINT: ทดสอบ KEEP และ REPLACE; จำนวนของต้องยังเท่าเดิม




# ==================================================
# STEP 7 — FIND new_item_2 จาก TODO 8 ใน 06_2
# ==================================================
# TODO: แสดงสถานการณ์ที่สอง
# หากเลือกเปลี่ยน ให้ใช้ index() และ backpack[item_index] = new_item_2
# นี่คือ logic ชุดเดียวกับ Terminal Version ไม่ใช่กติกาใหม่
# RUN CHECKPOINT: ของที่เลือกเปลี่ยนต้องหาย และของใหม่อยู่ตำแหน่งเดิม




# ==================================================
# STEP 8 — ENDING SCREEN จาก TODO 9 ใน 06_2
# ==================================================
# TODO: คัดลอก if/elif/else + and/or ตอนจบจากเกมของเรา
# เปลี่ยน print แต่ละตอนจบเป็น message แล้ว render/blit
# ล้าง screen ก่อนวาด Ending เพื่อไม่ให้ข้อความ Scene ก่อนหน้าซ้อนกัน
# RUN CHECKPOINT: เล่นทุกเส้นทางจนถึง Ending และหน้าต่างไม่ดับก่อนจบ




# โครงชั่วคราวนี้ทำให้ไฟล์เปิดและปิดได้ระหว่างสร้าง STEP แรก ๆ
pygame.event.clear()
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.wait()
pygame.quit()


# ==================================================
# STEP 9 — TEST Terminal → Pygame
# ==================================================
# [ ] Story/ภารกิจเหมือน 06_2
# [ ] มีตัวเลือกเริ่มต้น 5 ชิ้นและเลือกต่างกันได้ 3 ชิ้น
# [ ] Button มี Reaction และแสดงความคืบหน้า 1/3–3/3
# [ ] สถานการณ์แรกตรวจของชิ้นเดิมถูกต้อง
# [ ] new_item_1 ใช้ remove() + append()
# [ ] new_item_2 ใช้ index() + เปลี่ยนค่าตาม Index
# [ ] ผู้เล่นเลือก KEEP ได้ทั้งสองสถานการณ์
# [ ] ตอนจบทุกแบบใช้เงื่อนไขเดียวกับ Terminal Version
# [ ] ไม่มี for/while ก่อน Chapter 04


# ==================================================
# STEP 10 — TRANSFER / CREATIVE STUDIO
# ==================================================
# [ ] Theme, place, mission และ story เป็นของเรา
# [ ] รูป/สี/ข้อความเป็นโลกเดียวกัน
# [ ] เพิ่ม secret ending จาก item ที่ดูเหมือนไม่สำคัญ
# [ ] ออกแบบกติกาของเรา: เป้าหมาย ___ อุปสรรค ___ ชนะเมื่อ ___ แพ้เมื่อ ___
# [ ] เพิ่มการตัดสินใจ 1 จุดที่มีผลต่อตอนจบจริง ไม่ใช่แค่เปลี่ยนข้อความ
# [ ] เขียน Migration Map: DATA ___ / LIST LOGIC ___ / EVENT ___ / DRAW ___
# [ ] อธิบายได้ว่าอะไรคือ DATA, EVENT, LOGIC และ UI
