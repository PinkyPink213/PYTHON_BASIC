"""บทที่ 2: Access Tuples — เข้าถึงข้อมูล"""

animals = ("cat", "dog", "rabbit", "panda")

print("--- Example 1: Positive index ---")
print(animals[0])
print(animals[2])


print("\n--- Example 2: Negative index ---")
print(animals[-1])
print(animals[-2])


print("\n--- Example 3: Slicing ---")
print(animals[1:3])
print(animals[:2])
print(animals[2:])


print("\n--- Example 4: in and not in ---")
print("panda" in animals)
print("tiger" not in animals)


print("\n--- Typing Practice ---")
# พิมพ์ Tuple ของหวาน 4 อย่าง แล้วลองแสดง:
# - ตัวแรกด้วย Index 0
# - ตัวสุดท้ายด้วย Index -1
# - สองตัวตรงกลางด้วย Slicing


print("\n--- Your turn 1 ---")
scores = (10, 20, 30, 40, 50)
# TODO 1: แสดง 10 ด้วย Index
# TODO 2: แสดง 50 ด้วย Negative Index
# TODO 3: ใช้ Slicing แสดง (20, 30, 40)


print("\n--- Your turn 2 ---")
# TODO 4: ถ้า 30 อยู่ใน scores ให้แสดง "Score found!"
# TODO 5: ถ้า 100 ไม่อยู่ใน scores ให้แสดง "Score not found."


# === คำถามเช็กความเข้าใจ ===
# 1. Index ของสมาชิกตัวแรกคือเท่าไร?
# 2. Index -1 หมายถึงสมาชิกใด?
# 3. Slicing เปลี่ยน Tuple เดิมหรือสร้างผลลัพธ์ใหม่?

