"""บทที่ 5: match-case — เลือกทำงานตามค่าที่ได้รับ"""

# match-case ไม่ใช่ Loop และไม่ได้ทำคำสั่งซ้ำ
# match จะนำค่าหนึ่งค่าไปเปรียบเทียบกับ case จากบนลงล่าง
# เมื่อพบ case ที่ตรงกัน จะทำคำสั่งของ case นั้น

print("--- Example 1: Traffic light ---")
light = "green"

match light:
    case "red":
        print("Stop!")
    case "yellow":
        print("Get ready.")
    case "green":
        print("Go!")
    case _:
        print("Unknown light.")


print("\n--- Example 2: Many answers in one case ---")
answer = "y"

# | แปลว่า หรือ จึงรองรับคำตอบได้มากกว่าหนึ่งแบบ
match answer:
    case "yes" | "y":
        print("You chose yes.")
    case "no" | "n":
        print("You chose no.")
    case _:
        print("Please answer yes or no.")


print("\n--- Example 3: Number with Guard ---")
score = 75

# Guard คือเงื่อนไข if ที่เขียนต่อท้าย case
match score:
    case 100:
        print("Perfect score!")
    case value if value >= 50:
        print("Passed!")
    case _:
        print("Try again!")


print("\n--- Your turn 1: Day activity ---")
day = "saturday"
# TODO 1: ใช้ match ตรวจ day
# saturday หรือ sunday -> print("Weekend fun!")
# monday -> print("Back to school.")
# วันอื่น -> print("Normal school day.")


print("\n--- Your turn 2: Simple calculator ---")
operator = input("Choose +, -, or *: ")
number_1 = 8
number_2 = 2
# TODO 2: ใช้ match ตรวจ operator แล้วแสดงผลคำนวณ
# + ใช้บวก, - ใช้ลบ และ * ใช้คูณ
# เครื่องหมายอื่น -> print("Unknown operator.")


print("\n--- Your turn 3: Animal sounds ---")
animal = input("Choose cat, dog, or duck: ").lower()
# TODO 3: ใช้ match แสดงเสียงสัตว์
# cat -> "Meow!"
# dog -> "Woof!"
# duck -> "Quack!"
# สัตว์อื่น -> "I do not know that sound."


print("\n--- Your turn 4: Ticket price ---")
age = 10
# TODO 4: ใช้ match และ Guard ตรวจ age
# อายุต่ำกว่า 6 ปี -> print("Free ticket")
# อายุต่ำกว่า 13 ปี -> print("Child ticket")
# นอกนั้น -> print("Regular ticket")


# === คำถามเช็กความเข้าใจ ===
# 1. match-case ทำคำสั่งซ้ำหรือไม่?
# 2. case _ ทำหน้าที่คล้าย else อย่างไร?
# 3. เครื่องหมาย | ใน case ใช้ทำอะไร?
# 4. Guard คืออะไร?

