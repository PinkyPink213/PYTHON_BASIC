"""บทที่ 7.1: เกมตัวอย่าง — Pet Rescue Center"""

# Dictionary เป็นฐานข้อมูลสัตว์ แต่ละตัวมีชนิด อายุ และสิ่งของที่ต้องใช้

print("==================================")
print("        PET RESCUE CENTER")
print("==================================")

pets = {
    "milo": {"animal": "cat", "age": 3, "needs": "milk"},
    "lucky": {"animal": "dog", "age": 5, "needs": "ball"},
    "snow": {"animal": "rabbit", "age": 2, "needs": "carrot"}
}

print("Animals waiting for help:")
for pet_name, information in pets.items():
    print("- " + pet_name + " the " + information["animal"])

choice = input("Choose a pet to help: ").lower()

if choice not in pets:
    print("That pet is not at the rescue center.")
else:
    chosen_pet = pets[choice]
    animal = chosen_pet["animal"]
    age = chosen_pet["age"]
    needed_item = chosen_pet["needs"]

    print(choice.title() + " is a " + str(age) + "-year-old " + animal + ".")
    item = input("What item will you give? ").lower()

    if item == needed_item:
        chosen_pet["status"] = "happy"
        print("*** RESCUE SUCCESS! " + choice.upper() + " IS HAPPY! ***")
    else:
        chosen_pet["status"] = "still waiting"
        print(choice.title() + " needs " + needed_item + ", not " + item + ".")

    print("Updated pet data: " + str(chosen_pet))

