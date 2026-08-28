# Chapter 04 — Python Loops และ Match-Case

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | แกะโค้ดซ้ำจาก Chapter 03 |
| 10–50 | for, range, while, break และ continue |
| 50–70 | เกม Terminal Loop ของเด็ก |
| 70–90 | พิมพ์ `07` และ trace EVENT→UPDATE→DRAW |
| 90–115 | Upgrade เกมเดิมด้วย `08_2` |
| 115–120 | อธิบายหนึ่ง frame และ Demo |

`match-case` และ animation ตกแต่งเป็น Bonus เมื่อ Core เสร็จ

Loop ช่วยทำงานซ้ำ ส่วน `match-case` ใช้เลือกการทำงานจากค่าหนึ่งค่าและไม่ใช่ Loop

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `01_for_loop.py` | ใช้ `for` อ่านข้อมูลทีละชิ้น |
| `02_for_with_range.py` | ทำซ้ำตามจำนวนรอบด้วย `range()` |
| `03_while_loop.py` | ทำซ้ำขณะที่เงื่อนไขเป็นจริงและป้องกัน Infinite Loop |
| `04_break_and_continue.py` | หยุด Loop ด้วย `break` และข้ามรอบด้วย `continue` |
| `05_loop_list_challenge.py` | รวม List, Conditions และ Loops |
| `05_match_case.py` | `match`, `case`, `case _` และหลายคำตอบด้วย `|` |
| `06_1_mystery_animal_while_game.py` | เล่น Guessing Game เวอร์ชัน `while` |
| `06_2_convert_game_to_match.py` | แปลงเฉพาะส่วน `if-elif-else` ที่กำหนดเป็น `match-case` |
| `06_3_create_your_while_match_game.py` | สร้างเกมถามซ้ำและเมนูคำสั่งด้วยไอเดียของตัวเอง |
| `07_pygame_game_loop_animation.py` | Pygame Basic: Game Loop, FPS และ Animation |
| `08_1_mystery_animal_loop_pygame.py` | Guided Example: Mystery Animal Pygame |
| `08_2_create_your_while_match_game_pygame.py` | Upgrade เกมที่เด็กสร้างใน `06_3` |

## เลือกใช้ให้ถูก

- `for` — อ่านสมาชิกหรือทำซ้ำตามจำนวนที่รู้
- `while` — ถามซ้ำจนกว่าจะถูกหรือจนกว่าเกมจบ
- `break` — ออกจาก Loop ทันที
- `continue` — ข้ามเฉพาะรอบปัจจุบัน
- `match-case` — เลือกหนึ่งการทำงานจากค่าที่ได้รับ

## ผลลัพธ์ท้ายบท

เด็กดัดแปลง Guessing Game ให้ถามซ้ำ รับมือคำตอบผิด และเลือกคำสั่งด้วย `match-case` ได้

## Pygame Upgrade

บทนี้เริ่ม Game Loop อย่างเป็นทางการผ่าน `EVENT → UPDATE → DRAW` รวม FPS และ
animation แล้วนำไปทำ Mystery Animal เวอร์ชันเคลื่อนไหว ทุก STEP มี Practice
ให้พิมพ์ทันที และไม่ใช้ Pygame helper ที่ยังไม่ได้สอน
