# Chapter 02 — If, Elif และ Else

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | ทบทวน input และ Demo Mystery Animal สองเวอร์ชัน |
| 10–50 | if/elif/else, Boolean และ logical operators |
| 50–70 | เล่น `06_1` และสร้างเกม `06_2` |
| 70–90 | พิมพ์ `07_pygame_event_image_button.py` |
| 90–115 | Upgrade เกมเดิมด้วย `08_2` |
| 115–120 | อธิบาย input→event และ print→draw |

Nested challenges ที่เหลือเป็น Bonus หากเวลาไม่พอ

ไฟล์ Pygame ใช้รูปแบบเดียวกับ `01_if_elif_else.py`: พิมพ์ Example ที่รันได้ก่อน
แล้วทำ Your turn/TODO ทันที จากนั้นทายผลและ Run Checkpoint

เรียนรู้การให้โปรแกรมตัดสินใจและสร้างเกมที่มีหลายผลลัพธ์

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `00_1_input_lesson.py` | ทบทวน `input()` สำหรับรับคำตอบในเกม |
| `00_2_input_todo.py` | แบบฝึกรับคำตอบก่อนเริ่ม Conditions |
| `01_if_elif_else.py` | `if`, `elif`, `else`, Comparison Operators และการเยื้อง |
| `02_boolean_true_false.py` | Boolean `True`/`False` และผลจากการเปรียบเทียบ |
| `03_logical_operators.py` | เชื่อมเงื่อนไขด้วย `and`, `or`, `not` |
| `04_1_nested_if_roller_coaster.py` | Nested `if` ผ่านสถานการณ์รถไฟเหาะ |
| `04_2_nested_if_treasure_game.py` | ฝึก Nested `if` ในเกมสมบัติ |
| `05_pass_statement.py` | ใช้ `pass` เว้นส่วนที่ยังไม่เขียน |
| `06_1_mystery_animal_game.py` | เล่นเกมทายสัตว์ตัวอย่าง |
| `06_2_create_your_guessing_game.py` | สร้าง Guessing Game พร้อมธีมและคำใบ้ของตัวเอง |
| `07_pygame_event_image_button.py` | Pygame Basic: โหลดรูป Event, Rect และปุ่มคลิก |
| `08_1_mystery_animal_pygame.py` | แปลง Mystery Animal เดิมเป็น Pygame |
| `08_2_create_your_guessing_game_pygame.py` | แปลง Guessing Game ของตัวเองเป็น Pygame |

## สิ่งที่ต้องจำ

- `=` ใช้เก็บค่า แต่ `==` ใช้เปรียบเทียบ
- เงื่อนไขลงท้ายด้วย `:` และโค้ดด้านในเยื้อง 4 ช่อง
- Python ตรวจ `if-elif-else` จากบนลงล่างและทำทางเลือกแรกที่เป็นจริง
- Nested `if` ใช้เมื่อด่านถัดไปควรถูกตรวจหลังผ่านด่านแรก

## ผลลัพธ์ท้ายบท

เด็กสร้างเกมทายคำหรือทายสิ่งของที่มีคำใบ้ เงื่อนไขหลายทาง และผลลัพธ์ชนะ/ลองใหม่ได้

## Pygame Upgrade

Terminal Version ยังคงอยู่ครบสำหรับฝึก `input()` และ Conditions ก่อน จากนั้นเด็ก
เรียนว่า mouse event ทำหน้าที่เป็น input และข้อความ/ภาพบนจอทำหน้าที่แทน `print()`
พร้อม Creative Challenge ให้เลือก asset ที่เตรียมไว้หรือใช้รูปของตัวเอง

หลักการ Convert: จำนวนครั้งที่ทาย คำใบ้ Bonus Round และผลลัพธ์ต้องมาจาก
Terminal Version เดิม; เปลี่ยนเฉพาะ `input()` เป็น click และ `print()` เป็น DRAW
