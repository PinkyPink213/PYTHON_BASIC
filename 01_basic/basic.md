# Chapter 01 — Python Basic

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | Demo Terminal Profile เทียบ Pygame Card |
| 10–50 | Variables, String, Input, Number และ Math |
| 50–65 | ทำ `09_1` และเริ่มผลงาน `09_2` |
| 65–75 | พิมพ์ `10` เพื่อติดตั้ง ตรวจสอบ และเปิดหน้าต่างแรก |
| 75–95 | พิมพ์ตาม `11_1` พร้อม Practice ทุก STEP |
| 95–115 | Upgrade ผลงานเดิมด้วย `11_2` |
| 115–120 | ชี้ DATA/UI และ Demo ผลงาน |

ไฟล์ที่ทำไม่ทันเป็น Bonus ไม่ใช่งานบังคับในคาบ

พื้นฐานที่เด็กต้องใช้ก่อนเริ่มเขียนเกม โดยบทนี้ยังไม่สอน `if-elif-else`

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `00_comments_and_quotes.py` | Comment ทั้งบรรทัด/ท้ายบรรทัด, `'...'`, `"..."`, `\'`, `\"`, `\n` และ Triple Quotes |
| `01_print_function.py` | แสดงข้อความ ตัวเลข และหลายค่าด้วย `print()` |
| `02_variables.py` | สร้าง เปลี่ยน และคัดลอกค่าของตัวแปร |
| `03_string_manipulation.py` | ต่อและทำซ้ำ String, `lower()`, `upper()`, `strip()` และ f-string |
| `04_input_function.py` | ถามและเก็บคำตอบด้วย `input()` |
| `05_variable_naming_rules.py` | กฎการตั้งชื่อและ `snake_case` |
| `06_data_types.py` | `str`, `int`, `float`, `bool` และ `type()` |
| `07_type_conversion.py` | Casting ด้วย `int()`, `float()` และ `str()` |
| `08_mathematical_operations.py` | Operators, ลำดับการคำนวณ, `+=` และ `-=` |
| `09_1_profile_generator.py` | เล่นและศึกษา Adventure Profile Generator |
| `09_2_create_your_profile.py` | สร้าง Profile Generator ด้วยไอเดียของตัวเอง |
| `10_pygame_first_window.py` | ติดตั้ง Pygame, ตรวจสอบ และเปิดหน้าต่างสีแรกโดยไม่ใช้ Loop |
| `11_1_profile_generator_pygame.py` | เรียน Pygame Basic พร้อมแปลง Profile เป็นการ์ดทีละขั้น |
| `11_2_create_your_profile_pygame.py` | สร้าง Pygame Profile Card ของตัวเอง |

## วิธีเรียน

1. ครูอธิบาย Example และให้เด็กทายผลก่อน Run
2. เด็กอ่านผลลัพธ์หรือเงื่อนไขใน Practice แล้วคิดโค้ดเอง
3. เด็กทำ Your Turn โดยยังไม่เปิด `answers`
4. Run ตรวจทีละเคส แล้วค่อยเปรียบเทียบเฉลย
5. ปิดท้ายด้วย Mini Project ที่รวมความรู้ทั้งบท

## ผลลัพธ์ท้ายบท

เด็กสามารถรับและเก็บข้อมูล จัดข้อความ แปลงชนิดข้อมูล คำนวณ และแสดง Profile ที่ออกแบบเองได้

## Pygame Upgrade

เส้นทางไฟล์:

```text
09_1_profile_generator.py
        ↓ เรียนเปิดหน้าต่าง Pygame ครั้งแรก
10_pygame_first_window.py
        ↓ พิมพ์ตามและเรียนวิธี Convert
11_1_profile_generator_pygame.py

09_2_create_your_profile.py
        ↓ เปิดคู่กันและทำ STEP/TODO
11_2_create_your_profile_pygame.py
```

เก็บ Terminal Profile ไว้เพื่อฝึก `print()` และ `input()` ก่อน จากนั้นเรียนการเปิด
หน้าต่าง สี รูปทรง และข้อความ แล้วนำ Variables เดิมไปแสดงเป็น Profile Card
บทนี้วาด Static Profile Card หนึ่งครั้งและใช้ `event.wait()` จึงยังไม่ใช้
`if`, `for` หรือ `while` ก่อนลำดับบท
