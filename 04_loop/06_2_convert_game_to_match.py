"""บทที่ 6.2: แปลงเกมจาก if-elif-else เป็น match-case"""

# เกมนี้คัดลอกมาจาก 06_1_mystery_animal_while_game.py
# โค้ดส่วนอื่นเขียนไว้ให้ครบแล้ว
# ให้น้องแก้เฉพาะ 2 จุดที่มี TODO โดยแปลง if-elif-else เป็น match-case

print("==================================")
print("  MYSTERY ANIMAL SHOP: MATCH")
print("==================================")

secret_item = "rabbit"
secret_price = 500
max_attempts = 3
animals = ["cat", "rabbit", "dog"]
hints = [
    "Hint 1: It has long ears.",
    "Hint 2: Choose from cat, rabbit, or dog.",
    "Hint 3: The word starts with R."
]

print("Animals in this shop:")
for animal in animals:
    print("- " + animal)

attempts = 0
item_correct = False

while attempts < max_attempts and not item_correct:
    print("\n[ Guess " + str(attempts + 1) + " of " + str(max_attempts) + " ]")
    print(hints[attempts])
    item_guess = input("What is the mystery animal? ").lower()

    # TODO 1: แปลง if-elif-else ที่คอมเมนต์ไว้เป็น match-case
    # if item_guess == secret_item:
    #     item_correct = True
    #     print("*** Correct animal! ***")
    # elif item_guess in animals:
    #     print("Oops! That is not the mystery animal.")
    # else:
    #     print("That animal is not in this shop.")
    #
    # ใช้ case "rabbit", case "cat" | "dog" และ case _
    pass  # ลบ pass หลังเขียน match-case

    attempts += 1

if item_correct:
    print("You found it in " + str(attempts) + " guess(es)!")
    print("\n--- BONUS ROUND: GUESS THE PRICE ---")
    price_guess = int(input("How many baht does the rabbit cost? "))

    # TODO 2: แปลง if-elif-else ที่คอมเมนต์ไว้เป็น match-case
    # if price_guess == secret_price:
    #     print("*** PERFECT PRICE! YOU WIN! ***")
    # elif price_guess < secret_price:
    #     print("The price is too low!")
    # else:
    #     print("The price is too high!")
    #
    # ใช้ case 500, Match Guard สำหรับราคาต่ำ และ case _
    pass  # ลบ pass หลังเขียน match-case
else:
    print("\n========== GAME OVER ==========")
    print("The mystery animal was " + secret_item + ".")
    print("Good try! Play again soon!")


# === ทดลองหลังเขียนเสร็จ ===
# 1. ตอบ rabbit ถูกและทายราคา 500
# 2. ตอบ cat หรือ dog ก่อน แล้วค่อยตอบ rabbit
# 3. พิมพ์ชื่อสัตว์ที่ไม่มีในร้าน
# 4. ทายราคาต่ำกว่าและสูงกว่า 500

