"""เฉลยบทที่ 4: break และ continue"""

print("--- Example 1: break stops the loop ---")
while True:
    command = input("Type go or quit: ").lower()

    if command == "quit":
        print("Loop stopped!")
        break

    print("Keep going!")


print("\n--- Example 2: continue skips one round ---")
for number in range(1, 6):
    if number == 3:
        continue

    print(number)


print("\n--- Your turn 1: Answer ---")
while True:
    command = input("Type play or stop: ").lower()

    if command == "stop":
        print("Stopped!")
        break

    print("Playing...")


print("\n--- Your turn 2: Answer ---")
for number in range(1, 11):
    if number == 5:
        continue

    print(number)


print("\n--- Your turn 3: Answer ---")
cave_items = ["rock", "coin", "key", "torch"]

for item in cave_items:
    print("Checking " + item)

    if item == "key":
        print("Key found!")
        break


print("\n--- Your turn 4: Answer ---")
answers = ["cat", "", "rabbit", "", "dog"]

for answer in answers:
    if answer == "":
        continue

    print(answer)
