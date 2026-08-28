# Capsule Milestone Projects

สองโปรเจกต์ใหญ่สำหรับสรุปความรู้หลังเรียนครบ 8 Chapters เด็กจะนำสิ่งที่เรียนแยกกันมาประกอบเป็นเกมที่เล่นได้จริงและนำไปโชว์ได้

## Milestones

| ลำดับ | โปรเจกต์ | ผลงานที่สร้าง |
|---:|---|---|
| 01 | [Hangman](./01_hangman) | เกมทายคำพร้อมคำใบ้ หัวใจ ตัวอักษรที่เคยทาย และ ASCII Art |
| 02 | [Tic-Tac-Toe](./02_tic_tac_toe) | เกมกระดาน 3×3 สำหรับสองคน พร้อมตรวจ Win และ Draw |

แต่ละ Milestone จะเก็บ Terminal Version สำหรับทบทวนความรู้ทั้ง 8 Chapters และเพิ่ม
Pygame Version ต่อท้ายในรูปแบบ `_1` ตัวอย่าง, `_2` Starter และ `answers/_2`
โดยใช้ STEP → Practice → Your Turn แบบเดียวกับเกมท้ายบท

## จุดประสงค์

เด็กจะได้ฝึก:

- อ่านเกมตัวอย่างและอธิบาย Flow ด้วยคำพูดของตัวเอง
- แยกเกมหนึ่งเกมออกเป็นปัญหาย่อยและ Functions
- เลือก Data Structure ให้เหมาะกับหน้าที่
- เขียนเกมจาก Guided Starter โดยไม่ลอกทั้งไฟล์
- ทดสอบเส้นทางปกติ ชนะ แพ้ เสมอ และ Input ผิด
- เพิ่มธีม กติกา และหน้าตาที่เป็นความคิดของตัวเอง
- นำเสนอเกมและอธิบายส่วนที่ตัวเองสร้าง

## Files ในแต่ละโปรเจกต์

- `README.md` — อ่านเป้าหมาย กติกา ขั้นตอน และ Checklist ก่อนเริ่ม
- `01_play_example.py` — เกมสมบูรณ์สำหรับเล่นและศึกษา
- `02_create_your_game.py` — Starter Project พร้อม Guide ทีละขั้น
- `answers/02_create_your_game.py` — ตัวอย่าง Creative Answer เปิดเมื่อทำเองแล้วหรือติดจริง ๆ

## วิธีทำ Milestone

ทุก Milestone ใช้ลำดับเดียวกันเพื่อให้เด็กฝึก “แปลง Interface” ไม่ใช่คัดลอกเกมใหม่:

1. เล่นและอธิบาย Terminal Version
2. วงส่วนที่เก็บ **DATA** และ **game logic** — ย้ายมาใช้เหมือนเดิม
3. ทำ Migration Map: `input → event`, `print → draw`, loop เดิม → game loop
4. พิมพ์ Pygame Guided Version และทายผลที่ CHECKPOINT
5. เปิด Terminal/Pygame ข้างกัน แล้วทดสอบ win, lose/draw และ input ผิดให้ตรงกัน
6. ทำ Creative Studio หลัง Core ผ่านเท่านั้น

ไฟล์ `03_2_create_your_pygame.py` ของทั้งสองโปรเจกต์เรียง STEP ให้ตรงกับ
`03_1_play_pygame.py` หนึ่งต่อหนึ่ง เด็กจึงเปิดสองไฟล์ข้างกัน ยืม Pattern
ที่เพิ่งพิมพ์ตาม แล้วเขียนลงพื้นที่ TODO โดยไม่ต้องเดาโครงโปรแกรมใหม่

### Creative Studio

เด็กเขียน Design Note สั้น ๆ ก่อนลงมือ: ชื่อเกม, ผู้เล่นต้องทำอะไร และจุดเด่น
จากนั้นเลือกอย่างน้อย 2 ด้าน ได้แก่ theme/ภาพ, สี/เสียง, ข้อมูลเกม, หรือกติกาพิเศษ
ท้ายคาบต้องชี้ได้ว่าความคิดใหม่ทำให้แก้ **DATA**, **logic** หรือ **UI** ส่วนใด

1. อ่าน README ของเกม
2. เล่น Example ให้ครบหลายตอนจบ
3. อธิบายว่า Variables และ Functions สำคัญทำหน้าที่อะไร
4. วาด Flow เกมลงบนกระดาษ
5. ปิด Example แล้วเปิด Guided Starter
6. ทำทีละ STEP และ Run ตรวจทุกครั้ง
7. เลือก Creative Choices อย่างน้อย 2 อย่าง
8. ทดสอบตาม Test Checklist
9. เปิด Answer เพื่อเปรียบเทียบหลังทำเสร็จ
10. Demo เกมและอธิบายโค้ดของตัวเอง

## ขอบเขตความรู้

ใช้ความรู้จาก 8 Chapters: Basic, If–Elif–Else, Lists, Loops, Tuples, Sets, Dictionaries และ Functions รวม Randomisation กับ Error Handling

ไม่จำเป็นต้องใช้ Classes, GUI, External Packages, Files หรือ Database

## เกณฑ์ผ่าน Capsule

- เกมเปิดและเล่นจนจบได้
- Input ผิดไม่ทำให้เกมพัง
- มีผลลัพธ์ชนะและแพ้/เสมอ
- ใช้ Function แยกหน้าที่สำคัญ
- เด็กอธิบาย Data Structure ที่เลือกใช้ได้
- มีอย่างน้อย 2 Features ที่ออกแบบเอง
- เด็กเล่น Demo และตอบคำถามเกี่ยวกับโค้ดได้
