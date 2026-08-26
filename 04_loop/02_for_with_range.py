"""บทที่ 2: for loop กับ range()"""

print("--- Example 1: Count from 0 ---")
for number in range(5):
    print(number)


print("\n--- Example 2: Choose start and stop ---")
# หยุดก่อน 6 จึงได้เลข 1 ถึง 5
for number in range(1, 6):
    print(number)


print("\n--- Example 3: Count by 2 ---")
for number in range(2, 11, 2):
    print(number)


print("\n--- Example 4: Repeat a message ---")
for round_number in range(1, 4):
    print("Round " + str(round_number) + ": Go!")


print("\n--- Your turn 1 ---")
# TODO 1: ใช้ range() แสดงเลข 1 ถึง 10


print("\n--- Your turn 2 ---")
# TODO 2: ใช้ range() แสดงเลข 5, 10, 15 และ 20


print("\n--- Your turn 3 ---")
# TODO 3: แสดง "Jump!" จำนวน 3 ครั้ง


print("\n--- Your turn 4: Countdown ---")
# TODO 4: ใช้ range() แสดงเลข 5, 4, 3, 2, 1
# คำใบ้: step สามารถเป็น -1 ได้
# หลังจบ for ให้ print("Blast off!")


print("\n--- Your turn 5: Multiplication table ---")
# TODO 5: ใช้ for และ range() สร้างแม่ 3 ตั้งแต่ 3 x 1 ถึง 3 x 5
# ตัวอย่างบรรทัดแรก: print("3 x 1 = " + str(3 * 1))


print("\n--- Your turn 6: Even or odd ---")
# TODO 6: ใช้ for ตรวจเลข 1 ถึง 6
# ถ้าหาร 2 ลงตัว ให้ print ว่าเป็น even
# ถ้าหารไม่ลงตัว ให้ print ว่าเป็น odd
# คำใบ้: number % 2 == 0


# === คำถามเช็กความเข้าใจ ===
# 1. range(5) เริ่มจากเลขอะไร?
# 2. range(1, 6) มีเลข 6 หรือไม่?
# 3. ตัวเลขตัวที่สามใน range(start, stop, step) ทำหน้าที่อะไร?
# 4. ถ้าต้องการนับถอยหลัง ควรใช้ step เป็นบวกหรือลบ?
