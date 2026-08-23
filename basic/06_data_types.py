"""บทที่ 6: Data Types — ชนิดของข้อมูล"""

# ข้อมูลพื้นฐานที่ควรรู้มี 4 ชนิด
name = "Mali"       # str: ข้อความ
age = 10            # int: จำนวนเต็ม
height = 135.5      # float: จำนวนทศนิยม
is_student = True   # bool: True หรือ False

print("--- Example 1: Check with type() ---")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


print("\n--- Example 2: 10 and \"10\" are different ---")
number = 10
text_number = "10"
print(type(number))
print(type(text_number))


print("\n--- Typing Practice: พิมพ์และทาย ---")
# พิมพ์ตาม ทายชนิดข้อมูลก่อน แล้วใช้ type() ตรวจ
# game_name = "Dragon Cave"
# lives = 3
# speed = 2.5
# game_over = False
# print(type(game_name))
# print(type(lives))
# print(type(speed))
# print(type(game_over))


print("\n--- Your turn 1 ---")
# TODO 1: สร้างตัวแปร str, int, float และ bool อย่างละหนึ่งตัว
# ใช้ type() ตรวจทุกตัวแปร


print("\n--- Your turn 2 ---")
score = "50"
# TODO 2: ทายว่า score เป็นชนิดใด แล้วใช้ type(score) ตรวจ


# === คำถามเช็กความเข้าใจ ===
# 1. "25" กับ 25 เป็นข้อมูลชนิดเดียวกันหรือไม่?
# 2. จำนวนทศนิยมใช้ชนิดใด?
# 3. bool มีค่าอะไรได้บ้าง?

