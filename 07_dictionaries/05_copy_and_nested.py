"""บทที่ 5: Copy and Nested Dictionaries"""

print("--- Example 1: copy() ---")
original = {"name": "Mali", "score": 10}
copied = original.copy()
copied["score"] = 50
print(original)
print(copied)


print("\n--- Example 2: Nested Dictionary ---")
students = {
    "student_1": {"name": "Mali", "score": 80},
    "student_2": {"name": "Ton", "score": 70}
}
print(students["student_1"]["name"])
print(students["student_2"]["score"])


print("\n--- Typing Practice ---")
# pets = {
#     "pet_1": {"name": "Milo", "animal": "cat"},
#     "pet_2": {"name": "Lucky", "animal": "dog"}
# }
# print(pets["pet_1"]["name"])


print("\n--- Your turn 1 ---")
# TODO 1: copy() ข้อมูล student_1 แล้วเปลี่ยน score ในตัว Copy
# ตรวจว่า Dictionary เดิมไม่เปลี่ยน


print("\n--- Your turn 2 ---")
# TODO 2: เพิ่ม student_3 ซึ่งมี name และ score ลงใน students
# แสดงชื่อของ student_3 ด้วย Key สองชั้น


# === คำถามเช็กความเข้าใจ ===
# 1. ทำไมจึงใช้ copy() เมื่อต้องการแก้ข้อมูลแยกกัน?
# 2. Nested Dictionary คืออะไร?
# 3. เข้าถึงข้อมูลชั้นในด้วย Key กี่ครั้ง?

