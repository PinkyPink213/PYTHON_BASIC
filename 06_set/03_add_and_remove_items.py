"""บทที่ 3: Add and Remove Set Items"""

print("--- Example 1: add() one item ---")
backpack = {"map", "water"}
backpack.add("rope")
print(backpack)


print("\n--- Example 2: update() many items ---")
backpack.update({"food", "torch"})
print(backpack)


print("\n--- Example 3: remove() and discard() ---")
backpack.remove("map")
backpack.discard("compass")  # ไม่มี compass ก็ไม่ Error
print(backpack)


print("\n--- Example 4: pop() and clear() ---")
removed_item = backpack.pop()  # ลบสมาชิกใดสมาชิกหนึ่ง
print("Removed: " + removed_item)
backpack.clear()
print(backpack)


print("\n--- Typing Practice ---")
# pets = {"cat", "dog"}
# pets.add("rabbit")
# pets.update({"fish", "bird"})
# pets.discard("dog")
# print(pets)


print("\n--- Your turn 1 ---")
skills = {"jump", "run"}
# TODO 1: ใช้ add() เพิ่ม swim
# TODO 2: ใช้ update() เพิ่ม climb และ fly


print("\n--- Your turn 2 ---")
# TODO 3: ใช้ remove() ลบ run
# TODO 4: ใช้ discard() ลบ dance ซึ่งไม่มีอยู่ แล้ว print(skills)


# === คำถามเช็กความเข้าใจ ===
# 1. add() และ update() ต่างกันอย่างไร?
# 2. remove() และ discard() ต่างกันอย่างไร?
# 3. pop() รู้ล่วงหน้าหรือไม่ว่าจะลบสมาชิกใด?

