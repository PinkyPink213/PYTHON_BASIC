"""บทที่ 3: String Manipulation — เล่นกับข้อความ"""

print("--- Example 1: Join strings with + ---")
first_name = "Mali"
last_name = "Dee"
full_name = first_name + " " + last_name
print(full_name)


print("\n--- Example 2: Repeat text with * ---")
cheer = "Go! "
print(cheer * 3)


print("\n--- Example 3: Useful string methods ---")
message = "  Python Is Fun  "
print(message.lower())
print(message.upper())
print(message.strip())


print("\n--- Example 4: f-string ---")
name = "Ton"
age = 11
print(f"My name is {name}. I am {age} years old.")


print("\n--- Practice 1: Join strings ---")
# กำหนด hero_name เป็นชื่อฮีโร่ที่เด็กเลือกเอง
# กำหนด hero_power เป็นพลังที่เด็กเลือกเอง
# ใช้ + สร้างประโยคว่า ฮีโร่ใช้พลังอะไร


print("\n--- Practice 2: Repeat text ---")
# สร้างข้อความเชียร์สั้น ๆ แล้วใช้ * แสดงซ้ำ 3 ครั้ง


print("\n--- Practice 3: String methods ---")
# สร้างข้อความที่มีช่องว่างด้านหน้าและด้านหลัง
# ทดลองแสดงผลด้วย lower(), upper() และ strip() ทีละแบบ


print("\n--- Practice 4: f-string ---")
# ใช้ตัวแปร hero_name และ hero_power จาก Practice 1
# สร้าง Hero Card หนึ่งบรรทัดด้วย f-string


print("\n--- Your turn 1 ---")
animal = "panda"
food = "bamboo"
# TODO 1: ใช้ + แสดง "The panda eats bamboo."


print("\n--- Your turn 2 ---")
word = "Hooray! "
# TODO 2: ใช้ * แสดง word จำนวน 3 ครั้ง


print("\n--- Your turn 3 ---")
player = "Nida"
score = 20
# TODO 3: ใช้ f-string แสดง "Nida has 20 points."


# === คำถามเช็กความเข้าใจ ===
# 1. + ทำอะไรเมื่อใช้กับ String?
# 2. lower() และ upper() ต่างกันอย่างไร?
# 3. f-string ช่วยนำตัวแปรมาใส่ในข้อความอย่างไร?
