"""เกมตัวอย่างสมบูรณ์: Choose Your Category Hangman"""

# ==================================================
# เกมนี้คืออะไร?
# ==================================================
# Animal Hangman คือเกมทายชื่อสัตว์จากคำใบ้
# ตัวอักษรของคำลับจะถูกซ่อนด้วย _ และผู้เล่นทายได้ครั้งละ 1 ตัวอักษร
# ทายถูกจะเปิดตัวอักษรทุกตำแหน่งที่พบ แต่ทายผิดจะเสียหัวใจ 1 ดวง
# ผู้เล่นชนะเมื่อเปิดคำครบก่อนภาพ Hangman สมบูรณ์

# เป้าหมาย:
# ใช้คำใบ้ช่วยทายชื่อสัตว์ โดยทายผิดได้ไม่เกิน 4 ครั้ง


# ==================================================
# Features ของเกม
# ==================================================
# - ให้ผู้เล่นเลือก Category แล้วสุ่มคำพร้อมคำใบ้จากหมวดนั้น
# - แสดงคำลับด้วย _ และเปิดเฉพาะตัวอักษรที่ทายถูก
# - เก็บตัวอักษรที่เคยทาย เพื่อป้องกันการทายซ้ำ
# - ตรวจว่าผู้เล่นพิมพ์ตัวอักษรเพียง 1 ตัว
# - มีหัวใจและ ASCII Art ที่เปลี่ยนเมื่อทายผิด
# - มีหน้าจอชนะและ GAME OVER


# ==================================================
# Flow ของเกม
# ==================================================
# START -> เลือก Category -> สุ่มคำและคำใบ้
#   |
#   v
# แสดงรูป, คำใบ้, คำที่ซ่อน, ตัวอักษรที่เคยทาย และหัวใจ
#   |
#   v
# รับตัวอักษร 1 ตัว
#   |-- Input ผิด ------> แจ้งเตือน แล้วถามใหม่
#   |-- เคยทายแล้ว ----> แจ้งเตือน แล้วถามใหม่
#   |-- อยู่ในคำ ------> เปิดตัวอักษร
#   +-- ไม่อยู่ในคำ ---> เพิ่ม mistakes
#   |
#   v
# เปิดครบ? -> WIN | mistakes ครบ? -> GAME OVER | ยังไม่จบ -> รอบใหม่


# ==================================================
# ความรู้จาก 8 Chapters ที่ใช้
# ==================================================
# Basic: Variables, Strings, Input และ String Methods
# If-Elif-Else: ตรวจ Input, คำตอบถูก/ผิด และตอนจบ
# Lists: สร้าง display ของตัวอักษรและใช้ append()
# Loops: for อ่านตัวอักษร และ while ควบคุมรอบเกม
# Tuples: เก็บ HANGMAN_ART ที่ไม่ต้องเปลี่ยน
# Sets: เก็บตัวอักษรที่เคยทายและตัวอักษรที่ถูกโดยไม่ซ้ำ
# Dictionaries: จับคู่คำศัพท์กับคำใบ้
# Functions: แยกสุ่มคำ สร้างหน้าจอ แสดงสถานะ และควบคุมเกม
# Randomisation: random.choice() สุ่มคำลับ

import random

HANGMAN_ART = (
    """ +---+\n     |\n     |\n     |\n    ===""",
    """ +---+\n O   |\n     |\n     |\n    ===""",
    """ +---+\n O   |\n |   |\n     |\n    ===""",
    """ +---+\n O   |\n/|\\  |\n     |\n    ===""",
    """ +---+\n O   |\n/|\\  |\n/ \\  |\n    ===""",
)

CATEGORIES = {
    "animals": {
        "rabbit": "It has long ears.",
        "tiger": "It has orange and black stripes.",
        "panda": "It likes bamboo.",
    },
    "food": {
        "pizza": "It has cheese and a round base.",
        "sushi": "It often has rice and seaweed.",
        "mango": "It is a sweet yellow fruit.",
    },
    "space": {
        "rocket": "It carries people beyond Earth.",
        "saturn": "It is famous for its rings.",
        "comet": "It is an icy space traveler.",
    },
}


def choose_word(word_data):
    word = random.choice(list(word_data.keys()))
    return word, word_data[word]


def choose_category(category_data):
    """แสดงหมวดและถามซ้ำจนผู้เล่นพิมพ์ Key ที่มีอยู่จริง."""
    print("Categories: " + " | ".join(category_data))
    category = input("Choose a category: ").strip().lower()
    while category not in category_data:
        print("Please choose animals, food, or space.")
        category = input("Choose a category: ").strip().lower()
    return category


def make_display(secret_word, correct_letters):
    display = []
    for letter in secret_word:
        if letter in correct_letters:
            display.append(letter.upper())
        else:
            display.append("_")
    return " ".join(display)


def show_screen(category, secret_word, hint, correct_letters, guessed_letters, mistakes):
    print("\n" + HANGMAN_ART[mistakes])
    print("Category: " + category.upper())
    print("Hint: " + hint)
    print("Word: " + make_display(secret_word, correct_letters))
    print("Guessed: " + " ".join(sorted(guessed_letters)))
    print("Lives: " + "♥ " * (4 - mistakes) + "♡ " * mistakes)


def play_hangman():
    category = choose_category(CATEGORIES)
    secret_word, hint = choose_word(CATEGORIES[category])
    guessed_letters = set()
    correct_letters = set()
    mistakes = 0

    print("╔══════════════════════════════╗")
    print("║       CATEGORY HANGMAN       ║")
    print("╚══════════════════════════════╝")

    while mistakes < 4 and not set(secret_word).issubset(correct_letters):
        show_screen(category, secret_word, hint, correct_letters, guessed_letters, mistakes)
        guess = input("Guess one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please type one letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.add(guess)
            if guess in secret_word:
                correct_letters.add(guess)
                print("Correct!")
            else:
                mistakes += 1
                print("Wrong guess!")

    show_screen(category, secret_word, hint, correct_letters, guessed_letters, mistakes)
    if set(secret_word).issubset(correct_letters):
        print("★ YOU SAVED THE ANIMAL! ★")
    else:
        print("GAME OVER — The word was " + secret_word.upper())


play_hangman()
