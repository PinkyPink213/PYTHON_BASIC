# Python Loops สำหรับเด็ก

Loop คือการสั่งให้ Python ทำงานเดิมซ้ำหลายครั้ง ช่วยให้เราไม่ต้องเขียนคำสั่งเดิมซ้ำเอง

## `for` loop

ใช้เมื่อเราต้องการหยิบข้อมูลจาก List ทีละชิ้น

```python
animals = ["cat", "dog", "rabbit"]

for animal in animals:
    print(animal)
```

ตัวแปร `animal` จะเปลี่ยนค่าไปทีละรอบ จนกว่าจะหยิบข้อมูลครบทุกชิ้น

## `range()`

ใช้สร้างชุดตัวเลขสำหรับ `for` loop

```python
for number in range(1, 6):
    print(number)
```

ผลลัพธ์คือเลข 1 ถึง 5 เพราะ `range()` หยุดก่อนเลขตัวสุดท้าย

| คำสั่ง | ตัวเลขที่ได้ |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 5)` | 1, 2, 3, 4 |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 |

## `while` loop

ใช้ทำงานซ้ำตราบใดที่เงื่อนไขยังเป็น `True`

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

ต้องทำให้เงื่อนไขเปลี่ยนเป็น `False` ได้ ไม่เช่นนั้นจะเกิด Infinite Loop หรือ Loop ที่ไม่สิ้นสุด

## `break`

ใช้หยุด Loop ทันที

```python
while True:
    answer = input("Type quit to stop: ")

    if answer == "quit":
        break
```

## `continue`

ใช้ข้ามรอบปัจจุบัน แล้วเริ่มรอบถัดไป

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

## `match-case`

`match-case` ไม่ใช่ Loop และไม่ได้ทำงานซ้ำ แต่เป็นคำสั่งเลือกการทำงานจากค่าที่ได้รับ
คล้ายกับ `if-elif-else` โดย Python จะเลือก `case` ที่ตรงกับค่านั้น

```python
command = input("Choose look, walk, or quit: ").lower()

match command:
    case "look":
        print("You look around.")
    case "walk":
        print("You walk forward.")
    case "quit":
        print("Goodbye!")
    case _:
        print("Unknown command.")
```

`case _` หมายถึงกรณีอื่นทั้งหมด ทำหน้าที่คล้าย `else`

รวมหลายคำตอบด้วย `|`:

```python
match answer:
    case "yes" | "y":
        print("You chose yes.")
    case "no" | "n":
        print("You chose no.")
    case _:
        print("Please try again.")
```

ใช้เงื่อนไขเพิ่มเติมหลัง `case` ด้วย `if` ได้ เรียกว่า Guard:

```python
match score:
    case 100:
        print("Perfect!")
    case value if value >= 50:
        print("Passed!")
    case _:
        print("Try again!")
```

## เลือกใช้ Loop แบบไหนดี?

| สถานการณ์ | Loop ที่เหมาะสม |
|---|---|
| หยิบของใน List ทีละชิ้น | `for` |
| ทำซ้ำตามจำนวนรอบที่รู้แน่นอน | `for` และ `range()` |
| ถามซ้ำจนกว่าคำตอบจะถูก | `while` |
| เล่นเกมจนกว่าผู้เล่นจะออก | `while` |
| เลือกการทำงานจากค่าหนึ่งค่า | `match-case` |

## สิ่งที่ควรจำ

- โค้ดข้างใน Loop ต้องเยื้อง 4 ช่อง
- `for` เหมาะกับข้อมูลใน List และจำนวนรอบที่รู้แน่นอน
- `while` ทำซ้ำตามเงื่อนไข
- ตรวจให้แน่ใจว่า `while` สามารถหยุดได้
- `break` หยุด Loop
- `continue` ข้ามไปทำรอบถัดไป
- `match-case` ใช้แยกการทำงานตามค่าที่ได้รับ
- `case _` รองรับกรณีอื่นทั้งหมด
