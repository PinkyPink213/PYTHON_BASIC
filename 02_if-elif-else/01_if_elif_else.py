"""บทที่ 1: if, elif, else และเครื่องหมายเปรียบเทียบ"""

# เครื่องหมายเปรียบเทียบให้ผลเป็น True หรือ False
print("--- Meet the comparison operators ---")
print(5 == 5)   # == เท่ากับ
print(5 != 3)   # != ไม่เท่ากับ
print(8 > 4)    # >  มากกว่า
print(2 < 7)    # <  น้อยกว่า
print(5 >= 5)   # >= มากกว่าหรือเท่ากับ
print(3 <= 6)   # <= น้อยกว่าหรือเท่ากับ


print("\n--- Example 1: if ---")
age = 10
if age >= 8:
    print("You can join the game!")


print("\n--- Example 2: if and else ---")
answer = "cat"
if answer == "cat":
    print("Correct answer!")
else:
    print("Try again!")


print("\n--- Example 3: if, elif and else ---")
temperature = 25
if temperature > 30:
    print("It is hot.")
elif temperature < 20:
    print("It is cool.")
else:
    print("It is a nice day.")


print("\n--- Your turn 1: != ---")
pet = "cat"
# TODO 1: ถ้า pet ไม่เท่ากับ "dog"
# ให้ print("This pet is not a dog.")
pass


print("\n--- Your turn 2: <= ---")
books = 3
# TODO 2: ถ้า books น้อยกว่าหรือเท่ากับ 3
# ให้ print("You can carry the books.")
pass


print("\n--- Your turn 3: if, elif and else ---")
score = 75
# TODO 3: 80 ขึ้นไป -> print("You got a gold star!")
# 50 ขึ้นไป -> print("Great job!")
# น้อยกว่า 50 -> print("Try again!")
pass

# ลองเปลี่ยนค่าตัวแปร แล้วสังเกตว่าผลเปลี่ยนอย่างไร


# === คำถามเช็กความเข้าใจ ===
# ตอบด้วยคำพูดก่อน แล้วค่อยลองรันโค้ดเพื่อตรวจคำตอบ
# 1. เครื่องหมาย == กับ = ใช้ต่างกันอย่างไร?
# 2. ถ้า score = 50 เงื่อนไข score >= 50 จะเป็น True หรือ False?
# 3. เพราะอะไรจึงควรตรวจ score >= 80 ก่อน score >= 50?
