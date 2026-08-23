"""บทที่ 0: Comments and Quotes — คอมเมนต์และเครื่องหมายคำพูด"""

# ==================================================
# 1. Comment คืออะไร?
# ==================================================
# Comment คือข้อความอธิบายโค้ดสำหรับคนอ่าน
# Python จะไม่ทำคำสั่งที่อยู่หลังเครื่องหมาย #

# นี่คือ Comment ทั้งบรรทัด
print("This line works.")

print("This also works.")  # นี่คือ Comment ที่อยู่ท้ายบรรทัด

# print("This line will not run.")
# เมื่อนำ # ไว้หน้าโค้ด Python จะข้ามโค้ดบรรทัดนั้น


# ==================================================
# 2. Comment หลายบรรทัด
# ==================================================
# Python ใช้ # ที่ต้นของแต่ละบรรทัด
# วิธีนี้ชัดเจนว่าเป็น Comment จริง
# และเหมาะกับการเขียนคำอธิบายหลายบรรทัด


# ==================================================
# 3. Single quote และ Double quote
# ==================================================
# String หรือข้อความเขียนได้ทั้ง '...' และ "..."

print('Hello with single quotes!')
print("Hello with double quotes!")

# ควรเปิดและปิดด้วยเครื่องหมายชนิดเดียวกัน
# print("This is wrong!')  # เปิดและปิดไม่ตรงกัน จึงเกิด SyntaxError


# ==================================================
# 4. เลือก Quote ให้ข้อความอ่านง่าย
# ==================================================
# ถ้าข้อความมี ' อยู่ข้างใน ใช้ Double quote ครอบด้านนอกได้ง่าย
print("I'm learning Python.")

# ถ้าข้อความมี " อยู่ข้างใน ใช้ Single quote ครอบด้านนอกได้ง่าย
print('The robot says, "Hello!"')


# ==================================================
# 5. Escape character: \
# ==================================================
# ใช้ backslash \\ เมื่อต้องการใส่ Quote ชนิดเดียวกับที่ครอบ String
print("The robot says, \"Welcome!\"")
print('I\'m ready!')

# \\n ใช้ขึ้นบรรทัดใหม่ และ \\t ใช้เว้นระยะแบบ Tab
print("Name:\tMali\nScore:\t10")


# ==================================================
# 6. Triple quotes
# ==================================================
# Triple quotes สร้าง String ที่เขียนได้หลายบรรทัด
story = """A cat found a key.
The key opened a magic door.
The adventure began!"""
print(story)

# ข้อควรจำ:
# """ข้อความ""" และ '''ข้อความ''' เป็น String ไม่ใช่ Comment จริง
# เมื่อวางไว้บรรทัดแรกของไฟล์หรือฟังก์ชัน จะเรียกว่า docstring
# สำหรับ Comment ทั่วไป ให้ใช้ # จะชัดเจนที่สุด


print("\n--- Typing Practice: Type it yourself ---")
# พิมพ์ตามทีละบรรทัด อย่า Copy/Paste
# print("My name is Mali.")
# print('My favorite game is "Minecraft".')
# print("I\'m learning Python!")
# print("Line 1\nLine 2")
# จากนั้นเพิ่ม Comment อธิบายโค้ดของตัวเองอย่างน้อย 2 บรรทัด


print("\n--- Your turn 1: Add comments ---")
# TODO 1: เขียน Comment อธิบายว่าโปรแกรมนี้จะแสดงชื่อและอายุ
# จากนั้นใช้ print() แสดงชื่อและอายุคนละบรรทัด


print("\n--- Your turn 2: Choose the quotes ---")
# TODO 2: แสดงข้อความ: I'm a Python student.
# เลือก Single quote หรือ Double quote ให้เขียนง่ายที่สุด


print("\n--- Your turn 3: A robot speaks ---")
# TODO 3: แสดงข้อความ: The robot says, "Let's play!"
# เลือก Quote ด้านนอกและใช้ Escape character หากจำเป็น


print("\n--- Your turn 4: Multiline story ---")
# TODO 4: ใช้ Triple quotes สร้างตัวแปร story ที่มีเรื่องสั้น 3 บรรทัด
# จากนั้น print(story)


print("\n--- Your turn 5: Turn code off ---")
# TODO 5: เขียน print("Secret message")
# จากนั้นเติม # ด้านหน้าเพื่อไม่ให้ข้อความทำงาน


# === คำถามเช็กความเข้าใจ ===
# 1. Python ทำอะไรกับข้อความที่อยู่หลัง #?
# 2. Single quote และ Double quote ใช้สร้างข้อมูลชนิดใด?
# 3. เพราะอะไร "I'm ready" จึงเหมาะกับ Double quote ด้านนอก?
# 4. \\n และ \\t ทำหน้าที่อะไร?
# 5. Triple-quoted text เป็น Comment จริงหรือเป็น String?

