"""เฉลยบทที่ 3: while loop"""

print("--- Example 1: Countdown ---")
count = 3

while count > 0:
    print(count)
    count -= 1

print("Blast off!")


print("\n--- Example 2: Fill a backpack ---")
backpack = []

while len(backpack) < 3:
    item = input("Choose an item: ").lower()

    if item in backpack:
        print("You already have that item.")
    else:
        backpack.append(item)

print("Backpack is full: " + str(backpack))


print("\n--- Your turn 1: Answer ---")
number = 1

while number <= 5:
    print(number)
    number += 1


print("\n--- Your turn 2: Answer ---")
password = ""

while password != "python":
    password = input("Enter the password: ").lower()

    if password != "python":
        print("Wrong password. Try again.")

print("Welcome!")


print("\n--- Your turn 3: Answer ---")
water = 0

while water < 10:
    water += 2
    print("Water: " + str(water) + " litres")


print("\n--- Your turn 4: Answer ---")
menu = ["pizza", "rice", "salad"]
food = ""

while food not in menu:
    food = input("Choose pizza, rice, or salad: ").lower()

    if food not in menu:
        print("That food is not on the menu.")

print("You ordered " + food)


print("\n--- Your turn 5: Answer ---")
secret_number = 7
guess = 0
attempts = 0

while guess != secret_number and attempts < 3:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess != secret_number:
        print("Try again!")

if guess == secret_number:
    print("Correct! You win!")
else:
    print("No guesses left. The answer was 7.")
