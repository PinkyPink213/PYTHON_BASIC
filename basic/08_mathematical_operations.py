"""บทที่ 8: Mathematical Operations — การคำนวณ"""

print("--- Basic operators ---")
print(10 + 3)   # บวก
print(10 - 3)   # ลบ
print(10 * 3)   # คูณ
print(10 / 3)   # หาร ได้ float
print(10 // 3)  # หารปัดเศษลง
print(10 % 3)   # เศษจากการหาร
print(2 ** 3)   # ยกกำลัง


print("\n--- Order of operations ---")
print(2 + 3 * 4)      # คูณก่อนบวก
print((2 + 3) * 4)    # วงเล็บก่อน


print("\n--- Update a value ---")
score = 10
score += 5
score -= 2
print(score)


print("\n--- Typing Practice: Mini calculator ---")
# พิมพ์ตาม แล้วทายคำตอบก่อนกด Run
# number_1 = 12
# number_2 = 4
# print(number_1 + number_2)
# print(number_1 - number_2)
# print(number_1 * number_2)
# print(number_1 / number_2)


print("\n--- Your turn 1: Candy calculator ---")
candies = 12
friends = 3
# TODO 1: ใช้ // หาว่าเพื่อนแต่ละคนได้ลูกอมกี่เม็ด
# TODO 2: ใช้ % หาว่าเหลือลูกอมกี่เม็ด


print("\n--- Your turn 2: Rectangle ---")
width = 5
height = 3
# TODO 3: คำนวณพื้นที่ width * height และเส้นรอบรูป 2 * (width + height)


print("\n--- Your turn 3: Game score ---")
game_score = 20
# TODO 4: เพิ่ม 10 ด้วย += จากนั้นลด 5 ด้วย -= แล้ว print(game_score)


# === คำถามเช็กความเข้าใจ ===
# 1. / และ // ให้ผลต่างกันอย่างไร?
# 2. % ใช้หาอะไร?
# 3. วงเล็บเปลี่ยนลำดับการคำนวณอย่างไร?
