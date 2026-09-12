"""เฉลยบทที่ 2.1: ตรวจสอบข้อมูลใน List"""

print("--- Your turn 1: Answer ---")
backpack = ["map", "water", "rope"]

if "map" in backpack:
    print("You have a map.")


print("\n--- Your turn 2: Answer ---")
if "torch" not in backpack:
    print("You need a torch.")


print("\n--- Your turn 3: Answer ---")
foods = ["rice", "egg", "banana"]

if "egg" in foods:
    print("We can cook fried rice!")
else:
    print("We need an egg.")


print("\n--- Your turn 4: Answer ---")
choices = ["forest", "cave", "beach"]
answer = "castle"

if answer not in choices:
    print("That place is not available.")
else:
    print("You chose " + answer)


print("\n--- Your turn 5: Answer ---")
school_bag = ["book", "pencil"]

if "eraser" not in school_bag:
    school_bag.append("eraser")

print(school_bag)

