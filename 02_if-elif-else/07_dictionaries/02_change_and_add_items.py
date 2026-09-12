"""บทที่ 2: Change and Add Dictionary Items"""

player = {"name": "Mali", "score": 10}

print("--- Example 1: Change a value ---")
player["score"] = 20
print(player)


print("\n--- Example 2: Add a new item ---")
player["level"] = 2
print(player)


print("\n--- Example 3: update() ---")
player.update({"score": 30, "role": "knight"})
print(player)


print("\n--- Typing Practice ---")
# pet = {"name": "Milo", "age": 3}
# pet["age"] = 4
# pet["color"] = "brown"
# print(pet)


print("\n--- Your turn 1 ---")
game = {"title": "Dragon Cave", "players": 1}
# TODO 1: เปลี่ยน players เป็น 2
# TODO 2: เพิ่ม key "difficulty" มีค่า "easy"


print("\n--- Your turn 2 ---")
# TODO 3: ใช้ update() เปลี่ยน difficulty เป็น hard และเพิ่ม lives = 3


# === คำถามเช็กความเข้าใจ ===
# 1. ใช้ Key เดิมแล้วกำหนดค่าใหม่เกิดอะไรขึ้น?
# 2. ใช้ Key ใหม่แล้วกำหนดค่าเกิดอะไรขึ้น?
# 3. update() เปลี่ยนและเพิ่มข้อมูลพร้อมกันได้หรือไม่?

