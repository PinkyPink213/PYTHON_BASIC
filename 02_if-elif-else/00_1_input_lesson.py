"""บทที่ 0.1: เรียนรู้ input() และ int(input())"""

# input() หยุดรอให้ผู้เล่นพิมพ์คำตอบแล้วกด Enter
# ค่าที่ได้จาก input() เป็น string หรือข้อความเสมอ

print("--- Example 1: Text input ---")
name = input("What is your name? ")
print("Hello, " + name + "!")


print("\n--- Band Name Generator ---")

# ขั้นที่ 1: รับชื่อเมือง
city = input("What city did you grow up in? ")

# ขั้นที่ 2: รับชื่อสัตว์เลี้ยง
pet = input("What is your pet's name? ")

# ขั้นที่ 3: รับเลขนำโชค
# ใช้ int() เปลี่ยนคำตอบจากข้อความให้เป็นจำนวนเต็ม
lucky_number = int(input("What is your lucky number? "))

# ขั้นที่ 4: ใช้ str() เปลี่ยนตัวเลขกลับเป็นข้อความเพื่อนำมาต่อกัน
print("Your band name is " + city + " " + pet + " " + str(lucky_number) + "!")


print("\n--- Example 2: Calculate with int input ---")
age = int(input("How old are you? "))
next_age = age + 1
print("Next year, you will be " + str(next_age) + " years old.")


# === คำถามเช็กความเข้าใจ ===
# 1. input() รอให้ผู้เล่นทำอะไร?
# 2. ทำไม lucky_number จึงใช้ int(input())?
# 3. ทำไมต้องใช้ str(lucky_number) เมื่อนำไปต่อกับชื่อวง?
