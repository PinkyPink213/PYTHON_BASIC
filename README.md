# Python for Kids — 10-Class Game Creator Path

หลักสูตร Python แบบลงมือพิมพ์และสร้างเกมสำหรับเด็กประถม

ในแต่ละ Chapter ใช้รูปแบบเดียวกัน:

1. ครูอธิบาย Example
2. เด็กพิมพ์ Typing Practice ตามด้วยตัวเอง
3. เด็กทำ Your Turn หรือ TODO
4. ตรวจคำตอบในโฟลเดอร์ `answers`
5. ปิดท้ายด้วยเกมตัวอย่างและงานสร้างเกมของตัวเอง

## 10 Classes

| ลำดับ | Chapter | เนื้อหาหลัก |
|---:|---|---|
| 01 | [Basic](./01_basic) | Comments, Print, Variables, Strings, Input, Data Types, Casting และ Math |
| 02 | [If–Elif–Else](./02_if-elif-else) | Boolean, Conditions, Logical Operators และ Nested `if` |
| 03 | [Lists](./03_list) | Access, Check, Change, Add, Remove, Methods และ Nested Lists |
| 04 | [Loops](./04_loop) | `for`, `range`, `while`, `break`, `continue` และ `match-case` |
| 05 | [Tuples](./05_tuple) | Access, Update, Unpack, Loop, Join และ Tuple Methods |
| 06 | [Sets](./06_set) | Access, Add, Remove, Loop, Join, Frozenset และ Set Methods |
| 07 | [Dictionaries](./07_dictionaries) | Access, Change, Add, Remove, Loop, Copy และ Nested Dictionaries |
| 08 | [Functions](./08_functions) | Random, Error Handling, Arguments, Return, Scope และ Function Techniques |
| 09 | [Capsule: Hangman](./milestone-projects/01_hangman) | รวมความรู้สร้างเกมทายคำพร้อม ASCII Art |
| 10 | [Capsule: Tic-Tac-Toe](./milestone-projects/02_tic_tac_toe) | รวมความรู้สร้างเกมกระดาน 3×3 สำหรับสองคน |

`range()` สอนอยู่ใน Chapter 04 Loops ส่วน Array และ Iterator ไม่อยู่ในขอบเขตหลักสูตร 10 Classes นี้

## Re-knowledge Project

[Create Your Adventure Game](./reknowledge/create_your_adventure_game.py) เป็นโปรเจกต์ทบทวนหลังเรียน Basic และ If–Elif–Else โดยมีเกมตัวอย่าง [Escape from the Magic Castle](./reknowledge/answers/escape_from_magic_castle.py)

## Capsule Milestones

หลังเรียนครบ 8 Chapters นักเรียนจะสร้างเกมใหญ่สองงาน:

### [Capsule Milestone 1 — Hangman](./milestone-projects/01_hangman)

เกมทายคำที่มี ASCII Art, คำใบ้, จำนวนชีวิต, ตัวอักษรที่เคยทาย และหลายตอนจบ

ความรู้หลักที่ใช้:

- Strings, Lists และ Sets
- `if-elif-else`
- `for` และ `while`
- Functions และ `return`
- Dictionaries สำหรับหมวดและคำใบ้
- Randomisation และ Error Handling ตามความเหมาะสม

### [Capsule Milestone 2 — Tic-Tac-Toe](./milestone-projects/02_tic_tac_toe)

เกมกระดาน 3×3 สำหรับผู้เล่นสองคน มีการตรวจช่องซ้ำ ผู้ชนะ ผลเสมอ และการเล่นหลายรอบ

ความรู้หลักที่ใช้:

- Nested Lists
- Loops และ Conditions
- Functions, Arguments และ Return Values
- Sets หรือ Tuples สำหรับรูปแบบการชนะ
- Dictionaries สำหรับคะแนนผู้เล่น
- Error Handling สำหรับตำแหน่งที่พิมพ์ผิด

## ขอบเขตของ Capsule Milestones

Milestones ใช้เฉพาะความรู้จาก 8 Chapters หลัก ไม่บังคับใช้เนื้อหาที่ยังไม่ได้เรียน เช่น:

- Object-Oriented Programming และ Classes
- GUI frameworks
- External packages
- File และ Database storage

แต่ละ Milestone ต้องมี:

- เกมตัวอย่างสมบูรณ์สำหรับเล่นและศึกษา
- Starter Project ที่แบ่ง TODO เป็นขั้นสำหรับเด็กประถม
- Guide ที่ช่วยให้เริ่มได้ แต่ไม่เปิดเผยโค้ดทั้งหมด
- Creative Choices เพื่อให้เปลี่ยนธีม กติกา และหน้าตาได้
- Checklist ตรวจความรู้ที่นำมาใช้
- ตัวอย่างเฉลยในโฟลเดอร์ `answers`

## ลำดับการเรียน

```text
01 Basic
   ↓
02 If–Elif–Else
   ↓
03 Lists
   ↓
04 Loops
   ↓
05 Tuples
   ↓
06 Sets
   ↓
07 Dictionaries
   ↓
08 Functions
   ↓
Capsule 1: Hangman
   ↓
Capsule 2: Tic-Tac-Toe
```

## เมื่อจบ 10 Classes เด็กจะทำอะไรได้บ้าง?

### เข้าใจพื้นฐานการเขียนโปรแกรม

- อ่านและเขียน Python ที่มี Variables, Data Types, Input และ Output
- ใช้ Conditions และ Loops ควบคุมเส้นทางและการทำงานซ้ำ
- เลือกใช้ List, Tuple, Set และ Dictionary ให้เหมาะกับข้อมูล
- แยกโปรแกรมออกเป็น Functions ที่รับข้อมูลและ `return` ผลลัพธ์
- ใช้ Randomisation สร้างเกมที่ผลลัพธ์เปลี่ยนได้
- ใช้ Error Handling รับมือคำตอบผิดโดยไม่ให้เกมหยุดทำงาน

### คิดและแก้ปัญหาเป็นขั้นตอน

- แปลงกติกาเกมเป็น Flow และเงื่อนไข
- แยกงานใหญ่เป็น Functions ขนาดเล็ก
- ทดลองหลายเส้นทาง เช่น ชนะ แพ้ เสมอ และ Input ผิด
- อ่าน Error และแก้ข้อผิดพลาดพื้นฐานได้
- เปรียบเทียบ Example กับ Starter Project แล้วสร้างวิธีของตัวเอง

### สร้างผลงานที่นำไปโชว์ได้

- Adventure Game ที่มีหลายด่านและหลายตอนจบ
- Hangman พร้อมคำสุ่ม คำใบ้ ชีวิต ตัวอักษรที่เคยทาย และ ASCII Art
- Tic-Tac-Toe พร้อมกระดาน ตรวจช่องซ้ำ ผู้ชนะ และผลเสมอ
- ปรับธีม ตัวละคร ข้อความ กติกา และหน้าตาของเกมให้เป็นผลงานเฉพาะตัว

### ผลลัพธ์สุดท้าย

เด็กไม่ได้เพียงพิมพ์โค้ดตาม แต่สามารถวางแผนเกม อธิบายว่าโค้ดแต่ละส่วนทำอะไร
สร้างเกมจาก Guided Starter ทดสอบ แก้ Error และนำเสนอผลงาน Terminal Game
ที่ออกแบบด้วยความคิดสร้างสรรค์ของตัวเองได้
