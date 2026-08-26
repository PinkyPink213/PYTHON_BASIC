# Chapter 08 — Functions, Randomisation และ Error Handling

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

## แกนหลักที่ต้องใช้ในเกม

- Function ควรทำหน้าที่หลักหนึ่งอย่างและมีชื่อที่อ่านแล้วเข้าใจ
- `print()` ใช้แสดงผล ส่วน `return` ส่งค่าไปใช้ต่อ
- Randomisation ทำให้เกมแต่ละรอบต่างกัน
- Error Handling ช่วยให้ Input ผิดไม่ทำให้เกมปิด

Decorators, Lambda, Recursion และ Generators เป็นหัวข้อเสริม หากเวลาไม่พอสามารถเรียนหลัง Milestone ได้

## ผลลัพธ์ท้ายบท

เด็กแบ่งเกมออกเป็น Functions รับ Arguments ส่งค่ากลับ สุ่มเหตุการณ์ และรับมือคำตอบผิดได้
