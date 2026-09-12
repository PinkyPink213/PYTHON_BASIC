"""บทที่ 3: Update Tuples — แก้ไขผ่าน List"""

# Tuple เปลี่ยนสมาชิกโดยตรงไม่ได้
colors = ("red", "green", "blue")

# colors[1] = "yellow"  # TypeError

print("--- Example 1: Change an item ---")
color_list = list(colors)
color_list[1] = "yellow"
colors = tuple(color_list)
print(colors)


print("\n--- Example 2: Add an item ---")
color_list = list(colors)
color_list.append("purple")
colors = tuple(color_list)
print(colors)


print("\n--- Example 3: Remove an item ---")
color_list = list(colors)
color_list.remove("red")
colors = tuple(color_list)
print(colors)


print("\n--- Typing Practice ---")
# พิมพ์ตามกระบวนการ 3 ขั้น:
# 1. แปลง Tuple เป็น List
# 2. แก้ไข List
# 3. แปลง List กลับเป็น Tuple


print("\n--- Your turn 1 ---")
tools = ("hammer", "rope", "map")
# TODO 1: แปลง tools เป็น List เปลี่ยน "rope" เป็น "torch"
# แล้วแปลงกลับเป็น Tuple และ print(tools)


print("\n--- Your turn 2 ---")
# TODO 2: เพิ่ม "key" ลงใน tools โดยแปลงผ่าน List


print("\n--- Your turn 3 ---")
# TODO 3: ลบ "map" ออกจาก tools โดยแปลงผ่าน List


# === คำถามเช็กความเข้าใจ ===
# 1. เพราะอะไรจึงเขียน colors[0] = "pink" ไม่ได้?
# 2. ต้องแปลง Tuple เป็นข้อมูลชนิดใดก่อนแก้ไข?
# 3. หลังแก้เสร็จควรแปลงกลับด้วยฟังก์ชันใด?

