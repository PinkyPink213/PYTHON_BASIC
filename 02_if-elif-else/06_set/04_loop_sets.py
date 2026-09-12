"""บทที่ 4: Loop Sets"""

print("--- Example 1: Read every item ---")
colors = {"red", "green", "blue"}
for color in colors:
    print(color)


print("\n--- Example 2: Count matching items ---")
numbers = {1, 2, 3, 4, 5, 6}
even_count = 0

for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even.")
        even_count += 1

print("Even numbers: " + str(even_count))


print("\n--- Typing Practice ---")
# animals = {"cat", "dog", "rabbit"}
# for animal in animals:
#     print("I found a " + animal + "!")


print("\n--- Your turn 1 ---")
scores = {40, 55, 70, 90}
# TODO 1: ใช้ for และ if แสดงเฉพาะคะแนนตั้งแต่ 50 ขึ้นไป


print("\n--- Your turn 2 ---")
items = {"coin", "key", "map"}
# TODO 2: ใช้ for ตรวจของ ถ้าพบ key ให้แสดง "Key found!"
# ค่าอื่นให้แสดง "Checking ..."


# === คำถามเช็กความเข้าใจ ===
# 1. for ใช้อ่านสมาชิก Set ได้หรือไม่?
# 2. ควรใช้ Index ร่วมกับ Set หรือไม่?
# 3. if สามารถอยู่ข้างใน for ได้หรือไม่?

