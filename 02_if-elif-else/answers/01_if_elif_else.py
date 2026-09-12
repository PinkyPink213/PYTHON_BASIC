"""เฉลยบทที่ 1: if, elif, else และเครื่องหมายเปรียบเทียบ"""

print("--- Meet the comparison operators ---")
print(5 == 5)
print(5 != 3)
print(8 > 4)
print(2 < 7)
print(5 >= 5)
print(3 <= 6)

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

# === แนวคำตอบ ===
# 1. = ใช้เก็บค่าลงตัวแปร ส่วน == ใช้เปรียบเทียบว่าสองค่าเท่ากันหรือไม่
# 2. True เพราะ 50 เท่ากับ 50 จึงผ่านเครื่องหมาย >=
# 3. Python เลือกเงื่อนไขแรกที่เป็น True ถ้าตรวจ >= 50 ก่อน คะแนน 80 ก็จะหยุดตรงนั้น

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
if pet != "dog":
    print("This pet is not a dog.")

print("\n--- Your turn 2: <= ---")
books = 3
if books <= 3:
    print("You can carry the books.")

print("\n--- Your turn 3: if, elif and else ---")
score = 75
if score >= 80:
    print("You got a gold star!")
elif score >= 50:
    print("Great job!")
else:
    print("Try again!")
