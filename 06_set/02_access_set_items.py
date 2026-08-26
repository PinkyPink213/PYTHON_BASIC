"""บทที่ 2: Access Set Items — ตรวจและอ่านสมาชิก"""

# Set ไม่มี Index จึงเขียน animals[0] ไม่ได้
animals = {"cat", "dog", "rabbit"}

print("--- Example 1: in and not in ---")
print("cat" in animals)
print("tiger" not in animals)


print("\n--- Example 2: Use with if ---")
if "rabbit" in animals:
    print("Rabbit found!")


print("\n--- Example 3: Read with for ---")
for animal in animals:
    print(animal)


print("\n--- Typing Practice ---")
# tools = {"key", "map", "torch"}
# if "key" in tools:
#     print("You can open the door!")


print("\n--- Your turn 1 ---")
foods = {"rice", "egg", "banana"}
# TODO 1: ถ้า egg อยู่ใน foods ให้แสดง "We can cook!"
# TODO 2: ถ้า milk ไม่อยู่ใน foods ให้แสดง "We need milk."


print("\n--- Your turn 2 ---")
# TODO 3: ใช้ for แสดงอาหารทุกค่าใน foods


# === คำถามเช็กความเข้าใจ ===
# 1. เพราะอะไรจึงใช้ foods[0] ไม่ได้?
# 2. in ใช้ตรวจอะไร?
# 3. for แสดงสมาชิก Set ตามลำดับเดิมทุกครั้งหรือไม่?

