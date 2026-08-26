"""ตัวอย่างเฉลยบทที่ 6.3: Mystery Toy Shop"""

print("==================================")
print("       MYSTERY TOY SHOP")
print("==================================")

choices = ["robot", "ball", "kite"]
secret_item = "robot"
secret_price = 300
max_attempts = 3
hints = [
    "Hint 1: It can move.",
    "Hint 2: It is a toy that can beep.",
    "Hint 3: The word starts with R."
]

print("Choose from:")
for choice in choices:
    print("- " + choice)

attempts = 0
item_correct = False

while attempts < max_attempts and not item_correct:
    print("\n[ Guess " + str(attempts + 1) + " of " + str(max_attempts) + " ]")
    print(hints[attempts])
    item_guess = input("What is the mystery toy? ").lower()

    match item_guess:
        case "robot":
            item_correct = True
            print("*** Correct toy! ***")
        case "ball" | "kite":
            print("Oops! Try the next hint.")
        case _:
            print("That toy is not in this shop.")

    attempts += 1

if item_correct:
    print("\n--- BONUS ROUND: GUESS THE PRICE ---")
    price_guess = int(input("How many baht does it cost? "))

    match price_guess:
        case 300:
            print("*** PERFECT! YOU WIN! ***")
        case price if price < secret_price:
            print("The price is too low!")
        case _:
            print("The price is too high!")
else:
    print("\n========== GAME OVER ==========")
    print("The mystery toy was " + secret_item + ".")

