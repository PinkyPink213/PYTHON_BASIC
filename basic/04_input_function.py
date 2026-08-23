"""บทที่ 4: input() — รับคำตอบจากผู้ใช้"""

print("--- Example 1: Ask a question ---")
name = input("What is your name? ")
print("Hello, " + name + "!")


print("\n--- Example 2: Store many answers ---")
city = input("Where do you live? ")
favorite_food = input("What food do you like? ")
print("You live in " + city + " and like " + favorite_food + ".")


print("\n--- Example 3: Clean the answer ---")
color = input("Choose a color: ").strip().lower()
print("You chose " + color + ".")


print("\n--- Typing Practice: Make a welcome message ---")
# พิมพ์ตามแล้ว Run เพื่อตอบคำถามด้วยข้อมูลของตัวเอง
# player_name = input("What is your name? ")
# favorite_game = input("What game do you like? ")
# print("Hello, " + player_name + "! You like " + favorite_game + ".")


print("\n--- Your turn 1 ---")
# TODO 1: ถามชื่อสัตว์เลี้ยงด้วย input() แล้วแสดงข้อความทักทายสัตว์เลี้ยง


print("\n--- Your turn 2 ---")
# TODO 2: ถามชื่อโรงเรียนและวิชาที่ชอบ แล้วแสดงคำตอบในประโยคเดียว


print("\n--- Your turn 3 ---")
# TODO 3: ถามชื่อผู้เล่น ใช้ .strip().upper() แล้วแสดงชื่อที่ได้


# === คำถามเช็กความเข้าใจ ===
# 1. input() ทำให้โปรแกรมหยุดรออะไร?
# 2. ข้อความใน input("...") มีประโยชน์อย่างไร?
# 3. input() ให้ข้อมูลชนิดใดเสมอ?
