# Chapter 05 — Python Tuples

## Core Route — 120 นาที

| เวลา | กิจกรรมหลัก |
|---|---|
| 0–10 | Demo แผนที่และพิกัด |
| 10–50 | create, access, unpack และ immutability |
| 50–70 | เกม Tuple Terminal ของเด็ก |
| 70–90 | พิมพ์ `08_pygame_coordinates_and_click.py` |
| 90–115 | Upgrade ด้วย `09_2` |
| 115–120 | อธิบาย Tuple→position→draw |

Tuple methods และการตกแต่งแผนที่เป็น Bonus

บทสอน Pygame ให้พิมพ์ Example พิกัดและการคลิกก่อน แล้วทำ Your turn/TODO
โดยเปลี่ยน Tuple หนึ่งค่า ทายตำแหน่ง และ Run Checkpoint

Tuple เก็บข้อมูลหลายค่าที่มีลำดับและเก็บค่าซ้ำได้ แต่เปลี่ยนสมาชิกโดยตรงไม่ได้

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `01_python_tuples.py` | สร้าง Tuple, ค่าซ้ำ, Tuple ว่าง และ Tuple หนึ่งสมาชิก |
| `02_access_tuples.py` | Index, Negative Index, Slicing, `in`, `not in` |
| `03_update_tuples.py` | แปลง Tuple → List → แก้ไข → Tuple |
| `04_unpack_tuples.py` | Unpack ค่าใส่ตัวแปรและใช้ `*` รวบค่าที่เหลือ |
| `05_loop_tuples.py` | อ่าน Tuple ด้วย `for` และใช้ร่วมกับ Conditions |
| `06_join_and_methods.py` | รวมด้วย `+`, ทำซ้ำด้วย `*`, `count()`, `index()` |
| `07_1_space_coordinates_game.py` | เล่นเกมพิกัดอวกาศตัวอย่าง |
| `07_2_create_your_tuple_game.py` | สร้างเกม Tuple ของตัวเอง |
| `08_pygame_coordinates_and_click.py` | Pygame Basic: พิกัด `(x, y)` และการคลิกวัตถุ |
| `09_1_space_coordinates_pygame.py` | Guided Example: Space Coordinates Pygame |
| `09_2_create_your_tuple_game_pygame.py` | Upgrade เกมที่เด็กสร้างใน `07_2` |

## สิ่งที่ต้องจำ

- Tuple หนึ่งสมาชิกต้องมี comma เช่น `("cat",)`
- ถ้าต้องแก้ไขสมาชิก ต้องแปลงผ่าน List
- Unpack ต้องมีจำนวนตัวแปรสัมพันธ์กับข้อมูล เว้นแต่ใช้ `*`

## ผลลัพธ์ท้ายบท

เด็กใช้ Tuple เก็บข้อมูลคงที่ เช่น พิกัด กฎ หรือตัวเลือกที่ไม่ควรถูกแก้ และนำไปสร้างเกมได้

## Pygame Upgrade

เด็กใช้ Tuple `(name, x, y)` วางวัตถุบนแผนที่และตรวจการคลิก จากนั้นนำพิกัดจาก
Terminal Space Coordinates มาสร้างแผนที่ภาพ พร้อม Creative Choice เป็นดาวเคราะห์
เกาะสมบัติ หรือจุดหมายที่เด็กออกแบบเอง

Pygame Upgrade ต้องรักษาลำดับ `เลือกจุดหมาย → เลือก/เดาพิกัด → ตรวจผล`
จาก Terminal โดยใช้ตำแหน่ง Mouse แทนการพิมพ์พิกัด
