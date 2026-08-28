# Chapter 03 — Python Lists

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | Demo inventory และทายค่าของ List |
| 10–50 | access, change, append, remove, in และ len |
| 50–70 | สร้างเกมของตัวเองใน `06_2` |
| 70–90 | พิมพ์ `07_pygame_list_inventory.py` |
| 90–115 | Upgrade ด้วย `08_2` โดยยังไม่ใช้ Loop |
| 115–120 | ชี้ DATA→EVENT→DRAW และ Demo |

Nested List และการแต่ง asset เพิ่มเป็น Bonus

List ใช้เก็บข้อมูลหลายค่าที่มีลำดับ แก้ไขได้ และเก็บค่าซ้ำได้

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `01_list_basics.py` | สร้าง List, `len()` และชนิดข้อมูลใน List |
| `02_access_list_items.py` | Index, Negative Index และ Slicing |
| `02_1_check_list_items.py` | ตรวจของด้วย `in` และ `not in` ร่วมกับ Conditions |
| `03_change_and_add_items.py` | เปลี่ยนค่า, `append()`, `insert()`, `extend()` |
| `04_remove_and_list_methods.py` | `remove()`, `pop()`, `del`, `clear()` และ Methods |
| `05_list_with_conditions.py` | ใช้ List ร่วมกับ `if-elif-else` โดยยังไม่ใช้ Loop |
| `05_1_copy_and_join_lists.py` | Copy และ Join Lists |
| `05_2_nested_lists.py` | List ที่อยู่ข้างใน List |
| `06_1_treasure_backpack_game.py` | เล่นเกมติดเกาะและจัดกระเป๋าที่รับของได้ 3 ชิ้น |
| `06_2_create_your_list_game.py` | สร้างเกม List ของตัวเองตาม Pattern ของเกมตัวอย่าง |
| `07_pygame_list_inventory.py` | Pygame Basic: วาด Inventory จาก List |
| `08_1_treasure_backpack_pygame.py` | Guided Example: Treasure Backpack Pygame |
| `08_2_create_your_list_game_pygame.py` | Upgrade เกมที่เด็กสร้างใน `06_2` |

## เกมท้ายบท: Treasure Backpack

ผู้เล่นเลือกของ 3 ชิ้นจากของ 5 ชิ้น โปรแกรมตรวจของที่ไม่มีและของซ้ำ หากผิดให้
อ่านข้อความแล้ว Run ใหม่ จากนั้นจึงพบของใหม่และตัดสินใจว่าจะเก็บ เปลี่ยน
หรือนำของใดออกจากกระเป๋า (การถามซ้ำอัตโนมัติจะเริ่มใน Chapter 04 Loops)

เกมใช้เฉพาะ Basic, Conditions และ List Manipulation จึงยังไม่ต้องใช้ `while`

## ผลลัพธ์ท้ายบท

เด็กเข้าถึง ตรวจ เพิ่ม เปลี่ยน ลบ คัดลอก และรวมข้อมูลใน List แล้วนำไปสร้างระบบกระเป๋าในเกมได้

## Pygame Upgrade และ Assets

เรียนวาด Inventory จาก List ใน `07_pygame_list_inventory.py` แล้วแปลงเกมตัวอย่าง
เป็น `_1` และเกมที่เด็กสร้างใน `06_2` เป็น `_2` แบบ STEP/Practice/Your Turn
เลือกไอคอนพร้อมใช้ได้จาก `assets/items/` และค่อยเปลี่ยนเป็นรูปของตัวเองหลังเกมทำงาน

`08_1` รักษา Flow จาก Terminal Version ครบ: Story → เลือกของเดิม 3/5 → Cliff →
พบ Radio และเลือก Keep/Replace → พบ Coconut และเลือก Keep/Replace → Ending
ส่วน `08_2` มี STEP ตรงกันเพื่อให้เด็กย้ายสถานที่ ของใหม่ เหตุการณ์ และตอนจบ
จาก `06_2` ของตัวเอง ไม่ได้บังคับให้เปลี่ยนกลับเป็นธีมเกาะ
