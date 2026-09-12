# Chapter 06 — Python Sets

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | Demo การเลือกสมาชิกไม่ซ้ำ |
| 10–50 | membership, add/remove และ set operations |
| 50–70 | เกม Set Terminal ของเด็ก |
| 70–90 | พิมพ์ `09_pygame_set_selection.py` |
| 90–115 | Upgrade ด้วย `10_2` โดยยังไม่ใช้ Dictionary |
| 115–120 | อธิบาย selected→membership→สี Card |

Frozenset และ methods เพิ่มเติมเป็น Bonus

บทสอน Pygame ให้พิมพ์ Example เลือก Card ก่อน แล้วทำ Your turn/TODO กับ
`add()`, `remove()` และ membership พร้อม Run Checkpoint

Set เก็บค่าที่ไม่ซ้ำ ไม่มี Index และลำดับที่แสดงอาจเปลี่ยนได้

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `01_python_sets.py` | สร้าง Set, ค่าซ้ำ และ Set ว่างด้วย `set()` |
| `02_access_set_items.py` | ตรวจด้วย `in`/`not in` และอ่านด้วย `for` |
| `03_add_and_remove_items.py` | `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()` |
| `04_loop_sets.py` | ใช้ Set กับ `for` และ Conditions |
| `05_join_sets.py` | Union, Intersection, Difference และ Symmetric Difference |
| `06_frozenset.py` | Set ที่เพิ่มหรือลบสมาชิกไม่ได้ |
| `07_set_methods_exercises.py` | แบบฝึกรวม Set Methods |
| `08_1_rescue_team_game.py` | เล่นเกมจัดทีมกู้ภัยโดยใช้ Set |
| `08_2_create_your_set_game.py` | สร้างเกม Set ของตัวเอง |
| `09_pygame_set_selection.py` | Pygame Basic: เลือกตัวละครโดยไม่ซ้ำ |
| `10_1_rescue_team_pygame.py` | Guided Example: Rescue Team Pygame |
| `10_2_create_your_set_game_pygame.py` | Upgrade เกมที่เด็กสร้างใน `08_2` |

## สิ่งที่ต้องจำ

- Set ว่างใช้ `set()` เพราะ `{}` คือ Dictionary ว่าง
- `remove()` เกิด Error เมื่อไม่มีค่า แต่ `discard()` ไม่เกิด Error
- `pop()` ลบสมาชิกที่คาดตำแหน่งล่วงหน้าไม่ได้
- `frozenset` เหมาะกับชุดข้อมูลที่ไม่ควรถูกเปลี่ยน

## ผลลัพธ์ท้ายบท

เด็กใช้ Set กำจัดข้อมูลซ้ำ ตรวจสมาชิก และเปรียบเทียบกลุ่มข้อมูลเพื่อสร้างระบบทีมในเกมได้

## Pygame Upgrade

เด็กคลิกเลือกสมาชิกลง Set โดยชื่อไม่ซ้ำ สีของ Card แสดง membership และภารกิจ
ตรวจ required skills ด้วย Set Operations เท่านั้น ไม่ใช้ Dictionary ก่อน Chapter 07
ต้องเลือกสมาชิกต่างกันครบ 3 คนก่อนเริ่มภารกิจเหมือน Terminal Version
