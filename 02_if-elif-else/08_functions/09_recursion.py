"""บทที่ 9: Python Recursion — Function เรียกตัวเอง"""

def countdown(number):
    if number == 0:          # Base case: จุดหยุด
        print("Go!")
    else:
        print(number)
        countdown(number - 1)

countdown(3)


print("\n--- Your turn ---")
# TODO: สร้าง sum_to(number) ให้ return ผลรวม 1 ถึง number
# Base case: number == 1 ให้ return 1

# คำถาม: เพราะอะไร Recursion ต้องมี Base case?

