"""บทที่ 6: Dictionary Methods and Exercises"""

print("--- Example: Useful methods ---")
player = {"name": "Mali", "score": 20}
print(player.keys())
print(player.values())
print(player.items())
print(player.get("level", "Not found"))


print("\n--- Exercise 1: Inventory ---")
inventory = {"potion": 3, "key": 1, "coin": 10}
# TODO 1: เพิ่ม potion อีก 2 ขวด
# TODO 2: เพิ่ม torch จำนวน 1
# TODO 3: ลบ key ด้วย pop()


print("\n--- Exercise 2: Student report ---")
student = {"name": "Nida", "math": 80, "science": 90}
# TODO 4: คำนวณค่าเฉลี่ย math และ science
# TODO 5: เพิ่ม average ลงใน student แล้ว print()


print("\n--- Exercise 3: Safe get() ---")
# TODO 6: ใช้ get() อ่าน key "english" ถ้าไม่มีให้แสดง "No score"


# === คำถามเช็กความเข้าใจ ===
# 1. get() ช่วยป้องกันปัญหาเมื่อไม่มี Key อย่างไร?
# 2. keys(), values() และ items() ต่างกันอย่างไร?
# 3. Dictionary เหมาะกับข้อมูลที่มีชื่อกำกับอย่างไร?

