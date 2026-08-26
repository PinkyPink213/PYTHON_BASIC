# Capsule 2: Tic-Tac-Toe

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

