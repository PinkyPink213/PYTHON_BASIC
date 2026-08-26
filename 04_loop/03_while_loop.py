"""บทที่ 3: while loop — ทำซ้ำตราบใดที่เงื่อนไขยังจริง"""

print("--- Example 1: Countdown ---")
count = 3

while count > 0:
    print(count)
    count -= 1

print("Blast off!")


print("\n--- Example 2: Fill a backpack ---")
backpack = []

while len(backpack) < 3:
    item = input("Choose an item: ").lower()

    if item in backpack:
        print("You already have that item.")
    else:
        backpack.append(item)

print("Backpack is full: " + str(backpack))


print("\n--- Your turn 1 ---")
number = 1
# TODO 1: ใช้ while แสดงเลข 1 ถึง 5
# อย่าลืมเพิ่มค่า number ในแต่ละรอบ


print("\n--- Your turn 2 ---")
password = ""
# TODO 2: ถาม password ซ้ำจนกว่าผู้ใช้จะพิมพ์ "python"
# เมื่อถูกแล้ว print("Welcome!")


print("\n--- Your turn 3: Fill the water tank ---")
water = 0
# TODO 3: ใช้ while เติมน้ำครั้งละ 2 ลิตร จนมีน้ำ 10 ลิตร
# ในแต่ละรอบให้ print("Water: " + str(water) + " litres")


print("\n--- Your turn 4: Valid menu choice ---")
menu = ["pizza", "rice", "salad"]
food = ""
# TODO 4: ถามผู้ใช้ซ้ำจนกว่าจะพิมพ์อาหารที่อยู่ใน menu
# ถ้าพิมพ์ผิดให้ print("That food is not on the menu.")
# เมื่อเลือกถูกให้ print("You ordered " + food)


print("\n--- Your turn 5: Three chances ---")
secret_number = 7
guess = 0
attempts = 0
# TODO 5: ให้ผู้เล่นทายเลข ขณะที่ยังทายไม่ถูกและ attempts < 3
# ใช้ int(input()) รับคำตอบ และเพิ่ม attempts ทุกครั้ง
# หลังจบ while ใช้ if บอกว่าชนะหรือใช้โอกาสหมด


# === คำถามเช็กความเข้าใจ ===
# 1. while loop ทำงานต่อเมื่อเงื่อนไขเป็น True หรือ False?
# 2. เพราะอะไร count -= 1 จึงสำคัญ?
# 3. จะเกิดอะไรขึ้นถ้าเงื่อนไขของ while เป็น True ตลอดเวลา?
# 4. while สามารถตรวจสองเงื่อนไขพร้อมกันด้วย and ได้หรือไม่?
