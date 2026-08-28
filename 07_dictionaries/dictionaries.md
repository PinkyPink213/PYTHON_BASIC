# Chapter 07 — Python Dictionaries

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | Demo Character Card ที่อ่านจากข้อมูล |
| 10–50 | key/value, access, change และ nested dictionary |
| 50–70 | เกม Dictionary Terminal ของเด็ก |
| 70–90 | พิมพ์ `08_pygame_dictionary_cards.py` |
| 90–115 | Upgrade ด้วย `09_2` |
| 115–120 | อธิบาย single source of truth และ Demo |

Copy และ methods ที่ไม่ใช้ในเกมเป็น Bonus

Dictionary เก็บข้อมูลเป็นคู่ `key: value` และเข้าถึงข้อมูลด้วย Key

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `01_python_dictionaries.py` | สร้าง Dictionary, อ่านด้วย `[]`/`get()` และตรวจ Key |
| `02_change_and_add_items.py` | เปลี่ยน เพิ่ม และใช้ `update()` |
| `03_remove_items.py` | `pop()`, `del`, `popitem()` และ `clear()` |
| `04_loop_dictionaries.py` | Loop ผ่าน Keys, Values และคู่ข้อมูลจาก `items()` |
| `05_copy_and_nested.py` | `copy()` และ Nested Dictionaries |
| `06_methods_and_exercises.py` | แบบฝึกรวม Dictionary Methods |
| `07_1_pet_rescue_game.py` | เล่นเกมช่วยสัตว์ที่เก็บข้อมูลเป็น Dictionary |
| `07_2_create_your_dictionary_game.py` | สร้างเกม Dictionary ของตัวเอง |
| `08_pygame_dictionary_cards.py` | Pygame Basic: Character Cards จาก Dictionary |
| `09_1_pet_rescue_pygame.py` | Guided Example: Pet Rescue Pygame |
| `09_2_create_your_dictionary_game_pygame.py` | Upgrade เกมที่เด็กสร้างใน `07_2` |

## สิ่งที่ต้องจำ

- Key ห้ามซ้ำ แต่ Value ซ้ำได้
- ใช้ Key ไม่ใช่ Index เพื่อค้นหาข้อมูล
- `items()` ให้ทั้ง Key และ Value สำหรับแต่ละคู่
- `copy()` ช่วยให้แก้สำเนาโดยไม่เปลี่ยน Dictionary ต้นฉบับ

## ผลลัพธ์ท้ายบท

เด็กออกแบบข้อมูลที่มีรายละเอียดเป็นชื่อกำกับ เช่น ผู้เล่น สัตว์ ไอเทม และคะแนน แล้วใช้ในเกมได้

## Pygame Upgrade

Nested Dictionary กลายเป็นข้อมูลของ Character Cards และ Pet Rescue UI เด็กเพิ่ม
ตัวละครใหม่ได้โดยแก้ข้อมูลแทนการคัดลอกโค้ดวาด พร้อม STEP/Practice หลังแนวคิดใหม่
