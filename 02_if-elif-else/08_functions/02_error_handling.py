"""บทที่ 2: Error Handling — จัดการข้อผิดพลาด"""

print("--- Example: try and except ---")
try:
    age = int(input("How old are you? "))
    print("Next year: " + str(age + 1))
except ValueError:
    print("Please enter a whole number.")

print("\n--- Example: else and finally ---")
try:
    number = int(input("Choose a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("You chose " + str(number))
finally:
    print("Program finished.")

print("\n--- Your turn ---")
# TODO: รับตัวเลขสองตัวแล้วหารกัน
# จัดการ ValueError และ ZeroDivisionError ด้วย except แยกกัน

# คำถาม: try, except, else และ finally ทำงานเมื่อใด?

