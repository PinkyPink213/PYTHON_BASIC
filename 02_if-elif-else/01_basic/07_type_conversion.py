"""บทที่ 7: Type Conversion / Casting — เปลี่ยนชนิดข้อมูล"""

# input() ให้ผลเป็น String เสมอ
# ถ้าต้องการคำนวณ ต้องแปลงเป็นตัวเลขก่อน
# int()   แปลงเป็นจำนวนเต็ม
# float() แปลงเป็นจำนวนทศนิยม
# str()   แปลงเป็นข้อความ


print("--- Example 1: String to int ---")
age_text = "10"
age = int(age_text)
print(age + 1)


print("\n--- Example 2: String to float ---")
price_text = "25.5"
price = float(price_text)
print(price + 10)


print("\n--- Example 3: Number to String ---")
score = 50
print("Your score is " + str(score) + ".")


print("\n--- Practice 1: Convert to int ---")
# ถามจำนวนลูกอมจากผู้ใช้ แล้วแปลงคำตอบเป็น int
# เพิ่มลูกอมอีก 2 เม็ด และแสดงจำนวนใหม่


print("\n--- Practice 2: Convert to float ---")
# กำหนดข้อความ "19.5" แล้วแปลงเป็น float
# เพิ่มค่าอีก 0.5 และแสดงผลลัพธ์


print("\n--- Practice 3: Convert to str ---")
# กำหนดคะแนนเป็นตัวเลข แล้วใช้ str() เพื่อนำคะแนนไปต่อกับข้อความ


print("\n--- Your turn 1 ---")
# TODO 1: ถามอายุด้วย int(input())
# คำนวณอายุในปีถัดไป แล้วแสดงผลด้วย str()


print("\n--- Your turn 2 ---")
# TODO 2: ถามส่วนสูงด้วย float(input())
# เพิ่มส่วนสูงอีก 5.5 แล้ว print ผลลัพธ์


# === คำถามเช็กความเข้าใจ ===
# 1. input() ให้ข้อมูลชนิดใด?
# 2. int() และ float() ต่างกันอย่างไร?
# 3. เพราะอะไรจึงใช้ str() เมื่อต่อเลขกับข้อความด้วย +?
