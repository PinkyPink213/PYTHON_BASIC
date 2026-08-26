"""บทที่ 4: Unpack Tuples — แกะข้อมูลใส่ตัวแปร"""

print("--- Example 1: Basic unpacking ---")
player = ("Mali", 10, "wizard")
name, age, role = player
print(name)
print(age)
print(role)


print("\n--- Example 2: Use * to collect values ---")
colors = ("red", "green", "blue", "yellow")
first, *middle, last = colors
print(first)
print(middle)
print(last)


print("\n--- Typing Practice ---")
# พิมพ์ Tuple point = (5, 8)
# Unpack เป็น x, y แล้วแสดง "X: 5" และ "Y: 8"


print("\n--- Your turn 1 ---")
pet = ("Milo", "cat", 3)
# TODO 1: Unpack เป็น pet_name, animal_type, pet_age แล้ว print ทุกค่า


print("\n--- Your turn 2 ---")
medals = ("gold", "silver", "bronze", "special")
# TODO 2: Unpack ตัวแรกลง first_medal และที่เหลือลง other_medals ด้วย *


# === คำถามเช็กความเข้าใจ ===
# 1. จำนวนตัวแปรต้องสัมพันธ์กับจำนวนสมาชิกอย่างไร?
# 2. เครื่องหมาย * ช่วยเก็บค่าอย่างไร?
# 3. ตัวแปรที่มี * ได้ข้อมูลชนิด Tuple หรือ List?

