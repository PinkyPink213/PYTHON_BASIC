"""บทที่ 2: Boolean — True และ False"""

# Boolean มีเพียง True (จริง) และ False (ไม่จริง)
# ตัว T และ F ต้องเป็นตัวพิมพ์ใหญ่

print("--- Example 1: Boolean values ---")
is_sunny = True
is_raining = False
print(is_sunny)
print(is_raining)


print("\n--- Example 2: A comparison makes a Boolean ---")
age = 10
is_old_enough = age >= 8
print(is_old_enough)


print("\n--- Example 3: Boolean in an if ---")
homework_done = True
if homework_done:
    print("The homework is finished!")
else:
    print("Finish the homework first.")


print("\n--- Your turn 1 ---")
light_is_on = True
# TODO 1: print ค่าของ light_is_on
pass


print("\n--- Your turn 2 ---")
door_is_open = False
# TODO 2: ถ้า door_is_open เป็น True ให้ print("The door is open.")
# ถ้าเป็น False ให้ print("The door is closed.")
pass


print("\n--- Your turn 3 ---")
has_ticket = True
# TODO 3: ใช้ if ตรวจ has_ticket
# ถ้าเป็น True ให้ print("You may enter!")
pass


# === คำถามเช็กความเข้าใจ ===
# 1. Boolean มีค่าอะไรได้บ้าง?
# 2. True และ False ต้องเริ่มด้วยตัวพิมพ์ใหญ่หรือไม่?
# 3. ถ้า is_sleeping = False โค้ด if is_sleeping: จะทำงานหรือถูกข้าม?
