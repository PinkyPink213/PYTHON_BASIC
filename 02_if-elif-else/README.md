# Python for Kids — Terminal to Pygame Creator Path

หลักสูตร Python แบบลงมือพิมพ์และสร้างเกมสำหรับเด็กประถม

![ตัวอย่างโลกของเกมที่จะสร้าง](./docs/images/pygame-game-creator-path.png)

เด็กจะเริ่มจาก Python บน Terminal เพื่อเข้าใจ `print()`, `input()` และ Logic
จากนั้นในแต่ละ Chapter จะเรียน Pygame เพิ่มเพียงหนึ่งเรื่อง แล้วนำความรู้ใหม่
ไปแปลง Mini Project เดิมให้มีหน้าต่าง ภาพ ปุ่ม และการโต้ตอบ

## ติดตั้ง Pygame

macOS / Linux:

```bash
python3 -m pip install pygame
```

Windows (PowerShell หรือ Command Prompt):

```powershell
py -m pip install pygame
```

ตรวจว่าติดตั้งสำเร็จ:

```powershell
py -c "import pygame; print(pygame.version.ver)"
```

> สำหรับครู: ให้ทดลอง Run ไฟล์ Pygame ทุกไฟล์บนเครื่องที่จะใช้สอนก่อนเริ่มคาบ
> ไฟล์ตัวอย่างมีคอมเมนต์แบ่ง `SETUP`, `EVENT`, `UPDATE` และ `DRAW` ไว้แล้ว
> หาก Windows ไม่มีคำสั่ง `py` ให้ลอง `python` และตรวจว่าเลือก Add Python to PATH
> ตอนติดตั้ง Python แล้ว
>
> หากใช้ Python รุ่นใหม่มากและติดตั้ง `pygame` ไม่ผ่าน ให้ใช้
> `py -m pip install pygame-ce` (Windows) หรือ
> `python3 -m pip install pygame-ce` (macOS/Linux) แทน โค้ดยังคงเขียน
> `import pygame` เหมือนเดิม

ในแต่ละ Chapter ใช้รูปแบบเดียวกัน:

1. เด็กพิมพ์ **Example ที่รันได้** ตามครูและอธิบายผล
2. ทำ **Your turn / TODO** ที่อยู่ทันทีหลัง Example โดยปรับเพียงเรื่องที่เพิ่งเรียน
3. ทายผลก่อน Run แล้วตรวจด้วย **Run Checkpoint**
4. เปิด `answers` หลังลองทำเองแล้วเท่านั้น (เฉพาะบทที่มี Answer)
5. สร้าง Terminal Example (`_1`) และ Terminal Project ของเด็ก (`_2`)
6. เรียน Pygame เรื่องใหม่จากไฟล์บทสอนที่มี Example → Your turn → TODO
7. ศึกษา Pygame Example (`_1`) ที่ Convert เกมเดิมครบทั้ง DATA และ Logic
8. เปิดสามไฟล์ข้างกัน แล้ว Convert Terminal Project ของเด็กใน Pygame Starter (`_2`)
9. ทดสอบให้ผลตรง Terminal ก่อนเพิ่ม Creative Game Rules

### วิธีสอน Pygame ให้เด็กรู้ว่ากำลังทำอะไร

ทุกไฟล์สอนใช้จังหวะเดียวกัน:
**Example → พิมพ์ตาม → อธิบาย → Your turn/TODO → ทายผล → Run Checkpoint**
ครูให้เด็กชี้ 4 ส่วนก่อนจบ Practice: **DATA** ที่เกมจำ, **EVENT** ที่ผู้เล่นทำ,
**UPDATE/logic** ที่เปลี่ยนข้อมูล และ **DRAW** ที่นำข้อมูลไปแสดง ไม่เน้นจำคำสั่งโดด ๆ

Chapter 01–03 ใช้ `pygame.event.wait()` เพื่อยังไม่ข้ามไปใช้ Loop; Chapter 04
จึงสอน Game Loop แบบ `EVENT → UPDATE → DRAW` แล้วใช้ pattern นี้ต่อจนจบหลักสูตร

ไฟล์ Upgrade ต้องเปิดคู่กับ Terminal Project ของเด็กและใช้ Migration Map:
เก็บ DATA/logic เดิม, เปลี่ยน `input → event`, เปลี่ยน `print → render/draw`
จึงไม่ต้องเขียนเกมซ้ำจากศูนย์

### ความหมายของชื่อไฟล์เกม

- `_1` คือ Example สมบูรณ์สำหรับเล่น พิมพ์ตาม และศึกษา
- `_2` คือพื้นที่ให้เด็กสร้างหรือ Convert ผลงานของตัวเองด้วย TODO Guide
- ไฟล์ Pygame `_1` ต้องรักษาคำถาม ข้อมูล สูตร เงื่อนไข และผลชนะ–แพ้จาก Terminal `_1`
- ไฟล์ Pygame `_2` ต้องนำ DATA/Logic จาก Terminal `_2` ของเด็ก ไม่เปลี่ยนกลับเป็นธีม Example
- หน้าตาและวิธีรับคำตอบเปลี่ยนได้ แต่กติกาเดิมต้องผ่าน Test ก่อนเพิ่มกติกาสร้างสรรค์

## Pygame Progression

| Chapter | เกมที่นำมา Upgrade | Pygame เรื่องใหม่ |
|---|---|---|
| 01 Basic | Profile Generator | ติดตั้ง เปิดหน้าต่าง สี รูปทรง เส้น และข้อความ |
| 02 If–Else | Mystery Animal | Event, รูปภาพ และปุ่มคลิก |
| 03 Lists | Treasure Backpack | วาด Inventory จาก List |
| 04 Loops | Mystery Animal Loop | Game loop, FPS, keyboard และ animation |
| 05 Tuples | Space Coordinates | ตำแหน่ง `(x, y)` และการคลิกวัตถุ |
| 06 Sets | Rescue Team | เลือกตัวละครโดยไม่ซ้ำ |
| 07 Dictionaries | Pet Rescue | สร้าง Character Card จาก Dictionary |
| 08 Functions | Dice Battle | แยก UI และ game logic เป็น Functions |

## เกมที่เด็กจะได้สร้างในแต่ละ Chapter

ภาพด้านล่างมาจาก Pygame Example ที่อยู่ในหลักสูตรจริง เด็กจะเริ่มจาก Terminal
Version ก่อน แล้วค่อยสร้างหน้าตา Pygame และออกแบบ Version ของตัวเอง

| Chapter และเกม | ผลงานที่เด็กจะได้ | ภาพตัวอย่าง |
|---|---|---|
| **01 Basic — Adventure Profile Card** | รับชื่อ อายุ สัตว์ที่ชอบ และเลขนำโชค คำนวณข้อมูล แล้วเปลี่ยนผล `print()` เป็นการ์ดที่มีสี Shapes เส้น และข้อความ | <img src="./docs/images/game-previews/01-profile-card.png" width="300" alt="Adventure Profile Card"> |
| **02 If–Elif–Else — Mystery Animal** | ใช้คำใบ้และ Conditions ทายสัตว์ จากนั้นเปลี่ยน `input()` เป็นปุ่มรูปภาพและ Mouse Event | <img src="./docs/images/game-previews/02-mystery-animal.png" width="300" alt="Mystery Animal Game"> |
| **03 Lists — Treasure Backpack** | เลือกของ 3 ชิ้น จัดกระเป๋า พบเหตุการณ์ใหม่ เปลี่ยนของ และไปถึง Ending จากข้อมูลใน List | <img src="./docs/images/game-previews/03-treasure-backpack.png" width="300" alt="Treasure Backpack Game"> |
| **04 Loops — Mystery Animal Loop** | ทายซ้ำหลายรอบ ใช้ Game Loop, FPS, Keyboard และ Animation โดยซ่อนรูปสัตว์จนกว่าจะเฉลย | <img src="./docs/images/game-previews/04-mystery-animal-loop.png" width="300" alt="Mystery Animal Loop Game"> |
| **05 Tuples — Space Coordinates** | เก็บจุดหมายและพิกัดคงที่ใน Tuple เลือกตำแหน่งบนแผนที่ และตรวจภารกิจจาก `(x, y)` | <img src="./docs/images/game-previews/05-space-coordinates.png" width="300" alt="Space Coordinates Game"> |
| **06 Sets — Rescue Team** | เลือกฮีโร่ต่างกัน 3 คนโดยไม่ซ้ำ รวม Skills และตรวจทักษะที่ภารกิจกู้ภัยต้องใช้ | <img src="./docs/images/game-previews/06-rescue-team.png" width="300" alt="Rescue Team Game"> |
| **07 Dictionaries — Pet Rescue** | สร้าง Character Cards จาก Nested Dictionary เลือกสัตว์และของที่ต้องการ แล้วอัปเดตสถานะการช่วยเหลือ | <img src="./docs/images/game-previews/07-pet-rescue.png" width="300" alt="Pet Rescue Game"> |
| **08 Functions — Dice Battle** | แยก Function ทอยลูกเต๋า กติกาต่อสู้ และ UI รักษาชื่อผู้เล่น จำนวนรอบ และคะแนนชนะ | <img src="./docs/images/game-previews/08-dice-battle.png" width="300" alt="Dice Battle Game"> |
| **Milestone 1 — Category Hangman** | เลือกหมวดคำศัพท์ อ่าน Hint ทายตัวอักษร ดูรูป Hangman เพิ่มทีละส่วน และออกแบบหมวดของตัวเอง | <img src="./docs/images/game-previews/09-hangman.png" width="300" alt="Category Hangman Game"> |
| **Milestone 2 — Tic-Tac-Toe** | สร้างกระดาน 3×3 ตรวจช่องซ้ำ Win/Draw เก็บ Score และออกแบบสัญลักษณ์หรือกติกาพิเศษ | <img src="./docs/images/game-previews/10-tic-tac-toe.png" width="300" alt="Tic-Tac-Toe Game"> |

ไฟล์ `_1` คือเกมตัวอย่างสมบูรณ์ ส่วน `_2` เปิดพื้นที่ให้เด็กนำ Terminal Project
ของตัวเองมา Convert และเพิ่ม Theme, Asset, Story และ Creative Game Rules

Chapter 01–02 เก็บ Terminal Version ไว้ครบ แล้วเพิ่ม Pygame Version ต่อท้าย
เพื่อให้ครูเปรียบเทียบ `print/input` กับ `render/event` ได้โดยตรง ส่วนภาพใน
`assets/` เป็นตัวเลือกพร้อมใช้ เด็กสามารถเปลี่ยนเป็นภาพของตัวเองหลังเกมทำงานแล้ว

ตั้งแต่ Chapter 04 มี `assets/game_asset_choices.png` เป็นภาพ atlas ชุด Space,
Heroes, Pets, Dice Monster, Heart และ Star พร้อม README บอกวิธีเลือกใช้ เด็กไม่ต้อง
เสียเวลาค้นภาพในคาบ แต่ยังเลือกวาดหรือเปลี่ยนภาพเองได้ใน Creative Challenge

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
