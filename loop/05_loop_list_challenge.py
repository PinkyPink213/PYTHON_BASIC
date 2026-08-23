"""บทที่ 5: ภารกิจ Loop กับ List"""


print("--- Example: Count stars ---")
stars = ["gold", "silver", "gold", "gold"]
gold_count = 0

for star in stars:
    if star == "gold":
        gold_count += 1

print("Gold stars: " + str(gold_count))


print("--- Challenge 1: Count treasure ---")
treasures = ["coin", "gem", "coin", "key", "coin"]
coin_count = 0

# TODO 1: ใช้ for ตรวจ treasure ทุกชิ้น
# ถ้า treasure == "coin" ให้เพิ่ม coin_count ทีละ 1
# หลังจบ Loop ให้ print จำนวนเหรียญ


print("\n--- Challenge 2: Shopping total ---")
prices = [10, 25, 15]
total = 0

# TODO 2: ใช้ for บวกราคาทุกค่าลงใน total แล้ว print(total)


print("\n--- Challenge 3: Valid choice ---")
choices = ["forest", "cave", "beach"]
choice = ""

# TODO 3: ใช้ while ถามซ้ำจนกว่า choice จะอยู่ใน choices
# ถ้าพิมพ์ผิด ให้แสดงตัวเลือกอีกครั้ง
# เมื่อถูกแล้ว print("You chose " + choice)


# === คำถามเช็กความเข้าใจ ===
# 1. ทำไม coin_count ต้องเริ่มจาก 0?
# 2. ตัวแปร total เปลี่ยนค่าอย่างไรในแต่ละรอบ?
# 3. เงื่อนไข while ของ Challenge 3 ควรใช้ in หรือ not in?
