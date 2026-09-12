"""บทที่ 4: Loop Dictionaries"""

player = {"name": "Mali", "score": 20, "role": "wizard"}

print("--- Example 1: Loop through keys ---")
for key in player:
    print(key)


print("\n--- Example 2: keys() and values() ---")
for key in player.keys():
    print(key)

for value in player.values():
    print(value)


print("\n--- Example 3: items() ---")
for key, value in player.items():
    print(key + ": " + str(value))


print("\n--- Typing Practice ---")
# pet = {"name": "Milo", "animal": "cat", "age": 3}
# for key, value in pet.items():
#     print(key, value)


print("\n--- Your turn 1 ---")
scores = {"Mali": 80, "Ton": 45, "Nida": 90}
# TODO 1: ใช้ items() แสดงชื่อและคะแนนทุกคน
# TODO 2: ใช้ if แสดง "passed" เมื่อคะแนนตั้งแต่ 50 ขึ้นไป


# === คำถามเช็กความเข้าใจ ===
# 1. for ปกติอ่าน Key หรือ Value?
# 2. values() ให้ข้อมูลอะไร?
# 3. items() ให้ข้อมูลอะไรสองค่า?

