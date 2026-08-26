"""บทที่ 9.1: Mini Project — Adventure Profile Generator"""

# โปรเจกต์ตัวอย่างรวม print, variables, strings, input,
# data types, type conversion และการคำนวณ

print("==================================")
print("     ADVENTURE PROFILE MAKER")
print("==================================")

name = input("What is your name? ").strip()
age = int(input("How old are you? "))
favorite_animal = input("What is your favorite animal? ").strip().lower()
lucky_number = int(input("What is your lucky number? "))

next_age = age + 1
double_lucky_number = lucky_number * 2
hero_name = name + " the " + favorite_animal.title()

print("\n--- YOUR ADVENTURE PROFILE ---")
print(f"Hero name: {hero_name}")
print(f"Age next year: {next_age}")
print(f"Super lucky number: {double_lucky_number}")
print("Your adventure begins now!")


# === คำถามเช็กความเข้าใจ ===
# 1. เพราะอะไร age และ lucky_number จึงใช้ int(input())?
# 2. hero_name เกิดจากการต่อ String ใดบ้าง?
# 3. next_age และ double_lucky_number คำนวณอย่างไร?

