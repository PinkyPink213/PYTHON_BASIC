"""บทที่ 7: Set Methods Exercises"""

print("--- Example: issubset() and issuperset() ---")
all_powers = {"fly", "run", "jump", "swim"}
hero_powers = {"fly", "run"}
print(hero_powers.issubset(all_powers))
print(all_powers.issuperset(hero_powers))


print("\n--- Exercise 1: Unique names ---")
names = ["Mali", "Ton", "Mali", "Nida", "Ton"]
# TODO 1: ใช้ set() แปลง names เพื่อลบชื่อซ้ำ แล้ว print()


print("\n--- Exercise 2: Shared inventory ---")
player_1 = {"key", "map", "water"}
player_2 = {"torch", "map", "water"}
# TODO 2: หาของทั้งหมดของผู้เล่นทั้งสอง
# TODO 3: หาของที่ทั้งสองคนมีเหมือนกัน
# TODO 4: หาของที่ player_1 มีแต่ player_2 ไม่มี


print("\n--- Exercise 3: Required skills ---")
required_skills = {"swim", "run"}
my_skills = {"run", "jump", "swim"}
# TODO 5: ใช้ issubset() ตรวจว่ามีทักษะที่ต้องใช้ครบหรือไม่


# === คำถามเช็กความเข้าใจ ===
# 1. set(list) ช่วยจัดการข้อมูลซ้ำอย่างไร?
# 2. issubset() ใช้ตอบคำถามอะไร?
# 3. Set เหมาะกับการเปรียบเทียบกลุ่มข้อมูลอย่างไร?

