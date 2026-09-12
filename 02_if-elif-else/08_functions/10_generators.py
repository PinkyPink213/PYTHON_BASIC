"""บทที่ 10: Python Generators — ส่งค่าทีละค่า"""

def count_up(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for number in count_up(3):
    print(number)


print("\n--- Your turn ---")
# TODO: สร้าง even_numbers(limit) ใช้ yield ส่งเลขคู่ตั้งแต่ 2 ถึง limit
# จากนั้นใช้ for แสดงผล

# คำถาม: yield ต่างจาก return อย่างไร?

