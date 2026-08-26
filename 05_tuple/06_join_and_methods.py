"""บทที่ 6: Join Tuples และ Tuple Methods"""

print("--- Example 1: Join with + ---")
team_a = ("Mali", "Ton")
team_b = ("Nida", "Ploy")
all_players = team_a + team_b
print(all_players)


print("\n--- Example 2: Multiply a tuple ---")
sound = ("beep",)
print(sound * 3)


print("\n--- Example 3: count() ---")
votes = ("cat", "dog", "cat", "rabbit", "cat")
print(votes.count("cat"))


print("\n--- Example 4: index() ---")
print(votes.index("rabbit"))


print("\n--- Typing Practice ---")
# สร้าง Tuple สองชุด รวมด้วย + แล้วใช้ count() และ index() กับผลลัพธ์


print("\n--- Your turn 1 ---")
morning = ("wake up", "breakfast")
school = ("study", "read")
# TODO 1: รวมเป็น all_tasks แล้ว print()


print("\n--- Your turn 2 ---")
stars = ("gold", "silver", "gold", "bronze", "gold")
# TODO 2: ใช้ count() นับ "gold"
# TODO 3: ใช้ index() หาตำแหน่งแรกของ "bronze"


# === คำถามเช็กความเข้าใจ ===
# 1. + แก้ Tuple เดิมหรือสร้าง Tuple ใหม่?
# 2. count() คืนค่าอะไร?
# 3. index() คืนค่าอะไรเมื่อมีค่าซ้ำหลายตัว?

