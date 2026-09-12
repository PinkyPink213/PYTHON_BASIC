# Capsule 1: Hangman

หลัง Terminal Project มี `03_1_play_pygame.py` สำหรับศึกษา และ
`03_2_create_your_pygame.py` สำหรับ Upgrade ผลงาน `02_create_your_game.py`
โดยรักษาคำ หมวด คำใบ้ และ Creative Choices ของเด็กไว้

Starter Pygame เรียง STEP ตรงกับตัวอย่าง: Category Data → Functions → Setup →
Category Event → Letter Event → Update → Draw → Test → Creative Studio

## เกมนี้คืออะไร?

Hangman เป็นเกมทายคำ ผู้เล่นเห็นคำใบ้และช่องว่างแทนตัวอักษรของคำลับ จากนั้นทายครั้งละหนึ่งตัวอักษร ทายถูกจะเปิดตัวอักษร ทายผิดจะเสียหัวใจและ ASCII Art จะเปลี่ยน

## เป้าหมาย

เปิดตัวอักษรของคำลับให้ครบก่อนหัวใจหมด

## Features ในเกมตัวอย่าง

- สุ่มคำสัตว์และคำใบ้จาก Dictionary
- แสดง Category ของคำปัจจุบันและคำใบ้ที่สัมพันธ์กัน
- ผู้เล่นเลือก Animals, Food หรือ Space ก่อนสุ่มคำ และเปลี่ยนหมวดได้เมื่อ Restart
- ซ่อนคำด้วย `_`
- เปิดทุกตำแหน่งของตัวอักษรที่ทายถูก
- เก็บตัวอักษรที่เคยทายด้วย Set
- ป้องกันตัวอักษรซ้ำและ Input ที่ไม่ใช่ตัวอักษรหนึ่งตัว
- แสดงหัวใจและ ASCII Art ตามจำนวนครั้งที่ผิด
- Pygame Version วาดภาพ Hangman เพิ่มทีละส่วนตามจำนวนครั้งที่ผิด
- มี Win และ Game Over

## ความรู้ที่ใช้

- String สำหรับคำลับและตัวอักษร
- List สำหรับสร้างข้อความที่ซ่อน
- Tuple สำหรับ ASCII Art
- Set สำหรับตัวอักษรที่ไม่ซ้ำ
- Dictionary สำหรับจับคู่คำกับคำใบ้
- `for`, `while` และ Conditions
- Functions, Arguments และ Return Values
- `random.choice()`

## สิ่งที่เด็กต้องทำ

1. เล่น [เกมตัวอย่าง](./01_play_example.py) ให้ครบ Win, Game Over, ตัวอักษรซ้ำ และ Input ผิด
2. เขียน Flow ว่าเกมทำอะไรในหนึ่งรอบ
3. เปิด [Guided Starter](./02_create_your_game.py)
4. ออกแบบอย่างน้อย 3 Categories หมวดละ 3 คำพร้อมคำใบ้
5. ให้ผู้เล่นเลือก Category ก่อนโปรแกรมสุ่มคำจากหมวดนั้น
6. วาด ASCII Art อย่างน้อย 4 ระดับ
7. สร้าง Functions ตาม STEP และ Run ทีละส่วน
8. เพิ่ม Creative Features อย่างน้อย 2 อย่าง
9. เปิด Terminal Version คู่กับ `03_2_create_your_pygame.py` แล้วทำ Migration Map
10. ทดสอบว่ากติกาเดิมยังครบ ก่อนเลือก asset/theme ใน Creative Studio

## Terminal → Pygame

| Terminal | Pygame | สิ่งที่ยังเหมือนเดิม |
|---|---|---|
| `input()` ตัวอักษร | `KEYDOWN` | การตรวจคำตอบซ้ำ/ถูก/ผิด |
| `print()` word/hint/lives | `render()` + `blit()` | ค่า secret, used และ lives |
| `while` เล่นเกม | Pygame Game Loop | เงื่อนไข Win/Game Over |

Core ต้องผ่านก่อน: ทายถูก, ทายผิด, ตัวซ้ำ, Win และ Game Over จากนั้นเลือก
Creative อย่างน้อย 2 ด้านและเขียน Design Note ว่าแก้ DATA/logic/UI ส่วนใด

## Creative Ideas

- หมวด Space, Food, Games, Magic หรือ Dinosaurs
- ระดับ Easy/Hard
- Bonus Hint แลกกับหัวใจ
- ระบบคะแนนตามจำนวนครั้งที่เหลือ
- ASCII Art และข้อความชัยชนะของตัวเอง
- ให้ผู้เล่นเลือกหมวดก่อนเริ่ม

## Test Checklist

- [ ] ทายถูกหนึ่งตัวอักษรแล้วเปิดถูกทุกตำแหน่ง
- [ ] ทายผิดแล้วหัวใจลดหนึ่งครั้ง
- [ ] ทายตัวเดิมแล้วไม่เสียหัวใจซ้ำ
- [ ] พิมพ์หลายตัวอักษรแล้วได้รับคำเตือน
- [ ] เปิดคำครบแล้ว Win
- [ ] ทายผิดครบแล้ว Game Over และเห็นเฉลย

## คำถามสำหรับ Demo

- เพราะอะไรใช้ Set เก็บตัวอักษรที่เคยทาย?
- `make_display()` รับอะไรและ Return อะไร?
- `while` หยุดได้ด้วยสองเหตุผลใด?
- Feature ใดเป็นความคิดของเราเอง?

ตัวอย่าง Creative Answer อยู่ที่ [answers/02_create_your_game.py](./answers/02_create_your_game.py)
