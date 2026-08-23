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


print("\n--- Typing Practice: พิมพ์ตาม ---")
# พิมพ์ตาม แล้วลองตอบด้วยเลขจำนวนเต็ม
# candies = int(input("How many candies do you have? "))
# total_candies = candies + 2
# print("Now you have " + str(total_candies) + " candies.")


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

