"""บทที่ 5.2: Nested List — List ที่อยู่ใน List"""

print("--- Example: Student cards ---")
students = [
    ["Mali", 85],
    ["Ton", 72],
    ["Nida", 90]
]

print(students[0])     # การ์ดนักเรียนใบแรก
print(students[0][0])  # ชื่อในการ์ดใบแรก
print(students[0][1])  # คะแนนในการ์ดใบแรก


print("\n--- Your turn 1: Open a treasure map ---")
treasure_map = [
    ["tree", "rock"],
    ["river", "treasure"]
]
# TODO 1: แสดง "river" ด้วย Index สองชั้น
# TODO 2: แสดง "treasure" ด้วย Index สองชั้น


print("\n--- Your turn 2: Change a score ---")
# TODO 3: เปลี่ยนคะแนนของ Ton จาก 72 เป็น 80 ด้วย Index สองชั้น
# จากนั้น print(students)


# === คำถามเช็กความเข้าใจ ===
# 1. students[0] ได้ข้อมูลหนึ่งค่าหรือได้ List ชั้นใน?
# 2. students[0][1] หมายถึงอะไร?
# 3. Nested List มีประโยชน์เมื่อข้อมูลแต่ละชุดมีหลายค่าอย่างไร?

