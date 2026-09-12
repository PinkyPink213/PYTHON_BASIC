"""เฉลยบทที่ 3: Logical operators — and, or, not"""


print("--- AND: Example ---")
is_weekend = True
homework_done = True
if is_weekend and homework_done:
    print("Time to play!")

print("\n--- AND: Your turn 1 ---")
age = 10
has_ticket = True
if age >= 8 and has_ticket:
    print("You may enter the show!")

print("\n--- AND: Your turn 2 ---")
has_flour = True
has_eggs = True
if has_flour and has_eggs:
    print("We can bake a cake!")


print("\n--- OR: Example ---")
is_raining = False
is_snowing = True
if is_raining or is_snowing:
    print("Wear your boots!")

print("\n--- OR: Your turn 1 ---")
fruit = "apple"
if fruit == "apple" or fruit == "banana":
    print("This fruit is yellow or red!")

print("\n--- OR: Your turn 2 ---")
is_saturday = False
is_sunday = True
if is_saturday or is_sunday:
    print("It is the weekend!")


print("\n--- NOT: Example ---")
room_is_messy = False
if not room_is_messy:
    print("Your room is very clean!")

print("\n--- NOT: Your turn 1 ---")
is_sleeping = False
if not is_sleeping:
    print("The child is awake!")

print("\n--- NOT: Your turn 2 ---")
door_is_locked = False
if not door_is_locked:
    print("The door can be opened!")


# === แนวคำตอบ ===
# 1. and ต้องการให้ทุกเงื่อนไขเป็น True
# 2. True เพราะ or ต้องการเพียงหนึ่งเงื่อนไขที่เป็น True
# 3. False เพราะ not กลับค่าความจริง
