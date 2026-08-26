"""บทที่ 5: Variable Naming Rules — ตั้งชื่อตัวแปร"""

# กฎสำคัญ:
# - ใช้ตัวอักษร ตัวเลข และ _ ได้
# - ห้ามขึ้นต้นด้วยตัวเลข
# - ห้ามมีช่องว่างหรือเครื่องหมาย -
# - ห้ามใช้คำสงวน เช่น if, for, True
# - Python แยกตัวพิมพ์เล็กและใหญ่
# - ควรตั้งชื่อให้อ่านแล้วรู้ว่าเก็บอะไร

print("--- Example 1: Good names ---")
player_name = "Mali"
score_1 = 10
favorite_food = "pizza"
print(player_name, score_1, favorite_food)


print("\n--- Example 2: Uppercase and lowercase differ ---")
age = 10
Age = 20
print(age)
print(Age)


# ตัวอย่างชื่อที่ผิด จึงเขียนเป็นคอมเมนต์ไว้
# 2players = 5       # ขึ้นต้นด้วยตัวเลข
# player name = "A" # มีช่องว่าง
# player-score = 10 # มีเครื่องหมาย -
# if = "yes"        # if เป็นคำสงวน


print("\n--- Typing Practice: Fix the names ---")
# ชื่อตัวแปรด้านล่างผิดกฎ ให้เขียนใหม่เป็นชื่อที่ถูกต้อง
# เด็กเป็นคนคิดชื่อใหม่เอง แล้วกำหนดค่าและแสดงค่าทุกตัว
#
# player name
# 2nd_level
# pet-color


print("\n--- Your turn 1 ---")
# TODO 1: แก้ชื่อ 3 ตัวนี้ให้ถูก แล้วนำ # ด้านหน้าออก
# student name = "Mali"
# 1st_score = 20
# favorite-color = "green"


print("\n--- Your turn 2 ---")
# TODO 2: สร้างตัวแปรชื่อที่สื่อความหมายสำหรับเก็บชื่อเกมและจำนวนหัวใจ


# === คำถามเช็กความเข้าใจ ===
# 1. ชื่อตัวแปรขึ้นต้นด้วยตัวเลขได้หรือไม่?
# 2. snake_case คือการใช้เครื่องหมายใดแทนช่องว่าง?
# 3. score และ Score เป็นตัวแปรเดียวกันหรือไม่?
