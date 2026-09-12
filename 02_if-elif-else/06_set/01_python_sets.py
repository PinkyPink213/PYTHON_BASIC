"""บทที่ 1: Python Sets — กล่องของที่ไม่เก็บของซ้ำ"""

print("--- Example 1: Create a set ---")
animals = {"cat", "dog", "rabbit"}
print(animals)


print("\n--- Example 2: Duplicate values disappear ---")
votes = {"cat", "dog", "cat", "rabbit", "cat"}
print(votes)
print(len(votes))


print("\n--- Example 3: Empty set ---")
empty_set = set()
print(type(empty_set))


print("\n--- Typing Practice ---")
# colors = {"red", "green", "blue", "red"}
# print(colors)
# print(len(colors))


print("\n--- Your turn 1 ---")
# TODO 1: สร้าง Set ชื่อ fruits มี apple, banana, orange และ apple ซ้ำ
# แสดง Set และจำนวนสมาชิก


print("\n--- Your turn 2 ---")
# TODO 2: สร้าง Set ว่างชื่อ backpack แล้วใช้ type() ตรวจ


# === คำถามเช็กความเข้าใจ ===
# 1. Set เก็บค่าซ้ำหรือไม่?
# 2. Set ว่างสร้างด้วยคำสั่งใด?
# 3. ลำดับสมาชิกใน Set แน่นอนหรือไม่?

