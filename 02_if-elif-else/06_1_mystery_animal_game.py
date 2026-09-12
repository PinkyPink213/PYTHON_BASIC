"""บทที่ 6.1: เกมตัวอย่างสำหรับครู — Mystery Animal Shop"""

print("==================================")
print("     MYSTERY ANIMAL SHOP")
print("==================================")
print(" /\\_/\\")
print("( o.o )")
print(" > ^ <")
print("Can you find the mystery animal?")
print("You have 3 guesses!")

# เกมนี้มีเพียงหมวด animal เพื่อให้กติกาเข้าใจง่าย
category = "animal"
secret_item = "rabbit"
secret_price = 500

# คำใบ้จะง่ายขึ้นทีละระดับ
hint_1 = "Hint 1: It has long ears."
hint_2 = "Hint 2: Choose from cat, rabbit, or dog."
hint_3 = "Hint 3: The word starts with R."

print("Category: " + category)

# ผู้เล่นมีโอกาสทาย 3 ครั้งโดยใช้ nested if
item_correct = False

# ครั้งที่ 1
print("\n[ Guess 1 of 3 ]")
print(hint_1)
item_guess = input("What is the mystery animal? (use lowercase): ")

if item_guess == secret_item:
    item_correct = True
    print("*** Correct animal! ***")
else:
    print("Oops! That is not the animal.")

    # ครั้งที่ 2 จะทำงานเมื่อครั้งแรกตอบผิด
    print("\n[ Guess 2 of 3 ]")
    print(hint_2)
    item_guess = input("What is the mystery animal? (use lowercase): ")

    if item_guess == secret_item:
        item_correct = True
        print("*** Correct animal! ***")
    else:
        print("Oops! That is not the animal.")

        # ครั้งที่ 3 จะทำงานเมื่อสองครั้งแรกตอบผิด
        print("\n[ Final Guess ]")
        print(hint_3)
        item_guess = input("What is the mystery animal? (use lowercase): ")

        if item_guess == secret_item:
            item_correct = True
            print("*** Correct animal! ***")
        else:
            print("Oops! That is not the animal.")

# เมื่อทายสัตว์ถูก จึงเข้าสู่ด่านทายราคา
if item_correct:
    print("\n--- BONUS ROUND: GUESS THE PRICE ---")
    price_guess = int(input("How many baht does it cost? "))

    if price_guess == secret_price:
        print("**********************************")
        print("   PERFECT PRICE! YOU WIN!")
        print("**********************************")
    elif price_guess < secret_price:
        print("The price is too low!")
    else:
        print("The price is too high!")
else:
    print("\n========== GAME OVER ==========")
    print("The mystery animal was " + secret_item + ".")
    print("Good try! Play again soon!")


# ลองเล่นให้ครบหลายแบบ
# 1. ตอบ rabbit ถูกตั้งแต่ครั้งแรก
# 2. ตอบผิด 2 ครั้ง แล้วตอบ rabbit ในครั้งที่ 3
# 3. ตอบผิดครบทั้ง 3 ครั้ง
# 4. ทายสัตว์ถูก แต่ทายราคาต่ำหรือสูงกว่า 500


# === คำถามเช็กความเข้าใจ ===
# 1. ผู้เล่นมีโอกาสทายสัตว์ทั้งหมดกี่ครั้ง?
# 2. เพราะอะไรคำใบ้ครั้งที่ 2 จึงมีตัวเลือกให้?
# 3. โปรแกรมจะให้ทายราคาเมื่อใด?
# 4. ถ้าทายราคา 600 โปรแกรมจะบอกว่าสูงหรือต่ำเกินไป?
