"""บทที่ 6.1: Mystery Animal Shop — While กับ if-elif-else"""

# ==================================================
# ที่มาของเกม
# ==================================================
# เกมนี้ดัดแปลงจาก Mystery Animal Shop ในบท if-elif-else
# เกมเดิมใช้ Nested if เขียนการทายครั้งที่ 1, 2 และ 3 แยกกัน
# ทำให้ต้องเขียน input() และการตรวจคำตอบซ้ำหลายครั้ง
#
# ในภาคนี้ เราจะใช้ while loop ทำขั้นตอนการทายเดิมซ้ำ
# และใช้ attempts นับว่าผู้เล่นทายไปแล้วกี่ครั้ง
# คำใบ้ทั้ง 3 ข้อเก็บไว้ใน List แล้วเลือกด้วย Index
#
# เป้าหมาย:
# - ทายสัตว์ให้ถูกภายใน 3 ครั้ง
# - ถ้าทายสัตว์ถูก จะเข้าสู่ Bonus Round ทายราคา
#
# ความรู้ที่ใช้:
# - List และ Index
# - while loop
# - for loop
# - len() และ range()
# - if, elif, else และ Boolean
# - if, elif, else ตรวจคำตอบหลายกรณี

print("==================================")
print("   MYSTERY ANIMAL SHOP: LOOP")
print("==================================")
print("Can you find the mystery animal?")

secret_item = "rabbit"
secret_price = 500
max_attempts = 3

# คำใบ้เก็บใน List จากยากไปง่าย
hints = [
    "Hint 1: It has long ears.",
    "Hint 2: Choose from cat, rabbit, or dog.",
    "Hint 3: The word starts with R."
]

print("\nAnimals in this shop:")
animals = ["cat", "rabbit", "dog"]

# for loop แสดงสัตว์ทุกตัวในร้านทีละตัว
for animal in animals:
    print("- " + animal)

attempts = 0
item_correct = False

# ทำซ้ำเมื่อยังทายไม่ครบ 3 ครั้ง และยังตอบไม่ถูก
while attempts < max_attempts and not item_correct:
    print("\n[ Guess " + str(attempts + 1) + " of " + str(max_attempts) + " ]")

    # attempts เริ่มจาก 0 จึงใช้เป็น Index ของ hints ได้พอดี
    print(hints[attempts])
    item_guess = input("What is the mystery animal? ").lower()

    # if-elif-else แยกคำตอบถูก คำตอบผิด และคำตอบที่ไม่มีในร้าน
    if item_guess == secret_item:
        item_correct = True
        print("*** Correct animal! ***")
    elif item_guess in animals:
        print("Oops! That is not the mystery animal.")
    else:
        print("That animal is not in this shop.")

    # เพิ่มจำนวนครั้งหลังจากทายแต่ละรอบ
    attempts += 1


# เมื่อ while จบ ใช้ if ตรวจว่าจบเพราะตอบถูกหรือใช้โอกาสหมด
if item_correct:
    print("You found it in " + str(attempts) + " guess(es)!")
    print("\n--- BONUS ROUND: GUESS THE PRICE ---")

    price_guess = int(input("How many baht does the rabbit cost? "))

    if price_guess == secret_price:
        print("*** PERFECT PRICE! YOU WIN! ***")
    elif price_guess < secret_price:
        print("The price is too low!")
    else:
        print("The price is too high!")
else:
    print("\n========== GAME OVER ==========")
    print("The mystery animal was " + secret_item + ".")
    print("Good try! Play again soon!")


# เปรียบเทียบกับเกมเดิม
# - เดิม: เขียน input() 3 ชุด และซ้อน Nested if
# - ใหม่: เขียน input() เพียงชุดเดียว แล้วให้ while ทำซ้ำ
# - เดิม: hint_1, hint_2 และ hint_3 เป็นตัวแปรแยกกัน
# - ใหม่: เก็บคำใบ้ใน hints แล้วใช้ hints[attempts]
# - เวอร์ชันนี้ยังใช้ if-elif-else เพื่อตรวจคำตอบ
# - บทที่ 6.2 จะให้ลองแปลงส่วนนี้เป็น match-case


# === คำถามเช็กความเข้าใจ ===
# 1. while loop จะทำงานต่อเมื่อมีสองเงื่อนไขใดเป็นจริง?
# 2. attempts ทำหน้าที่อะไรบ้าง?
# 3. เพราะอะไร hints[attempts] จึงแสดงคำใบ้ใหม่ในแต่ละรอบ?
# 4. ถ้าทายถูกครั้งแรก while จะถามต่อหรือไม่?
# 5. for loop ในเกมใช้ทำอะไร?
# 6. elif item_guess in animals ตรวจคำตอบแบบใด?
