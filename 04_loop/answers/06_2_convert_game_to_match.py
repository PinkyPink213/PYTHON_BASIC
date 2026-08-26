"""เฉลยบทที่ 6.2: Mystery Animal Shop เวอร์ชัน match-case"""

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

    match item_guess:
        case "rabbit":
            item_correct = True
            print("*** Correct animal! ***")
        case "cat" | "dog":
            print("Oops! That is not the mystery animal.")
        case _:
            print("That animal is not in this shop.")

    attempts += 1

if item_correct:
    print("You found it in " + str(attempts) + " guess(es)!")
    print("\n--- BONUS ROUND: GUESS THE PRICE ---")
    price_guess = int(input("How many baht does the rabbit cost? "))

    match price_guess:
        case 500:
            print("*** PERFECT PRICE! YOU WIN! ***")
        case price if price < secret_price:
            print("The price is too low!")
        case _:
            print("The price is too high!")
else:
    print("\n========== GAME OVER ==========")
    print("The mystery animal was " + secret_item + ".")
    print("Good try! Play again soon!")

