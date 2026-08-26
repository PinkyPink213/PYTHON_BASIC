"""บทที่ 3: Remove Dictionary Items"""

player = {"name": "Mali", "score": 20, "level": 2, "role": "wizard"}

print("--- Example 1: pop() ---")
removed_score = player.pop("score")
print(removed_score)
print(player)


print("\n--- Example 2: del ---")
del player["role"]
print(player)


print("\n--- Example 3: popitem() ---")
last_item = player.popitem()
print(last_item)
print(player)


print("\n--- Typing Practice ---")
# pet = {"name": "Milo", "age": 3, "color": "brown"}
# pet.pop("age")
# del pet["color"]
# print(pet)


print("\n--- Your turn 1 ---")
book = {"title": "Magic Door", "pages": 100, "price": 250}
# TODO 1: ใช้ pop() ลบ price และเก็บค่าที่ลบไว้
# TODO 2: ใช้ del ลบ pages แล้ว print(book)


# === คำถามเช็กความเข้าใจ ===
# 1. pop(key) ลบและคืนค่าอะไร?
# 2. popitem() ลบข้อมูลตำแหน่งใด?
# 3. clear() ทำอะไรกับ Dictionary?

