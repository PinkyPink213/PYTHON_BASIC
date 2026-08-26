"""บทที่ 5: ใช้ List ร่วมกับ if, elif และ else"""

print("--- Example 1: Check with in ---")
inventory = ["key", "map", "torch"]

if "key" in inventory:
    print("You can open the door!")
else:
    print("The door is locked.")


print("\n--- Example 2: Check with not in ---")
if "potion" not in inventory:
    print("You should find a potion.")


print("\n--- Example 3: Decide with len() ---")
if len(inventory) >= 5:
    print("Your backpack is full.")
elif len(inventory) >= 3:
    print("Your backpack has some space.")
else:
    print("Your backpack is almost empty.")


print("\n--- Your turn 1 ---")
foods = ["rice", "egg", "banana"]
# TODO 1: ถ้า "egg" อยู่ใน foods ให้ print("We can cook fried rice!")
# ถ้าไม่อยู่ ให้ print("We need an egg.")


print("\n--- Your turn 2 ---")
# TODO 2: ถ้า "milk" ไม่อยู่ใน foods ให้เพิ่มด้วย append()
# จากนั้น print(foods)


print("\n--- Your turn 3: Backpack size ---")
backpack = ["map", "water", "rope", "torch"]
# TODO 3: ใช้ len(), if, elif และ else ตรวจจำนวนของ
# 4 ชิ้นขึ้นไป -> print("Backpack is full.")
# 2 ชิ้นขึ้นไป -> print("There is some space.")
# น้อยกว่า 2 ชิ้น -> print("Backpack is almost empty.")


print("\n--- Your turn 4: Two required items ---")
# TODO 4: ถ้ามีทั้ง "water" และ "rope" ใน backpack
# ให้ print("You are ready for the island!")
# ถ้าของไม่ครบ ให้ print("You need more supplies.")


# === คำถามเช็กความเข้าใจ ===
# 1. in ใช้ตรวจอะไร?
# 2. not in ให้ผล True เมื่อใด?
# 3. ถ้า inventory มี 3 ชิ้น ตัวอย่างที่ 3 จะแสดงข้อความใด?
