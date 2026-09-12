"""บทที่ 4.1: Nested if — ด่านเครื่องเล่น"""

# Flowchart
#
# START
#   |
#   v
# height_cm >= 120 ?
#   |-- NO  --> "Try the smaller ride." --> END
#   |
#   +-- YES --> has_permission ?
#                 |-- NO  --> "Ask an adult first." --> END
#                 +-- YES --> "You may ride!" -------> END
#
# if ตัวแรกตรวจส่วนสูง
# if ที่อยู่ด้านในตรวจว่าผู้ใหญ่อนุญาตหรือไม่

print("--- The Roller Coaster ---")
height_cm = 130
has_permission = True

# TODO: สร้างด่านตรวจเครื่องเล่น 2 ด่าน
# 1. ถ้า height_cm ตั้งแต่ 120 ขึ้นไป ให้ตรวจ has_permission ต่อ
# 2. ถ้าได้รับอนุญาต ให้ print("You may ride!")
# 3. ถ้าไม่ได้รับอนุญาต ให้ print("Ask an adult first.")
# 4. ถ้าสูงไม่ถึง ให้ print("Try the smaller ride.")
pass

# ลองเปลี่ยนค่าเพื่อดูทุกคำตอบ


# === คำถามเช็กความเข้าใจ ===
# 1. โปรแกรมจะตรวจ has_permission เมื่อ height_cm น้อยกว่า 120 หรือไม่?
# 2. ถ้า height_cm = 130 และ has_permission = False จะพิมพ์อะไร?
# 3. ทำไม if ตัวที่สองจึงต้องเยื้องอยู่ใน if ตัวแรก?
