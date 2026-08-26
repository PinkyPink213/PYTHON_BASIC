"""เฉลยบทที่ 5: ใช้ List ร่วมกับเงื่อนไข"""

inventory = ["key", "map", "torch"]

if "key" in inventory:
    print("You can open the door!")
else:
    print("The door is locked.")

if "potion" not in inventory:
    print("You should find a potion.")

if len(inventory) >= 5:
    print("Your backpack is full.")
elif len(inventory) >= 3:
    print("Your backpack has some space.")
else:
    print("Your backpack is almost empty.")

foods = ["rice", "egg", "banana"]
if "egg" in foods:
    print("We can cook fried rice!")
else:
    print("We need an egg.")

if "milk" not in foods:
    foods.append("milk")
print(foods)

backpack = ["map", "water", "rope", "torch"]
if len(backpack) >= 4:
    print("Backpack is full.")
elif len(backpack) >= 2:
    print("There is some space.")
else:
    print("Backpack is almost empty.")

if "water" in backpack and "rope" in backpack:
    print("You are ready for the island!")
else:
    print("You need more supplies.")
