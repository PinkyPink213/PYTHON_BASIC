"""บทที่ 1: for loop — หยิบข้อมูลจาก List ทีละชิ้น"""

# for loop ช่วยทำคำสั่งเดิมกับข้อมูลทุกชิ้นใน List

print("--- Example 1: Animals ---")
animals = ["cat", "dog", "rabbit"]

for animal in animals:
    print("I like " + animal + ".")


print("\n--- Example 2: Use if inside for ---")
scores = [80, 45, 72]

for score in scores:
    if score >= 50:
        print(str(score) + " passed!")
    else:
        print(str(score) + " needs more practice.")


print("\n--- Your turn 1 ---")
fruits = ["apple", "banana", "orange"]
# TODO 1: ใช้ for แสดงผลไม้ทีละชิ้น


print("\n--- Your turn 2 ---")
items = ["key", "apple", "map", "water"]
# TODO 2: ใช้ for หยิบ item ทีละชิ้น
# ถ้า item == "key" ให้ print("You found the key!")
# นอกนั้นให้ print("You found " + item)


print("\n--- Your turn 3: Pet sounds ---")
pets = ["cat", "dog", "duck"]
# TODO 3: ใช้ for และ if, elif, else แสดงเสียงสัตว์
# cat  -> print("Meow!")
# dog  -> print("Woof!")
# อื่น ๆ -> print("Quack!")


print("\n--- Your turn 4: Count passing scores ---")
class_scores = [75, 40, 90, 55, 30]
pass_count = 0
# TODO 4: ใช้ for ตรวจคะแนนทุกค่า
# ถ้าคะแนนตั้งแต่ 50 ขึ้นไป ให้เพิ่ม pass_count ทีละ 1
# หลังจบ for ให้แสดงจำนวนนักเรียนที่สอบผ่าน


# === คำถามเช็กความเข้าใจ ===
# 1. animal มีค่าเหมือนเดิมทุกรอบหรือไม่?
# 2. for loop หยุดเมื่อใด?
# 3. เราสามารถใส่ if ไว้ข้างใน for ได้หรือไม่?
# 4. ถ้าต้องการนับสิ่งที่พบใน Loop ควรสร้างตัวแปรเริ่มต้นเป็นเท่าไร?
