"""ตัวอย่างเฉลยบทที่ 7.2: Magic Door Coordinates"""

print("==================================")
print("       MAGIC DOOR MISSION")
print("==================================")

doors = (
    ("forest", "leaf", 3),
    ("ocean", "shell", 7),
    ("castle", "crown", 9)
)

door_names = ("forest", "ocean", "castle")

print("Available magic doors:")
for door in doors:
    place, symbol, number = door
    print("- " + place + " | symbol: " + symbol)

choice = input("Choose a door: ").lower()

if choice not in door_names:
    print("That magic door does not exist.")
else:
    door_index = door_names.index(choice)
    chosen_door = doors[door_index]
    place, correct_symbol, correct_number = chosen_door

    symbol_guess = input("Enter the magic symbol: ").lower()
    number_guess = int(input("Enter the magic number: "))

    if symbol_guess == correct_symbol and number_guess == correct_number:
        print("*** THE " + place.upper() + " DOOR OPENS! ***")
    elif symbol_guess == correct_symbol or number_guess == correct_number:
        print("One answer is correct. The door shakes but stays closed.")
    else:
        print("The magic door stays closed. Try again!")

