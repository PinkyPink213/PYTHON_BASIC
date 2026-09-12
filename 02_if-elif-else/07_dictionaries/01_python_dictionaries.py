"""บทที่ 1: Python Dictionaries และ Access Items"""

print("--- Example 1: Key and value ---")
player = {"name": "Mali", "score": 10, "role": "wizard"}
print(player)
print(player["name"])
print(player.get("score"))


print("\n--- Example 2: Check a key ---")
if "role" in player:
    print("Role found!")


print("\n--- Typing Practice ---")
# pet = {"name": "Milo", "animal": "cat", "age": 3}
# print(pet["name"])
# print(pet.get("animal"))


print("\n--- Your turn 1 ---")
# TODO 1: สร้าง Dictionary หนังสือ มี title, author และ pages
# แสดง title ด้วย [] และ pages ด้วย get()


print("\n--- Your turn 2 ---")
# TODO 2: ถ้า key "author" อยู่ใน Dictionary ให้แสดง "Author found!"


# === คำถามเช็กความเข้าใจ ===
# 1. Dictionary เก็บข้อมูลเป็นคู่แบบใด?
# 2. Key ซ้ำกันได้หรือไม่?
# 3. [] และ get() ใช้ทำอะไร?

