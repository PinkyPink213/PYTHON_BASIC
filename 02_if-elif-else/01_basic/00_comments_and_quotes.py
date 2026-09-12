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


# ==================================================
# 4. Escape Quotes ด้วย Backslash
# ==================================================
# ใส่ \ หน้า Quote เมื่อต้องการให้ Quote เป็นส่วนหนึ่งของข้อความ

# ใช้ \' เมื่อต้องการใส่ Single Quote ใน String ที่ครอบด้วย '...'
print('I\'m learning Python.')

# ใช้ \" เมื่อต้องการใส่ Double Quote ใน String ที่ครอบด้วย "..."
print("The robot says, \"Go!\"")


# ==================================================
# 5. New Line ด้วย \n
# ==================================================
# \n ทำให้ข้อความขึ้นบรรทัดใหม่
print("Line 1\nLine 2")


# ==================================================
# 6. Triple Quotes — ข้อความหลายบรรทัด
# ==================================================
# ใช้ """...""" เมื่อต้องการเขียน String หลายบรรทัด
story = """A cat found a key.
The key opened a door.
The adventure began!"""
print(story)


print("\n--- Practice 1: Comments ---")
# เขียน Comment ทั้งบรรทัดเพื่ออธิบายว่าโปรแกรมกำลังทักทาย
# จากนั้นเขียนคำสั่งให้แสดงคำว่า Hello!
# สุดท้ายเขียน Comment ต่อท้ายคำสั่งนั้น


print("\n--- Practice 2: Choose Quotes ---")
# เขียนโค้ดให้แสดงข้อความสองบรรทัดนี้
# เลือก Quote ด้านนอกให้ข้อความด้านในเขียนได้ง่าย
#
# I'm ready to code!
# The robot says, "Run!"


print("\n--- Practice 3: Escape Single Quote ---")
# ต้องใช้ Single Quote ครอบ String และใช้ \' ให้ผลลัพธ์เป็น
#
# I'm a coder!


print("\n--- Practice 4: Escape Double Quote ---")
# ต้องใช้ Double Quote ครอบ String และใช้ \" ให้ผลลัพธ์เป็น
#
# The wizard says, "Welcome!"


print("\n--- Practice 5: New Line ---")
# ใช้คำสั่ง print() เพียงหนึ่งครั้ง และใช้ \n
# เพื่อให้ผลลัพธ์ออกมาเป็นสองบรรทัดดังนี้
#
# Hello
# Python


print("\n--- Practice 6: Triple Quotes ---")
# สร้างตัวแปร message ด้วย Triple Quotes ให้มีข้อความ 2 บรรทัด
# แล้วแสดง message บนหน้าจอ
# เด็กเลือกข้อความทั้งสองบรรทัดได้เอง


print("\n--- Your turn 1 ---")
# TODO 1:
# 1. เขียน Comment บอกว่าโปรแกรมนี้แสดงชื่อและงานอดิเรก
# 2. ใช้ print() แสดงชื่อของตัวเอง
# 3. ใช้ print() แสดงงานอดิเรกของตัวเอง


print("\n--- Your turn 2 ---")
# TODO 2: แสดงข้อความด้านล่าง โดยเลือก Quote ให้เหมาะสม
# I'm a Python student.
# The robot says, "Run!"


print("\n--- Your turn 3 ---")
# TODO 3: ใช้ Single Quote ครอบ String และใช้ \' แสดงข้อความนี้
# The cat's name is Luna.


print("\n--- Your turn 4 ---")
# TODO 4: ใช้ Triple Quotes สร้างเรื่องสั้น 3 บรรทัด
# เก็บไว้ในตัวแปร story แล้ว print(story)


# === คำถามเช็กความเข้าใจ ===
# 1. เครื่องหมายใดใช้เริ่ม Comment?
# 2. Single Quote และ Double Quote ใช้สร้างข้อมูลชนิดใด?
# 3. \' และ \" มีประโยชน์เมื่อใด?
# 4. \n ทำให้ข้อความเปลี่ยนอย่างไร?
# 5. Triple Quotes เหมาะกับข้อความแบบใด?
