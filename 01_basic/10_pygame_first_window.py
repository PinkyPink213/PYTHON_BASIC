"""บทที่ 10: Pygame ครั้งแรก — ติดตั้ง ตรวจสอบ และเปิดหน้าต่าง

เป้าหมายของไฟล์นี้
1. ติดตั้ง Pygame บน macOS, Linux หรือ Windows
2. เข้าใจ pygame.init(), set_mode(), fill(), flip() และ quit()
3. พิมพ์ตามทีละ STEP และ Run ได้ก่อนนำไปสร้าง Profile ในบท 11.1

ติดตั้งใน Terminal / PowerShell / Command Prompt
macOS / Linux: python3 -m pip install pygame
Windows:         py -m pip install pygame

ตรวจว่าติดตั้งสำเร็จ
macOS / Linux: python3 -c "import pygame; print(pygame.version.ver)"
Windows:         py -c "import pygame; print(pygame.version.ver)"

ถ้า Windows ไม่มีคำสั่ง py ให้ใช้ python แทน
ถ้า Python รุ่นใหม่ติดตั้ง pygame ไม่ผ่าน ใช้ pygame-ce แทนได้:
python3 -m pip install pygame-ce   หรือ   py -m pip install pygame-ce
จากนั้นยังเขียน import pygame เหมือนเดิม

บทนี้ยังไม่เรียน if, for หรือ while จึงใช้ event.wait() รอให้กด Keyboard
เรียนเหมือนไฟล์ Python ก่อนหน้า: พิมพ์ Example ตามก่อน แล้วทำ Your turn/TODO
"""

import pygame


# ==================================================
# Example 1 — เตรียมระบบ Pygame
# ==================================================

# init ย่อมาจาก initialize หมายถึงเตรียมส่วนต่าง ๆ ของ Pygame ให้พร้อม
pygame.init()

# RUN CHECKPOINT 1: ถ้าไม่มี ModuleNotFoundError แปลว่า import สำเร็จ


# ==================================================
# Example 2 — สร้างพื้นที่วาดภาพ
# ==================================================

# set_mode() รับขนาด (width, height)
# ตอนนี้จำรูปแบบเลขในวงเล็บก่อน เราจะเรียน Tuple อย่างละเอียดใน Chapter 05
screen = pygame.display.set_mode((700, 450))
pygame.display.set_caption("My First Pygame Window")

# Your turn 1
# TODO 1: เปลี่ยนชื่อบนแถบหน้าต่างให้เป็นชื่อเกมของเรา
# TYPE: พิมพ์ pygame.display.set_caption(...) ใต้คอมเมนต์นี้


# RUN CHECKPOINT 2: Run แล้วต้องเห็นหน้าต่างขนาด 700×450 พร้อมชื่อด้านบน


# ==================================================
# Example 3 — เติมสีพื้นหลังด้วย RGB
# ==================================================

# RGB คือปริมาณสีแดง เขียว น้ำเงิน แต่ละค่าอยู่ระหว่าง 0–255
background_color = (35, 45, 85)
screen.fill(background_color)

# Your turn 2
# TODO 2: สร้างสีของเรา แล้วเปลี่ยนตัวแปรใน screen.fill()
# my_color = (..., ..., ...)


# ตอนนี้คำสั่งวาดอยู่ในความจำ แต่หน้าจอยังไม่ได้อัปเดต
# flip() นำภาพที่วาดเสร็จแล้วไปแสดงบนหน้าต่าง
pygame.display.flip()

# RUN CHECKPOINT 3: เปลี่ยนเลข RGB ทีละค่า แล้วบอกว่าสีใดเพิ่มขึ้น


# ==================================================
# Example 4 — รอผู้ใช้ก่อนปิดหน้าต่าง
# ==================================================

# ปิด Event ทั้งหมดก่อน แล้วอนุญาตเฉพาะ Keyboard และปุ่มปิดหน้าต่าง
# วิธีนี้ทำให้หน้าต่างไม่ดับทันทีและยังไม่ต้องใช้ Loop
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.clear()

# wait() หยุดรอจนมี Event ที่อนุญาตหนึ่งครั้ง
pygame.event.wait()

# quit() ปิดระบบ Pygame หลังผู้ใช้กด Keyboard หรือปุ่มปิดหน้าต่าง
pygame.quit()

# RUN CHECKPOINT 4: click ในหน้าต่างต้องไม่ปิด; กด Keyboard แล้วจึงปิด


# ==================================================
# คำถามเช็กความเข้าใจ ก่อนเปิดบท 11.1
# ==================================================

# 1. pygame.init() เตรียมอะไร?
# 2. เลข 700 และ 450 ควบคุมอะไร?
# 3. screen.fill() กับ pygame.display.flip() ต่างกันอย่างไร?
# 4. เพราะอะไรเราใช้ event.wait() แทน while ใน Chapter 01?
# 5. ชี้ DATA (สี/ขนาด) และ UI (หน้าต่าง/สีที่เห็น) ในไฟล์นี้

# TRANSFER: ออกแบบหน้าต่างเกมของเราโดยเปลี่ยนชื่อ ขนาด และ RGB
# เมื่อ Run สำเร็จแล้ว ไป 11_1 เพื่อใช้หน้าต่างนี้แสดง Profile Generator
