"""บทที่ 4.1: Returning Functions — return กับ print ต่างกันอย่างไร"""

# print() แสดงข้อมูลบนหน้าจอ แต่ไม่ได้ส่งค่ากลับ
# return ส่งค่ากลับไปยังตำแหน่งที่เรียก Function


print("--- Example 1: Function with print ---")
def show_double(number):
    print(number * 2)

printed_result = show_double(5)
print("Value from show_double: " + str(printed_result))
# Function แสดง 10 แต่ printed_result เป็น None


print("\n--- Example 2: Function with return ---")
def get_double(number):
    return number * 2

returned_result = get_double(5)
print("Value from get_double: " + str(returned_result))


print("\n--- Example 3: Use a returned value ---")
answer = get_double(5) + 3
print(answer)

# return ทำให้เรานำค่าที่ได้ไปเก็บในตัวแปรและคำนวณต่อได้


print("\n--- Example 4: Code after return ---")
def make_message(name):
    return "Hello, " + name + "!"
    print("This line will not run.")

print(make_message("Mali"))
# เมื่อ Function พบ return จะออกจาก Function ทันที


print("\n--- Typing Practice ---")
# พิมพ์ตาม แล้วทายว่า area มีค่าเท่าไร
# def rectangle_area(width, height):
#     return width * height
#
# area = rectangle_area(5, 3)
# print(area)


print("\n--- Your turn 1 ---")
# TODO 1: สร้าง Function add(a, b) ที่ return ผลบวก
# เก็บผลลัพธ์ในตัวแปร total แล้ว print(total)


print("\n--- Your turn 2 ---")
# TODO 2: สร้าง Function create_title(name)
# ให้ return ข้อความ "*** name ***"
# เรียก Function แล้วนำข้อความที่ได้ไปต่อกับ " Welcome!"


print("\n--- Your turn 3: Compare ---")
# TODO 3: สร้าง Function สองตัวที่คำนวณ number * 3 เหมือนกัน
# Function แรกใช้ print() และ Function ที่สองใช้ return
# เก็บผลจากทั้งสอง Functionในตัวแปร แล้ว print เพื่อเปรียบเทียบ


# === คำถามเช็กความเข้าใจ ===
# 1. print() และ return ทำหน้าที่ต่างกันอย่างไร?
# 2. Function ที่ไม่มี return ส่งค่าอะไรกลับมา?
# 3. โค้ดหลัง return ใน Function จะทำงานหรือไม่?
# 4. เมื่อใดควรใช้ return แทน print()?

