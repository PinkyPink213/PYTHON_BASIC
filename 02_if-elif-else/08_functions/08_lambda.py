"""บทที่ 8: Python Lambda — Function สั้นหนึ่งบรรทัด"""

double = lambda number: number * 2
add = lambda a, b: a + b

print(double(5))
print(add(3, 4))

students = [("Mali", 80), ("Ton", 95), ("Nida", 70)]
students.sort(key=lambda student: student[1])
print(students)

print("\n--- Your turn ---")
# TODO 1: สร้าง lambda ชื่อ square คืนเลขยกกำลังสอง
# TODO 2: สร้าง lambda รับ name แล้วคืน "Hello, name!"

# คำถาม: Lambda เหมาะกับ Function แบบสั้นอย่างไร?

