"""เฉลยบทที่ 5: match-case"""

print("--- Your turn 1: Answer ---")
day = "saturday"

match day:
    case "saturday" | "sunday":
        print("Weekend fun!")
    case "monday":
        print("Back to school.")
    case _:
        print("Normal school day.")


print("\n--- Your turn 2: Answer ---")
operator = input("Choose +, -, or *: ")
number_1 = 8
number_2 = 2

match operator:
    case "+":
        print(number_1 + number_2)
    case "-":
        print(number_1 - number_2)
    case "*":
        print(number_1 * number_2)
    case _:
        print("Unknown operator.")


print("\n--- Your turn 3: Answer ---")
animal = input("Choose cat, dog, or duck: ").lower()

match animal:
    case "cat":
        print("Meow!")
    case "dog":
        print("Woof!")
    case "duck":
        print("Quack!")
    case _:
        print("I do not know that sound.")


print("\n--- Your turn 4: Answer ---")
age = 10

match age:
    case value if value < 6:
        print("Free ticket")
    case value if value < 13:
        print("Child ticket")
    case _:
        print("Regular ticket")

