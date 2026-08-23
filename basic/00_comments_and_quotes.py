"""บทที่ 0: Comments and Quotes"""

# ==================================================
# 1. Comment — ข้อความอธิบายโค้ด
# ==================================================
# Python จะไม่ทำคำสั่งที่อยู่หลังเครื่องหมาย #

# นี่คือ Comment ทั้งบรรทัด
print("This line works.")  # Comment เขียนท้ายบรรทัดได้

# เติม # หน้าโค้ด เมื่อต้องการหยุดโค้ดบรรทัดนั้นชั่วคราว
# print("This line will not run.")


# ==================================================
# 2. Single Quote และ Double Quote
# ==================================================
# String หรือข้อความใช้ได้ทั้ง '...' และ "..."

print('Hello with single quotes!')
print("Hello with double quotes!")

# เครื่องหมายที่เปิดและปิดต้องเป็นชนิดเดียวกัน
# print("This is wrong!')  # ผิด เพราะเปิดและปิดไม่ตรงกัน


# ==================================================
# 3. เลือก Quote ให้เหมาะกับข้อความ
# ==================================================
# ข้อความมี ' ด้านใน จึงใช้ Double Quote ครอบด้านนอก
print("I'm learning Python.")

# ข้อความมี " ด้านใน จึงใช้ Single Quote ครอบด้านนอก
print('The robot says, "Hello!"')

# \\n ทำให้ข้อความขึ้นบรรทัดใหม่
print("Line 1\nLine 2")


# ==================================================
# 4. Triple Quotes — ข้อความหลายบรรทัด
# ==================================================
# ใช้ """...""" เมื่อต้องการเขียน String หลายบรรทัด
story = """A cat found a key.
The key opened a door.
The adventure began!"""
print(story)


print("\n--- Typing Practice: พิมพ์ตาม ---")
# พิมพ์โค้ด 4 บรรทัดนี้ด้วยตัวเอง อย่า Copy/Paste
# จากนั้นกด Run และตรวจผลลัพธ์
#
# print("My name is Mali.")
# print('I like Python!')
# print("I'm ready to code!")
# print("Hello\nPython")
# message = """Hello!
# Welcome to my game."""
# print(message)


print("\n--- Your turn 1 ---")
# TODO 1:
# 1. เขียน Comment บอกว่าโปรแกรมนี้แสดงชื่อและงานอดิเรก
# 2. ใช้ print() แสดงชื่อของตัวเอง
# 3. ใช้ print() แสดงงานอดิเรกของตัวเอง


print("\n--- Your turn 2 ---")
# TODO 2: แสดงข้อความด้านล่าง โดยเลือก Quote ให้เหมาะสม
# I'm a Python student.
# The robot says, "Let's play!"


print("\n--- Your turn 3 ---")
# TODO 3: ใช้ Triple Quotes สร้างเรื่องสั้น 3 บรรทัด
# เก็บไว้ในตัวแปร story แล้ว print(story)


# === คำถามเช็กความเข้าใจ ===
# 1. เครื่องหมายใดใช้เริ่ม Comment?
# 2. Single Quote และ Double Quote ใช้สร้างข้อมูลชนิดใด?
# 3. \\n ทำให้ข้อความเปลี่ยนอย่างไร?
# 4. Triple Quotes เหมาะกับข้อความแบบใด?
