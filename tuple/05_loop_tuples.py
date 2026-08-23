"""บทที่ 5: Loop Tuples — อ่านสมาชิกทีละค่า"""

print("--- Example 1: for loop ---")
animals = ("cat", "dog", "rabbit")
for animal in animals:
    print(animal)


print("\n--- Example 2: Loop with if ---")
scores = (80, 45, 70)
for score in scores:
    if score >= 50:
        print(str(score) + " passed!")
    else:
        print(str(score) + " needs practice.")


print("\n--- Example 3: Loop with index ---")
for index in range(len(animals)):
    print(index, animals[index])


print("\n--- Typing Practice ---")
# พิมพ์ Tuple ของอาหาร 3 อย่าง
# ใช้ for แสดง "I like ..." ทีละอย่าง


print("\n--- Your turn 1 ---")
numbers = (2, 4, 6, 8)
# TODO 1: ใช้ for แสดง number ทุกค่า


print("\n--- Your turn 2 ---")
items = ("coin", "key", "map")
# TODO 2: ใช้ for กับ if เมื่อพบ "key" ให้แสดง "Key found!"
# ค่าอื่นให้แสดง "Checking ..."


# === คำถามเช็กความเข้าใจ ===
# 1. for เปลี่ยนสมาชิกใน Tuple หรือเพียงอ่านสมาชิก?
# 2. ใช้ if ข้างใน for ได้หรือไม่?
# 3. range(len(tuple)) ช่วยให้เราได้ข้อมูลอะไร?

