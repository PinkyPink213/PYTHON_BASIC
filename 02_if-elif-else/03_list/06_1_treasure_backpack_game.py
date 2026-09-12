"""บทที่ 6.1: เกมตัวอย่าง — เอาตัวรอดจากเกาะด้วย List"""

# ==================================================
# คำอธิบายเกม
# ==================================================
#
# เกิดพายุใหญ่และพัดเรามาติดอยู่บนเกาะร้าง!
# ก่อนออกสำรวจ เราพบของที่มีประโยชน์ 5 ชิ้น แต่กระเป๋าของเรา
# ใส่ของได้ไม่เกิน 3 ชิ้น จึงต้องเลือกของที่คิดว่าสำคัญที่สุด
#
# ระหว่างสำรวจเกาะ เราจะเจอสถานการณ์ต่าง ๆ เช่น
# - เจอหน้าผาที่อาจต้องใช้เชือก
# - เจอวิทยุสำหรับเรียกหน่วยกู้ภัย
# - เจอมะพร้าวที่ใช้เป็นอาหารและน้ำได้
#
# ถ้ากระเป๋ายังว่าง เราสามารถเพิ่มของใหม่ด้วย append()
# ถ้ากระเป๋าเต็ม เราต้องตัดสินใจว่าจะเก็บของเดิมไว้
# หรือนำของบางชิ้นออกเพื่อใส่ของใหม่แทน
#
# เป้าหมายของเกม:
# พยายามให้ตอนจบมีทั้ง "radio" และแหล่งน้ำ
# ซึ่งอาจเป็น "water" หรือ "coconut" เพื่อรอหน่วยกู้ภัยอย่างปลอดภัย
#
# ความรู้ที่ใช้ในเกม:
# - สร้าง List เพื่อใช้เป็นกระเป๋า
# - ใช้ len() ตรวจว่ากระเป๋าเต็มหรือยัง
# - ใช้ in และ not in ตรวจของในกระเป๋า
# - ใช้ append() เพิ่มของ
# - ใช้ remove() นำของออก
# - ใช้ index() และ backpack[index] เปลี่ยนของ
# - ใช้ if, elif, else, and, or และ Nested if ตัดสินใจ
#
# บทนี้ยังไม่ใช้ for หรือ while เพราะจะได้เรียนในบทถัดไป
# เวลาตอบคำถามในเกม ให้ใช้ตัวพิมพ์เล็ก

print("========================================")
print("       STRANDED ISLAND BACKPACK")
print("========================================")
print("A storm has left you stranded on an island!")
print("Your backpack can hold only 3 items.")

# ของที่เลือกได้ทั้งหมดเก็บอยู่ใน List
available_items = ["rope", "water", "fruit", "flashlight", "blanket"]

# ==================================================
# ด่านที่ 1: เลือกของ 3 ชิ้นใส่กระเป๋า
# ==================================================

print("\nAvailable items: " + str(available_items))

# ถามผู้เล่น 3 ครั้ง เพราะกระเป๋าใส่ของได้ 3 ชิ้น
# .lower() ช่วยเปลี่ยนคำตอบเป็นตัวพิมพ์เล็ก
item_1 = input("Choose item 1: ").lower()
item_2 = input("Choose item 2: ").lower()
item_3 = input("Choose item 3: ").lower()

# Boolean นี้ใช้บอกว่าสามารถเริ่มเกมได้หรือไม่
game_ready = False

# ตรวจว่าทุกคำตอบเป็นของที่อยู่ใน available_items
if (
    item_1 not in available_items
    or item_2 not in available_items
    or item_3 not in available_items
):
    print("An item is incorrect.")
    print("Please check available_items and run the game again.")

# ตรวจว่าผู้เล่นไม่ได้เลือกของชิ้นเดิมซ้ำกัน
elif item_1 == item_2 or item_1 == item_3 or item_2 == item_3:
    print("Please choose 3 different items and run the game again.")

else:
    # เมื่อคำตอบถูกและไม่ซ้ำ จึงเพิ่มของลงใน List
    backpack = []
    backpack.append(item_1)
    backpack.append(item_2)
    backpack.append(item_3)
    game_ready = True

    print("Your backpack is ready!")
    print("Backpack: " + str(backpack))

# ส่วนผจญภัยด้านล่างจะทำงานเมื่อเลือกของถูกต้องครบ 3 ชิ้นเท่านั้น
if game_ready:

    print("\nYou start exploring with: " + str(backpack))

    print("\n--- CLIFF PATH ---")
    print("A steep cliff blocks the path to higher ground.")

    if "rope" in backpack:
        print("You use the rope and climb the cliff safely!")
    else:
        print("You have no rope, so you take a long and tiring path.")

    print("\n--- ABANDONED CAMP ---")
    print("You find a rescue radio!")

    if len(backpack) < 3:
        take_radio = input("Take the radio? (yes/no): ").lower()
        if take_radio == "yes":
            backpack.append("radio")
    else:
        print("Your backpack is full: " + str(backpack))
        swap_radio = input("Replace an item with the radio? (yes/no): ").lower()
        if swap_radio == "yes":
            item_to_remove = input("Which item will you remove? ").lower()
            if item_to_remove in backpack:
                backpack.remove(item_to_remove)
                backpack.append("radio")
            else:
                print("That item is not in your backpack.")

    print("Backpack now: " + str(backpack))

    print("\n--- COCONUT TREE ---")
    take_coconut = input("Take the coconut? (yes/no): ").lower()

    if take_coconut == "yes":
        if len(backpack) < 3:
            backpack.append("coconut")
        else:
            print("Your backpack is full: " + str(backpack))
            replace_item = input("Replace an item? (yes/no): ").lower()
            if replace_item == "yes":
                item_to_remove = input("Which item will you remove? ").lower()
                if item_to_remove in backpack:
                    item_index = backpack.index(item_to_remove)
                    backpack[item_index] = "coconut"
                else:
                    print("That item is not in your backpack.")

    print("Final backpack: " + str(backpack))
    print("\n--- SUNSET ---")

    if "radio" in backpack and ("water" in backpack or "coconut" in backpack):
        print("You call for help and have enough water while waiting.")
        print("*** A RESCUE BOAT FINDS YOU! YOU WIN! ***")
    elif "radio" in backpack:
        print("You are rescued, but you are very thirsty.")
    elif "water" in backpack or "coconut" in backpack:
        print("You survive the night but cannot call for help.")
    else:
        print("You have no radio and no water. Try again!")


# === คำถามเช็กความเข้าใจ ===
# 1. game_ready เริ่มต้นเป็น True หรือ False?
# 2. game_ready จะเปลี่ยนเป็น True เมื่อใด?
# 3. เพราะอะไรส่วนผจญภัยจึงอยู่ข้างใน if game_ready?
# 4. remove() และ append() เปลี่ยนกระเป๋าตอนไหน?
# 5. ต้องมีของอะไรบ้างจึงจะได้ตอนจบที่ดีที่สุด?
