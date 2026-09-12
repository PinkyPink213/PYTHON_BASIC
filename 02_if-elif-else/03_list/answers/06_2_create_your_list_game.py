"""ตัวอย่างเฉลยบทที่ 6.2: Space Rescue List Game"""

print("========================================")
print("          SPACE RESCUE MISSION")
print("========================================")
print("Your spaceship has crashed on a strange moon!")
print("Your backpack can hold only 3 items.")

available_items = ["helmet", "oxygen", "food", "tool", "map"]

print("\nAvailable items: " + str(available_items))
item_1 = input("Choose item 1: ").lower()
item_2 = input("Choose item 2: ").lower()
item_3 = input("Choose item 3: ").lower()

game_ready = False

if (
    item_1 not in available_items
    or item_2 not in available_items
    or item_3 not in available_items
):
    print("An item is incorrect. Check the list and run again.")
elif item_1 == item_2 or item_1 == item_3 or item_2 == item_3:
    print("Please choose 3 different items and run again.")
else:
    backpack = []
    backpack.append(item_1)
    backpack.append(item_2)
    backpack.append(item_3)
    game_ready = True
    print("Backpack: " + str(backpack))

if game_ready:
    print("\n--- METEOR STORM ---")
    if "helmet" in backpack:
        print("Your helmet protects you from flying rocks!")
    else:
        print("You hide behind the spaceship until the storm ends.")

    print("\n--- BROKEN SATELLITE ---")
    print("You find a communicator for calling the rescue team!")

    if len(backpack) < 3:
        take_item = input("Take the communicator? (yes/no): ").lower()
        if take_item == "yes":
            backpack.append("communicator")
    else:
        print("Your backpack is full: " + str(backpack))
        swap_item = input("Replace an item? (yes/no): ").lower()
        if swap_item == "yes":
            item_to_remove = input("Which item will you remove? ").lower()
            if item_to_remove in backpack:
                backpack.remove(item_to_remove)
                backpack.append("communicator")
            else:
                print("That item is not in your backpack.")

    print("\n--- ENERGY CAVE ---")
    take_crystal = input("Take the energy crystal? (yes/no): ").lower()

    if take_crystal == "yes":
        if len(backpack) < 3:
            backpack.append("crystal")
        else:
            print("Your backpack is full: " + str(backpack))
            replace_item = input("Replace an item? (yes/no): ").lower()
            if replace_item == "yes":
                item_to_remove = input("Which item will you remove? ").lower()
                if item_to_remove in backpack:
                    item_index = backpack.index(item_to_remove)
                    backpack[item_index] = "crystal"
                else:
                    print("That item is not in your backpack.")

    print("Final backpack: " + str(backpack))
    print("\n--- RESCUE TIME ---")

    if "communicator" in backpack and ("oxygen" in backpack or "crystal" in backpack):
        print("You call the rescue team and have enough energy!")
        print("*** THE SPACE RESCUE TEAM FINDS YOU! ***")
    elif "communicator" in backpack:
        print("You call for help, but your energy is very low.")
    elif "oxygen" in backpack or "crystal" in backpack:
        print("You can survive, but you cannot call the rescue team.")
    else:
        print("You cannot call for help. Try the mission again!")

