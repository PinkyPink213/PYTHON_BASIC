"""บทที่ 6: Frozenset — Set ที่ล็อกไว้"""

print("--- Example 1: Create a frozenset ---")
directions = frozenset({"north", "south", "east", "west"})
print(directions)
print(type(directions))


print("\n--- Example 2: Read and compare ---")
print("north" in directions)
safe_directions = frozenset({"north", "east"})
print(directions & safe_directions)

# directions.add("up")       # AttributeError
# directions.remove("north") # AttributeError


print("\n--- Typing Practice ---")
# game_rules = frozenset({"no cheating", "take turns", "have fun"})
# print(game_rules)
# print("have fun" in game_rules)


print("\n--- Your turn 1 ---")
# TODO 1: สร้าง frozenset ชื่อ weekdays มี monday ถึง friday
# แสดงค่า ชนิดข้อมูล และตรวจว่า monday อยู่ข้างในหรือไม่


# === คำถามเช็กความเข้าใจ ===
# 1. frozenset เพิ่มหรือลบสมาชิกได้หรือไม่?
# 2. ใช้ in กับ frozenset ได้หรือไม่?
# 3. frozenset ใช้ union และ intersection ได้หรือไม่?

