"""เกมตัวอย่างและเฉลย: Escape from the Magic Castle"""

# ==================================================
# เกมนี้คือเกมอะไร?
# ==================================================
# ผู้เล่นตื่นขึ้นมาในปราสาทเวทมนตร์และต้องหนีออกจากปราสาท
# การจะหนีออกไปได้ ผู้เล่นต้องผ่านห้องทดสอบทั้งหมด 3 ห้อง
# แต่ละห้องให้ผู้เล่นตอบคำถามหรือตัดสินใจผ่าน input()
# คำตอบของผู้เล่นจะเปลี่ยนเส้นทาง คะแนน และตอนจบของเกม
#
# เป้าหมาย:
# ผ่านประตู ตอบปริศนาให้ถูก และหาทางข้ามสะพานเวทมนตร์


# ==================================================
# ห้องและสถานการณ์ในเกม
# ==================================================
# ROOM 1 — TWO DOORS
# ผู้เล่นเลือกประตูสีแดงหรือสีน้ำเงิน
# ประตูหนึ่งพาไปต่อ แต่อีกประตูมีมังกรรออยู่
#
# ROOM 2 — THE GUARDIAN
# ผู้เล่นต้องตอบปริศนาสัตว์เพื่อรับกุญแจสีเงิน
# ถ้าไม่ได้กุญแจ จะเปิดประตูไปห้องสุดท้ายไม่ได้
#
# ROOM 3 — THE MAGIC BRIDGE
# สะพานตรวจอายุและถามว่าผู้เล่นกลัวความสูงหรือไม่
# ผู้เล่นต้องผ่านหลายเงื่อนไขพร้อมกัน หรือพบทางออกอีกแบบ


# ==================================================
# Features ของเกม
# ==================================================
# - รับชื่อและคำตอบจากผู้เล่นด้วย input()
# - ใช้ .lower() ช่วยให้ตรวจคำตอบตัวพิมพ์เล็กได้ง่าย
# - มีระบบผ่านด่านด้วย game_continue
# - มีไอเทมสำคัญคือ silver key
# - มีระบบคะแนน: ผ่านแต่ละด่านได้รับ 10 คะแนน
# - เมื่อชนะ คะแนนจะคูณ bonus_multiplier
# - มีหลายตอนจบ: YOU WIN, TRY AGAIN และ GAME OVER
# - ด่านถัดไปจะไม่ทำงานถ้าผู้เล่นแพ้ด่านก่อนหน้า


# ==================================================
# ความรู้ Python ที่ใช้
# ==================================================
# จากบท Basic:
# - Comments, print(), Variables และกฎการตั้งชื่อ
# - String manipulation, input() และ f-string
# - Data Types: str, int, float และ bool
# - Casting ด้วย int() และ str()
# - Mathematical operations ด้วย +, += และ *
#
# จากบท if-elif-else:
# - เครื่องหมายเปรียบเทียบ
# - Boolean: True และ False
# - if, elif และ else
# - and, or และ not
# - Nested if


# ==================================================
# Flow ของเกม
# ==================================================
# START
#   |
#   v
# ROOM 1: เลือกประตู
#   |-- ผิด --> GAME OVER
#   +-- ถูก --> รับ 10 คะแนน
#                  |
#                  v
# ROOM 2: ตอบปริศนา
#   |-- ผิด --> ไม่ได้กุญแจ --> GAME OVER
#   +-- ถูก --> ได้กุญแจและรับ 10 คะแนน
#                  |
#                  v
# ROOM 3: ตรวจอายุและความกลัว
#   |-- ไม่ผ่าน --> TRY AGAIN
#   +-- ผ่าน --> รับคะแนนและโบนัส --> YOU WIN

print("========================================")
print("       ESCAPE FROM THE MAGIC CASTLE")
print("========================================")
print("Pass all 3 rooms to escape!")

player_name = input("What is your name? ")
print("Good luck, " + player_name + "!")

# str, int, float และ bool เป็น Data Types จากบท Basic
game_continue = True
score = 0
bonus_multiplier = 1.5

print("\n--- ROOM 1: TWO DOORS ---")
door = input("Choose the red or blue door: ").lower()

if door == "blue":
    print("The blue door opens!")
    score += 10
elif door == "red":
    print("A sleepy dragon is behind the door!")
    game_continue = False
else:
    print("That door does not exist!")
    game_continue = False

if game_continue:
    print("\n--- ROOM 2: THE GUARDIAN ---")
    print("I am small, furry, and I say meow.")
    animal = input("Am I a cat, dog, or rabbit? ").lower()

    if animal == "cat":
        print("Correct! You receive a silver key.")
        has_key = True
    elif animal == "dog" or animal == "rabbit":
        print("That animal lives here, but it is not me.")
        has_key = False
    else:
        print("That is not one of the choices.")
        has_key = False

    if has_key:
        print("The key opens Room 3!")
        score += 10
    else:
        print("You cannot continue without the key.")
        game_continue = False

if game_continue:
    print("\n--- ROOM 3: THE MAGIC BRIDGE ---")
    age = int(input("How old are you? "))
    afraid_answer = input("Are you afraid of heights? (yes/no): ").lower()

    is_old_enough = age >= 8
    is_not_too_old = age < 16
    is_afraid = afraid_answer == "yes"

    if is_old_enough and is_not_too_old and not is_afraid:
        print("You cross the magic bridge!")
        escaped = True
        score += 10
    elif not is_old_enough:
        print("Return when you are older.")
        escaped = False
    elif not is_not_too_old:
        print("A secret adult exit opens!")
        escaped = True
    else:
        print("You are too afraid to cross today.")
        escaped = False

    if escaped:
        # Mathematical operation: คูณคะแนนด้วยโบนัส
        final_score = score * bonus_multiplier
        print("***************************************")
        print("  YOU ESCAPED THE MAGIC CASTLE!")
        # f-string นำ String และตัวเลขมาแสดงในข้อความเดียวกัน
        print(f"  Player: {player_name}")
        print(f"  Final score: {final_score}")
        print("***************************************")
    else:
        print("========== TRY AGAIN ==========")
        # str() คือ Casting ตัวเลขเป็นข้อความก่อนใช้ +
        print("Your score is " + str(score) + ".")
else:
    print("========== GAME OVER ==========")
    print("Try again and choose a different answer!")
    print("Your score is " + str(score) + ".")
