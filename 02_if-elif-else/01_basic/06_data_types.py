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


print("\n--- Practice 1: Guess the types ---")
# ทายชนิดข้อมูลของแต่ละค่าก่อนเขียนโค้ด
# จากนั้นเก็บแต่ละค่าในตัวแปรและใช้ type() ตรวจคำตอบ
#
# "Dragon Cave"
# 3
# 2.5
# False


print("\n--- Practice 2: Same look, different type ---")
# สร้างตัวแปรหนึ่งตัวเก็บเลข 25 และอีกตัวเก็บข้อความ "25"
# ใช้ type() พิสูจน์ว่าทั้งสองตัวมีชนิดข้อมูลต่างกัน


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
