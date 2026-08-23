"""เฉลยบทที่ 1: for loop"""

print("--- Example 1: Animals ---")
animals = ["cat", "dog", "rabbit"]

for animal in animals:
    print("I like " + animal + ".")


print("\n--- Example 2: Use if inside for ---")
scores = [80, 45, 72]

for score in scores:
    if score >= 50:
        print(str(score) + " passed!")
    else:
        print(str(score) + " needs more practice.")


print("\n--- Your turn 1: Answer ---")
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


print("\n--- Your turn 2: Answer ---")
items = ["key", "apple", "map", "water"]

for item in items:
    if item == "key":
        print("You found the key!")
    else:
        print("You found " + item)


print("\n--- Your turn 3: Answer ---")
pets = ["cat", "dog", "duck"]

for pet in pets:
    if pet == "cat":
        print("Meow!")
    elif pet == "dog":
        print("Woof!")
    else:
        print("Quack!")


print("\n--- Your turn 4: Answer ---")
class_scores = [75, 40, 90, 55, 30]
pass_count = 0

for score in class_scores:
    if score >= 50:
        pass_count += 1

print("Students who passed: " + str(pass_count))
