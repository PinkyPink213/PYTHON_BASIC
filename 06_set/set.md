# Chapter 06 — Python Sets

Set เก็บค่าที่ไม่ซ้ำ ไม่มี Index และลำดับที่แสดงอาจเปลี่ยนได้

## ลำดับไฟล์

| ไฟล์ | สิ่งที่เรียน |
|---|---|
| `01_python_sets.py` | สร้าง Set, ค่าซ้ำ และ Set ว่างด้วย `set()` |
| `02_access_set_items.py` | ตรวจด้วย `in`/`not in` และอ่านด้วย `for` |
| `03_add_and_remove_items.py` | `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()` |
| `04_loop_sets.py` | ใช้ Set กับ `for` และ Conditions |
| `05_join_sets.py` | Union, Intersection, Difference และ Symmetric Difference |
| `06_frozenset.py` | Set ที่เพิ่มหรือลบสมาชิกไม่ได้ |
| `07_set_methods_exercises.py` | แบบฝึกรวม Set Methods |
| `08_1_rescue_team_game.py` | เล่นเกมจัดทีมกู้ภัยโดยใช้ Set |
| `08_2_create_your_set_game.py` | สร้างเกม Set ของตัวเอง |

## สิ่งที่ต้องจำ

- Set ว่างใช้ `set()` เพราะ `{}` คือ Dictionary ว่าง
- `remove()` เกิด Error เมื่อไม่มีค่า แต่ `discard()` ไม่เกิด Error
- `pop()` ลบสมาชิกที่คาดตำแหน่งล่วงหน้าไม่ได้
- `frozenset` เหมาะกับชุดข้อมูลที่ไม่ควรถูกเปลี่ยน

## ผลลัพธ์ท้ายบท

เด็กใช้ Set กำจัดข้อมูลซ้ำ ตรวจสมาชิก และเปรียบเทียบกลุ่มข้อมูลเพื่อสร้างระบบทีมในเกมได้

