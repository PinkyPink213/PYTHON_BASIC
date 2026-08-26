"""บทที่ 2.1: ตรวจสอบข้อมูลใน List ด้วย in และ not in"""

# in และ not in ใช้ตอบคำถามว่า ข้อมูลอยู่ใน List หรือไม่
# ผลของการตรวจสอบจะเป็น Boolean: True หรือ False

print("--- Example 1: Use in ---")
fruits = ["apple", "banana", "orange"]

print("banana" in fruits)  # True เพราะมี banana
print("mango" in fruits)   # False เพราะไม่มี mango


print("\n--- Example 2: Use not in ---")
print("mango" not in fruits)   # True เพราะไม่มี mango
print("apple" not in fruits)   # False เพราะมี apple


print("\n--- Example 3: Use in with if ---")
if "banana" in fruits:
    print("Banana is in the basket!")


print("\n--- Example 4: Use not in with if ---")
if "mango" not in fruits:
    print("Mango is not in the basket.")


print("\n--- Example 5: Use if and else ---")
item = "apple"

if item in fruits:
    print(item + " is available.")
else:
    print(item + " is not available.")


print("\n--- Your turn 1: Find the map ---")
backpack = ["map", "water", "rope"]
# TODO 1: ใช้ in ตรวจว่า "map" อยู่ใน backpack หรือไม่
# ถ้ามี ให้ print("You have a map.")


print("\n--- Your turn 2: Find a missing torch ---")
# TODO 2: ใช้ not in ตรวจว่า "torch" ไม่อยู่ใน backpack หรือไม่
# ถ้าไม่มี ให้ print("You need a torch.")


print("\n--- Your turn 3: Check food ---")
foods = ["rice", "egg", "banana"]
# TODO 3: ใช้ if และ else ตรวจว่า "egg" อยู่ใน foods หรือไม่
# ถ้ามี ให้ print("We can cook fried rice!")
# ถ้าไม่มี ให้ print("We need an egg.")


print("\n--- Your turn 4: Check the player's answer ---")
choices = ["forest", "cave", "beach"]
answer = "castle"
# TODO 4: ถ้า answer ไม่อยู่ใน choices
# ให้ print("That place is not available.")
# ถ้า answer อยู่ใน choices
# ให้ print("You chose " + answer)


print("\n--- Your turn 5: Add only when missing ---")
school_bag = ["book", "pencil"]
# TODO 5: ถ้า "eraser" ยังไม่อยู่ใน school_bag
# ให้ใช้ append() เพิ่ม "eraser"
# จากนั้น print(school_bag)


# === จุดที่มักเขียนผิด ===
# อย่าเขียนแบบนี้:
# if "map" in backpack == True:
#
# เขียนแบบนี้สั้นและอ่านง่ายกว่า:
# if "map" in backpack:
#
# not in ต้องเขียนติดกันเป็นสองคำ:
# if "torch" not in backpack:


# === คำถามเช็กความเข้าใจ ===
# 1. in ให้ผล True เมื่อใด?
# 2. not in ให้ผล True เมื่อใด?
# 3. "map" in backpack แก้ไขข้อมูลใน backpack หรือแค่ตรวจสอบ?
# 4. เพราะอะไรจึงควรตรวจ not in ก่อน append() ของบางชิ้น?

