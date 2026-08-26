"""บทที่ 6: Python Scope"""

score = 10  # Global scope

def show_score():
    message = "Inside function"  # Local scope
    print(message)
    print(score)

show_score()

# print(message)  # NameError เพราะ message เป็น Local

print("\n--- Your turn ---")
# TODO: สร้าง global variable game_name
# สร้าง function ที่มี local variable player_name และแสดงทั้งสองค่า

# คำถาม: Local และ Global variable มองเห็นได้จากบริเวณใด?

