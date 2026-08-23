"""บทที่ 7: Type Conversion / Casting — เปลี่ยนชนิดข้อมูล"""

# Casting คือการใช้ฟังก์ชันสร้างข้อมูลเป็นชนิดที่ต้องการ
# int()   -> จำนวนเต็ม
# float() -> จำนวนทศนิยม
# str()   -> ข้อความ
# bool()  -> Boolean

print("--- Example 1: str to int ---")
age_text = "10"
age_number = int(age_text)
print(age_number + 1)


print("\n--- Example 2: str to float ---")
price_text = "25.5"
price_number = float(price_text)
print(price_number + 10)


print("\n--- Example 3: number to str ---")
score = 50
print("Your score is " + str(score) + ".")


print("\n--- Example 4: input with int ---")
number = int(input("Choose a whole number: "))
print(number + 5)


print("\n--- Example 5: Cast to bool ---")
print(bool(1))    # True
print(bool(0))    # False
print(bool("Hi")) # True เพราะ String ไม่ว่าง
print(bool(""))   # False เพราะเป็น String ว่าง


print("\n--- Typing Practice: Fix a calculation ---")
# พิมพ์ตามเพื่อฝึก Casting จาก input เป็น int และจาก int เป็น str
# candies = int(input("How many candies do you have? "))
# total_candies = candies + 2
# print("Now you have " + str(total_candies) + " candies.")


print("\n--- Your turn 1 ---")
coins_text = "20"
# TODO 1: ใช้ int() เปลี่ยน coins_text แล้วบวกอีก 5


print("\n--- Your turn 2 ---")
temperature = 32.5
# TODO 2: ใช้ str() ต่อ temperature กับข้อความ "Temperature: "


print("\n--- Your turn 3 ---")
# TODO 3: ถามอายุด้วย int(input()) แล้วแสดงอายุในปีถัดไป


print("\n--- Your turn 4 ---")
# TODO 4: ใช้ bool() แปลงค่า 1, 0, "Python" และ ""
# ทายผลก่อน แล้ว print() เพื่อตรวจคำตอบ


# === คำถามเช็กความเข้าใจ ===
# 1. เพราะอะไรจึงคำนวณ "10" + 1 ไม่ได้?
# 2. int(), float(), str() และ bool() ทำหน้าที่อะไร?
# 3. int(input()) ต่างจาก input() อย่างไร?
# 4. ค่าใดบ้างที่ bool() เปลี่ยนเป็น False ในตัวอย่างนี้?
