# Chapter 08 — Functions, Randomisation และ Error Handling

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | Demo logic Function เทียบ draw Function |
| 10–50 | define/call, parameters, return และ scope |
| 50–70 | เกม Function Terminal ของเด็ก |
| 70–90 | พิมพ์ `12_pygame_ui_functions.py` |
| 90–115 | Upgrade ด้วย `13_2` |
| 115–120 | จัดประเภท DATA/logic/UI และ Demo |

`*args/**kwargs`, decorator, lambda, recursion และ generator เป็น Bonus
ไม่อยู่ใน Core Route สองชั่วโมง

บทสอน Pygame ให้พิมพ์ Example UI Function ที่รันได้ก่อน แล้วทำ Your turn/TODO
โดยเปลี่ยน Arguments หรือสร้าง Function เล็กหนึ่งตัว พร้อม Run Checkpoint

บทนี้สอนแยกโปรแกรมเป็นงานย่อยที่เรียกซ้ำได้ และรวมความรู้เพื่อสร้างเกม

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `01_randomisation.py` | `randint()`, `choice()` และ `shuffle()` |
| `02_error_handling.py` | `try-except` รับมือ Input ที่แปลงค่าไม่ได้ |
| `03_python_functions.py` | สร้างและเรียก Function ด้วย `def` |
| `04_1_return_vs_print.py` | ความต่างระหว่าง `print()` และ `return` |
| `04_arguments.py` | Parameters, Arguments, Default และ Keyword Arguments |
| `05_args_kwargs.py` | รับ Arguments ที่ไม่แน่นอนด้วย `*args`, `**kwargs` |
| `06_scope.py` | Local และ Global Scope |
| `07_decorators.py` | Function ที่ครอบและเพิ่มพฤติกรรมให้ Function อื่น |
| `08_lambda.py` | Function สั้นแบบ Lambda |
| `09_recursion.py` | Function ที่เรียกตัวเองและ Base Case |
| `10_generators.py` | ส่งค่าทีละตัวด้วย `yield` |
| `11_1_dice_battle_game.py` | เล่นเกมต่อสู้ด้วยลูกเต๋า |
| `11_2_create_your_function_game.py` | สร้างเกม Function ของตัวเอง |
| `12_pygame_ui_functions.py` | Pygame Basic: แยก UI เป็น Functions |
| `13_1_dice_battle_pygame.py` | Guided Example: Dice Battle Pygame |
| `13_2_create_your_function_game_pygame.py` | Upgrade เกมที่เด็กสร้างใน `11_2` |

## แกนหลักที่ต้องใช้ในเกม

- Function ควรทำหน้าที่หลักหนึ่งอย่างและมีชื่อที่อ่านแล้วเข้าใจ
- `print()` ใช้แสดงผล ส่วน `return` ส่งค่าไปใช้ต่อ
- Randomisation ทำให้เกมแต่ละรอบต่างกัน
- Error Handling ช่วยให้ Input ผิดไม่ทำให้เกมปิด

Decorators, Lambda, Recursion และ Generators เป็นหัวข้อเสริม หากเวลาไม่พอสามารถเรียนหลัง Milestone ได้

## ผลลัพธ์ท้ายบท

เด็กแบ่งเกมออกเป็น Functions รับ Arguments ส่งค่ากลับ สุ่มเหตุการณ์ และรับมือคำตอบผิดได้

## Pygame Upgrade

เด็กแยก game logic ออกจาก UI functions แล้วนำ Dice Battle เดิมมาแสดงผลด้วยปุ่ม
ลูกเต๋าและข้อความบนหน้าจอ ปิดท้ายด้วยการอธิบายว่า Function ใด update ข้อมูลและ
Function ใดมีหน้าที่ draw เท่านั้น
Pygame Version ยังคงชื่อผู้เล่น จำนวนรอบ ผล `battle()` และจำนวนชัยชนะจาก Terminal
