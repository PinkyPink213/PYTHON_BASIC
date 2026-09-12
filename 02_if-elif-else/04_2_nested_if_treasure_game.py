"""บทที่ 4.2: Nested if — เกมล่าหีบสมบัติ"""

# แผนที่เกม
#
# START
#   |
#   v
# has_key ?
#   |-- NO  --> "Find the key first!" --> END
#   |
#   +-- YES --> door == "gold" ?
#                 |-- NO  --> "Oh no! A sleepy dragon!" --> END
#                 +-- YES --> "You found the treasure!" ---> END

print("--- Treasure Cave Game ---")
has_key = True
door = "gold"

# TODO: สร้างเกมโดยใช้ nested if
# 1. if ด้านนอกตรวจว่า has_key เป็น True หรือไม่
# 2. ถ้ามีกุญแจ ใช้ if ด้านในตรวจว่า door == "gold" หรือไม่
# 3. แสดงข้อความตามแผนที่เกมด้านบน
pass

# ลองเล่นให้ครบ 3 ตอนจบ
# 1. has_key = False
# 2. has_key = True และ door = "gold"
# 3. has_key = True และ door = "red"


# === คำถามเช็กความเข้าใจ ===
# 1. ถ้าไม่มีกุญแจ โปรแกรมจะตรวจสีของประตูหรือไม่?
# 2. ถ้า has_key = True และ door = "red" จะพบอะไร?
# 3. ต้องตั้งค่าตัวแปรอย่างไรจึงจะพบสมบัติ?
