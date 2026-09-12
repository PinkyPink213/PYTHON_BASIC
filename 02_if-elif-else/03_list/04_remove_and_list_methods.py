"""บทที่ 4: ลบ ค้นหา นับ และเรียงข้อมูลใน List"""

print("--- Example 1: remove() removes by value ---")
pets = ["cat", "dog", "rabbit", "dog"]
pets.remove("dog")
print(pets)  # ลบ dog ตัวแรกที่พบ


print("\n--- Example 2: pop() removes by index ---")
removed_pet = pets.pop(1)
print("Removed: " + removed_pet)
print(pets)


print("\n--- Example 3: Useful methods ---")
scores = [30, 10, 20, 20]
print(scores.count(20))  # มีเลข 20 กี่ตัว
print(scores.index(20))  # เลข 20 ตัวแรกอยู่ Index ใด
scores.sort()
print(scores)


print("\n--- Your turn 1 ---")
shopping = ["milk", "bread", "eggs", "juice"]
# TODO 1: ใช้ remove() ลบ "bread"


print("\n--- Your turn 2 ---")
# TODO 2: ใช้ pop() ลบของชิ้นสุดท้าย


print("\n--- Your turn 3 ---")
numbers = [5, 2, 9, 2]
# TODO 3: แสดงจำนวนครั้งที่เลข 2 ปรากฏ จากนั้น sort() และ print(numbers)


print("\n--- Your turn 4: Save the popped item ---")
queue = ["Mali", "Nida", "Ton"]
# TODO 4: ใช้ pop(0) นำคนแรกออกและเก็บไว้ในตัวแปร first_person
# จากนั้น print(first_person) และ print(queue)


print("\n--- Your turn 5: Clear everything ---")
missions = ["find key", "open door", "get treasure"]
# TODO 5: ใช้ clear() ลบทุกภารกิจ แล้ว print(missions)


# === คำถามเช็กความเข้าใจ ===
# 1. remove() ลบด้วยค่า หรือ Index?
# 2. pop() ที่ไม่ใส่ Index จะลบข้อมูลใด?
# 3. sort() กับ reverse() ทำงานต่างกันอย่างไร?
