"""เฉลยบทที่ 4.2: Nested if — เกมล่าหีบสมบัติ"""

print("--- Treasure Cave Game ---")
has_key = True
door = "gold"

if has_key:
    if door == "gold":
        print("You found the treasure!")
    else:
        print("Oh no! A sleepy dragon!")
else:
    print("Find the key first!")

# === แนวคำตอบ ===
# 1. ไม่ตรวจ เพราะโปรแกรมไปที่ else ของ has_key ทันที
# 2. พบมังกรที่กำลังหลับ และแสดง "Oh no! A sleepy dragon!"
# 3. ตั้ง has_key = True และ door = "gold"
