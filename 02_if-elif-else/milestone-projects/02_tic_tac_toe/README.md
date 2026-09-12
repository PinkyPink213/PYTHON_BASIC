# Capsule 2: Tic-Tac-Toe

หลัง Terminal Project มี `03_1_play_pygame.py` สำหรับศึกษา และ
`03_2_create_your_pygame.py` สำหรับ Upgrade ผลงาน `02_create_your_game.py`
โดยรักษา board logic, winning lines และ score ของเด็กไว้

Starter Pygame เรียง STEP ตรงกับตัวอย่าง: Board Functions → Setup → State →
Mouse Event → Win/Draw Update → Grid/Symbol Draw → Test → Creative Studio

## เกมนี้คืออะไร?

Tic-Tac-Toe เป็นเกมกระดาน 3×3 สำหรับผู้เล่นสองคน ผู้เล่น X และ O ผลัดกันเลือกแถวกับคอลัมน์ คนแรกที่เรียงสัญลักษณ์ครบสามช่องในแนวนอน แนวตั้ง หรือแนวทแยงชนะ

## เป้าหมาย

สร้างเกมที่ตรวจตำแหน่ง ตรวจผู้ชนะ และตรวจผลเสมอได้อย่างถูกต้อง โดย Input ผิดไม่ทำให้โปรแกรมหยุด

## Features ในเกมตัวอย่าง

- กระดาน Nested List ขนาด 3×3
- แสดงเลขแถวและคอลัมน์
- สลับ Player X และ O
- ป้องกันช่องเดิมและตำแหน่งนอกกระดาน
- Winning Lines ทั้ง 8 แบบ
- ตรวจ Win และ Draw
- Error Handling สำหรับคำตอบที่ไม่ใช่ตัวเลข
- Dictionary สำหรับ Scoreboard

## ความรู้ที่ใช้

- Nested Lists สำหรับกระดาน
- Tuple สำหรับ Winning Lines
- Set สำหรับตำแหน่งที่ถูกใช้
- Dictionary สำหรับคะแนนและข้อมูลผู้เล่น
- Loops และ Conditions
- Functions, Arguments และ Return Values
- Casting และ `try-except`

## สิ่งที่เด็กต้องทำ

1. เล่น [เกมตัวอย่าง](./01_play_example.py) จนพบ Win, Draw และ Input Error
2. วาดกระดานและเขียน Winning Lines ทั้ง 8 แบบบนกระดาษ
3. เปิด [Guided Starter](./02_create_your_game.py)
4. สร้างและทดสอบ Function ทีละตัว
5. ต่อ Functions เป็น Game Loop
6. เปลี่ยนธีมและเพิ่ม Creative Features อย่างน้อย 2 อย่าง
7. เปิด Terminal Version คู่กับ `03_2_create_your_pygame.py` แล้วทำ Migration Map
8. ทดสอบ win/draw/ช่องซ้ำ/restart ให้ครบก่อน Creative Studio

## Terminal → Pygame

| Terminal | Pygame | สิ่งที่ยังเหมือนเดิม |
|---|---|---|
| `input()` row/column | mouse click → row/column | board และการตรวจช่องว่าง |
| `show_board()`/`print()` | grid, symbol และ status ใน DRAW | X/O ใน Nested List |
| `while` ผลัดกันเล่น | Pygame Game Loop | win, draw และสลับ player |

Core ต้องผ่านก่อน แล้วเด็กเลือกอย่างน้อย 2 ด้าน เช่น theme/symbol, palette,
ชื่อ/คะแนน, highlight เส้นชนะ หรือกติกาพิเศษ พร้อมอธิบายว่าแก้ DATA/logic/UI ตรงไหน

## Creative Ideas

- เปลี่ยน X/O เป็น Emoji หรือสัญลักษณ์เวทมนตร์
- รับชื่อผู้เล่น
- เก็บคะแนนหลายรอบ
- ให้เลือกขนาดกรอบหรือสีข้อความ
- เพิ่ม Computer Player แบบสุ่มช่องว่าง
- แสดงเส้นชัยชนะหรือ ASCII Art ตอนจบ

## Test Checklist

- [ ] วางสัญลักษณ์ในช่องว่างได้
- [ ] ช่องเดิมถูกปฏิเสธ
- [ ] เลข 0, 4 และตัวอักษรถูกปฏิเสธ
- [ ] X และ O สลับกันเฉพาะหลังเดินสำเร็จ
- [ ] ตรวจชนะครบแนวนอน แนวตั้ง และแนวทแยง
- [ ] กระดานเต็มโดยไม่มีผู้ชนะจบเป็น Draw

## คำถามสำหรับ Demo

- เพราะอะไร Board จึงเป็น Nested List?
- Winning Lines เก็บข้อมูลรูปแบบใด?
- `has_won()` Return ค่าอะไร?
- Set ช่วยป้องกันช่องซ้ำอย่างไร?
- Feature ใดเป็นความคิดของเราเอง?

ตัวอย่าง Creative Answer อยู่ที่ [answers/02_create_your_game.py](./answers/02_create_your_game.py)
