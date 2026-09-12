"""บทที่ 3: ตัวเชื่อมเงื่อนไข — and, or, not"""


# ==================================================
# 1. and — ทุกเงื่อนไขต้องเป็น True
# ==================================================

print("--- AND: Example ---")
is_weekend = True
homework_done = True

# ตัวอย่าง: เล่นได้เมื่อเป็นวันหยุด และ ทำการบ้านเสร็จ
if is_weekend and homework_done:
    print("Time to play!")


print("\n--- AND: Your turn 1 ---")
age = 10
has_ticket = True

# TODO 1: ถ้า age >= 8 และ has_ticket เป็น True
# ให้ print("You may enter the show!")
# คำใบ้: เชื่อมสองเงื่อนไขด้วย and
pass


print("\n--- AND: Your turn 2 ---")
has_flour = True
has_eggs = True

# TODO 2: ถ้ามีแป้ง และ มีไข่
# ให้ print("We can bake a cake!")
# ลองเปลี่ยน has_eggs เป็น False แล้วรันใหม่
pass


# ==================================================
# 2. or — อย่างน้อยหนึ่งเงื่อนไขต้องเป็น True
# ==================================================

print("\n--- OR: Example ---")
is_raining = False
is_snowing = True

# ตัวอย่าง: ถ้าฝนตก หรือ หิมะตก ให้ใส่รองเท้าบูต
if is_raining or is_snowing:
    print("Wear your boots!")


print("\n--- OR: Your turn 1 ---")
fruit = "apple"

# TODO 3: ถ้า fruit เท่ากับ "apple" หรือ "banana"
# ให้ print("This fruit is yellow or red!")
# คำใบ้: เขียนการเปรียบเทียบทั้งสองข้างของ or
pass


print("\n--- OR: Your turn 2 ---")
is_saturday = False
is_sunday = True

# TODO 4: ถ้าเป็นวันเสาร์ หรือ วันอาทิตย์
# ให้ print("It is the weekend!")
pass


# ==================================================
# 3. not — กลับค่าความจริง
# ==================================================

print("\n--- NOT: Example ---")
room_is_messy = False

# not False จะกลายเป็น True
if not room_is_messy:
    print("Your room is very clean!")


print("\n--- NOT: Your turn 1 ---")
is_sleeping = False

# TODO 5: ถ้าเด็ก ไม่ได้ กำลังนอน
# ให้ print("The child is awake!")
# คำใบ้: ใช้ not หน้าชื่อตัวแปร
pass


print("\n--- NOT: Your turn 2 ---")
door_is_locked = False

# TODO 6: ถ้าประตู ไม่ได้ ล็อก
# ให้ print("The door can be opened!")
pass


# === คำถามเช็กความเข้าใจ ===
# 1. and ต้องการให้ทุกเงื่อนไขเป็น True หรือเพียงหนึ่งเงื่อนไข?
# 2. False or True ให้ผลเป็นอะไร?
# 3. not True ให้ผลเป็นอะไร?
