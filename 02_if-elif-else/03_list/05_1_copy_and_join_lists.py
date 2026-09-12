"""บทที่ 5.1: คัดลอกและรวม List"""

print("--- Example 1: copy() makes a new list ---")
original_bag = ["map", "water"]
copied_bag = original_bag.copy()
copied_bag.append("rope")

print("Original: " + str(original_bag))
print("Copy: " + str(copied_bag))


print("\n--- Example 2: Join with + ---")
team_red = ["Mali", "Ton"]
team_blue = ["Nida", "Ploy"]
all_players = team_red + team_blue
print(all_players)


print("\n--- Your turn 1: Copy a wish list ---")
wish_list = ["book", "robot"]
# TODO 1: ใช้ copy() สร้าง List ใหม่ชื่อ birthday_list
# เพิ่ม "cake" ใน birthday_list แล้วแสดง List ทั้งสอง
# สังเกตว่า wish_list ต้องไม่มี cake


print("\n--- Your turn 2: Join two lists ---")
land_animals = ["cat", "dog"]
sea_animals = ["fish", "whale"]
# TODO 2: ใช้ + รวมสอง List เป็น all_animals แล้ว print(all_animals)


print("\n--- Your turn 3: Join with extend() ---")
morning_tasks = ["brush teeth", "eat breakfast"]
school_tasks = ["study", "read"]
# TODO 3: ใช้ extend() เพิ่ม school_tasks เข้า morning_tasks
# จากนั้น print(morning_tasks)


# === คำถามเช็กความเข้าใจ ===
# 1. เพราะอะไรจึงใช้ copy() เมื่อต้องการ List ใหม่ที่แก้แยกกันได้?
# 2. เครื่องหมาย + เปลี่ยน List เดิมหรือสร้าง List ใหม่?
# 3. extend() เพิ่มข้อมูลเข้า List ใด?

