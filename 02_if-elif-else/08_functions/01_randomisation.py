"""บทที่ 1: Randomisation — สุ่มผลลัพธ์"""

import random

print("--- Examples ---")
print(random.randint(1, 6))
colors = ["red", "blue", "green"]
print(random.choice(colors))
random.shuffle(colors)
print(colors)

print("\n--- Typing Practice ---")
# import random
# coin = random.choice(["heads", "tails"])
# print(coin)

print("\n--- Your turn ---")
# TODO 1: สุ่มเลข 1–10
# TODO 2: สุ่มสัตว์หนึ่งตัวจาก List 3 ตัว

# คำถาม: randint(), choice() และ shuffle() ทำหน้าที่ต่างกันอย่างไร?

