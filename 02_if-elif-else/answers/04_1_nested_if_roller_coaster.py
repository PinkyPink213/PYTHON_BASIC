"""เฉลยบทที่ 4.1: Nested if — ด่านเครื่องเล่น"""

print("--- The Roller Coaster ---")
height_cm = 130
has_permission = True

if height_cm >= 120:
    if has_permission:
        print("You may ride!")
    else:
        print("Ask an adult first.")
else:
    print("Try the smaller ride.")

# === แนวคำตอบ ===
# 1. ไม่ตรวจ เพราะโปรแกรมไปที่ else ของด่านส่วนสูงทันที
# 2. "Ask an adult first."
# 3. เพราะต้องตรวจการอนุญาตเมื่อผ่านด่านส่วนสูงแล้วเท่านั้น
