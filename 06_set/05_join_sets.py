"""บทที่ 5: Join Sets — รวมและเปรียบเทียบ Set"""

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("--- Example 1: union() ---")
print(set_a.union(set_b))
print(set_a | set_b)


print("\n--- Example 2: intersection() ---")
print(set_a.intersection(set_b))
print(set_a & set_b)


print("\n--- Example 3: difference() ---")
print(set_a.difference(set_b))
print(set_a - set_b)


print("\n--- Example 4: symmetric_difference() ---")
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)


print("\n--- Typing Practice ---")
# team_a = {"Mali", "Ton", "Nida"}
# team_b = {"Nida", "Ploy"}
# print(team_a | team_b)
# print(team_a & team_b)
# print(team_a - team_b)


print("\n--- Your turn 1 ---")
art_club = {"Mali", "Ton", "Ploy"}
music_club = {"Ton", "Nida", "Ploy"}
# TODO 1: แสดงนักเรียนที่อยู่ในอย่างน้อยหนึ่งชมรม
# TODO 2: แสดงนักเรียนที่อยู่ในทั้งสองชมรม
# TODO 3: แสดงนักเรียนที่อยู่เฉพาะ art_club


# === คำถามเช็กความเข้าใจ ===
# 1. union เก็บสมาชิกแบบใด?
# 2. intersection เก็บสมาชิกแบบใด?
# 3. difference ของ A กับ B เหมือน difference ของ B กับ A หรือไม่?

