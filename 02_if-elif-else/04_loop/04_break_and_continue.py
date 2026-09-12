"""บทที่ 4: break และ continue"""

print("--- Example 1: break stops the loop ---")
while True:
    command = input("Type go or quit: ").lower()

    if command == "quit":
        print("Loop stopped!")
        break

    print("Keep going!")


print("\n--- Example 2: continue skips one round ---")
for number in range(1, 6):
    if number == 3:
        continue

    print(number)


print("\n--- Your turn 1 ---")
# TODO 1: สร้างโปรแกรมที่ทำงานซ้ำจนกว่าผู้เล่นจะพิมพ์ stop
# ทำตามขั้นตอนทีละข้อ:
# 1. เขียน while True: เพื่อเริ่ม Loop ที่ทำงานซ้ำไปเรื่อย ๆ
# 2. เยื้อง 4 ช่อง แล้วสร้างตัวแปร command
# 3. รับคำตอบด้วย input("Type play or stop: ").lower()
# 4. เขียน if command == "stop":
# 5. ข้างใน if ให้ print("Stopped!")
# 6. บรรทัดถัดไปเขียน break เพื่อออกจาก while ทันที
# 7. นอก if แต่ยังอยู่ใน while ให้ print("Playing...")
#
# ทดลองรัน:
# - พิมพ์ play -> แสดง Playing... แล้วถามใหม่
# - พิมพ์ stop -> แสดง Stopped! แล้วจบ Loop


print("\n--- Your turn 2 ---")
# TODO 2: แสดงเลข 1 ถึง 10 แต่ไม่แสดงเลข 5
# ทำตามขั้นตอนทีละข้อ:
# 1. เขียน for number in range(1, 11):
#    ต้องใช้ stop เป็น 11 เพราะ range() หยุดก่อนเลขสุดท้าย
# 2. ข้างใน for เขียน if number == 5:
# 3. ข้างใน if เขียน continue เพื่อข้ามรอบที่ number เป็น 5
# 4. นอก if แต่ยังอยู่ใน for ให้ print(number)
#
# ผลลัพธ์ที่ควรได้:
# 1, 2, 3, 4, 6, 7, 8, 9, 10 โดยแต่ละเลขอยู่คนละบรรทัด


print("\n--- Your turn 3: Find the key ---")
cave_items = ["rock", "coin", "key", "torch"]
# TODO 3: ค้นหากุญแจและหยุดค้นหาทันทีเมื่อพบ
# ทำตามขั้นตอนทีละข้อ:
# 1. เขียน for item in cave_items: เพื่อหยิบของทีละชิ้น
# 2. ข้างใน for ให้ print("Checking " + item)
# 3. เขียน if item == "key":
# 4. ข้างใน if ให้ print("Key found!")
# 5. บรรทัดถัดไปเขียน break เพื่อหยุด for ทันที
#
# ผลลัพธ์จะตรวจ rock, coin และ key
# โปรแกรมจะไม่ตรวจ torch เพราะ break หยุด Loop หลังพบ key แล้ว


print("\n--- Your turn 4: Skip empty answers ---")
answers = ["cat", "", "rabbit", "", "dog"]
# TODO 4: แสดงเฉพาะคำตอบที่มีข้อความ และข้ามข้อความว่าง
# ทำตามขั้นตอนทีละข้อ:
# 1. เขียน for answer in answers: เพื่อหยิบคำตอบทีละค่า
# 2. ข้างใน for เขียน if answer == "":
#    "" คือ string ว่าง หรือข้อความที่ไม่มีตัวอักษร
# 3. ข้างใน if เขียน continue เพื่อข้ามคำตอบว่าง
# 4. นอก if แต่ยังอยู่ใน for ให้ print(answer)
#
# ผลลัพธ์ที่ควรได้:
# cat
# rabbit
# dog
# continue ข้ามเพียงรอบปัจจุบัน จากนั้น for ยังทำรอบถัดไป


# === คำถามเช็กความเข้าใจ ===
# 1. break ทำอะไรกับ Loop?
# 2. continue หยุด Loop ทั้งหมดหรือไม่?
# 3. while True หยุดได้อย่างไรในตัวอย่างแรก?
# 4. คำสั่งหลัง break ในรอบนั้นจะทำงานต่อหรือไม่?
