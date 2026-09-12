"""ตัวอย่างเฉลยบทที่ 6.2 — เด็กสามารถสร้างคำตอบที่ต่างกันได้"""

print("==================================")
print("     MY ROBOT GUESSING GAME")
print("==================================")
print("  [o_o]")
print(" /|___|\\")
print("  /   \\")
print("You have 3 guesses!")

# ตัวอย่างนี้เลือกเพียงหมวด toy
category = "toy"
secret_item = "robot"
secret_price = 300

hint_1 = "Hint 1: It can walk and beep."
hint_2 = "Hint 2: Choose from robot, ball, or kite."
hint_3 = "Hint 3: The word starts with R."

print("Category: " + category)

item_correct = False

print("\n[ Guess 1 of 3 ]")
print(hint_1)
item_guess = input("What is the mystery item? (use lowercase): ")

if item_guess == secret_item:
    item_correct = True
    print("*** Correct item! ***")
else:
    print("Oops! That is not the item.")
    print("\n[ Guess 2 of 3 ]")
    print(hint_2)
    item_guess = input("What is the mystery item? (use lowercase): ")

    if item_guess == secret_item:
        item_correct = True
        print("*** Correct item! ***")
    else:
        print("Oops! That is not the item.")
        print("\n[ Final Guess ]")
        print(hint_3)
        item_guess = input("What is the mystery item? (use lowercase): ")

        if item_guess == secret_item:
            item_correct = True
            print("*** Correct item! ***")
        else:
            print("Oops! That is not the item.")

if item_correct:
    print("\n--- BONUS ROUND: GUESS THE PRICE ---")
    price_guess = int(input("How many baht does it cost? "))

    if price_guess == secret_price:
        print("**********************************")
        print("       PERFECT! YOU WIN!")
        print("**********************************")
    elif price_guess < secret_price:
        print("The price is too low!")
    else:
        print("The price is too high!")
else:
    print("\n========== GAME OVER ==========")
    print("The mystery item was " + secret_item + ".")
    print("Good try! Play again soon!")


# นี่เป็นเพียงตัวอย่าง เด็กเลือกหมวด ของลับ ราคา และคำใบ้เองได้
