"""บทที่ 3: เปลี่ยนและเพิ่มของใน List"""

print("--- Example 1: Change an item ---")
fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"
print(fruits)


print("\n--- Example 2: append() adds to the end ---")
fruits.append("watermelon")
print(fruits)


print("\n--- Example 3: insert() chooses a position ---")
fruits.insert(1, "grape")
print(fruits)


print("\n--- Example 4: extend() adds many items ---")
fruits.extend(["cherry", "lemon"])
print(fruits)


print("\n--- Your turn 1 ---")
backpack = ["book", "pencil", "snack"]
# TODO 1: เปลี่ยน "pencil" เป็น "pen" ด้วย Index


print("\n--- Your turn 2 ---")
# TODO 2: ใช้ append() เพิ่ม "water" ต่อท้าย backpack


print("\n--- Your turn 3 ---")
# TODO 3: ใช้ insert() เพิ่ม "map" ที่ Index 0 แล้ว print(backpack)


print("\n--- Your turn 4: Add many items ---")
more_items = ["hat", "camera"]
# TODO 4: ใช้ extend() เพิ่มของจาก more_items เข้า backpack
# จากนั้น print(backpack)


print("\n--- Your turn 5: Change many items ---")
levels = ["easy", "easy", "hard", "hard"]
# TODO 5: ใช้ Slicing เปลี่ยนข้อมูลที่ Index 1 และ 2
# ให้เป็น "medium", "medium" แล้ว print(levels)


# === คำถามเช็กความเข้าใจ ===
# 1. append() เพิ่มข้อมูลไว้ตำแหน่งใด?
# 2. insert(0, "map") เพิ่ม map ไว้ตำแหน่งใด?
# 3. append(["a", "b"]) กับ extend(["a", "b"]) ให้ผลต่างกันอย่างไร?
