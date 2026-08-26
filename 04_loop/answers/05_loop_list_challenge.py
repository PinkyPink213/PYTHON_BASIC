"""เฉลยบทที่ 5: ภารกิจ Loop กับ List"""

print("--- Example: Count stars ---")
stars = ["gold", "silver", "gold", "gold"]
gold_count = 0

for star in stars:
    if star == "gold":
        gold_count += 1

print("Gold stars: " + str(gold_count))


print("--- Challenge 1: Count treasure ---")
treasures = ["coin", "gem", "coin", "key", "coin"]
coin_count = 0

for treasure in treasures:
    if treasure == "coin":
        coin_count += 1

print("Coins: " + str(coin_count))


print("\n--- Challenge 2: Shopping total ---")
prices = [10, 25, 15]
total = 0

for price in prices:
    total += price

print("Total: " + str(total))


print("\n--- Challenge 3: Valid choice ---")
choices = ["forest", "cave", "beach"]
choice = ""

while choice not in choices:
    print("Choices: " + str(choices))
    choice = input("Where do you want to go? ").lower()

    if choice not in choices:
        print("That place is not available. Try again.")

print("You chose " + choice)
