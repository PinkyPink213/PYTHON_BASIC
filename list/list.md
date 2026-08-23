# Python List

> อ้างอิง: [Python Lists — W3Schools](https://www.w3schools.com/python/python_lists.asp)

## 1. List คืออะไร?

`List` ใช้เก็บข้อมูลหลายค่าไว้ในตัวแปรเดียว

คุณสมบัติของ List:

- มีลำดับแน่นอน (`Ordered`)
- แก้ไขข้อมูลได้ (`Changeable`)
- เก็บข้อมูลซ้ำกันได้ (`Allow Duplicates`)
- เก็บข้อมูลต่างชนิดกันได้
- เขียนโดยใช้วงเล็บเหลี่ยม `[]`

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'banana', 'orange']
```

---

## 2. การสร้าง List

```python
students = ["Alice", "Bob", "Charlie"]
numbers = [10, 20, 30, 40]
scores = [85.5, 90.0, 72.5]
```

List สามารถเก็บข้อมูลต่างชนิดกันได้:

```python
information = ["Pink", 30, True, 55.5]

print(information)
```

สร้าง List ด้วย `list()`:

```python
fruits = list(("apple", "banana", "orange"))

print(fruits)
```

---

## 3. การนับจำนวนสมาชิก

ใช้ฟังก์ชัน `len()`:

```python
fruits = ["apple", "banana", "orange"]

print(len(fruits))
```

ผลลัพธ์:

```text
3
```

---

## 4. การเข้าถึงข้อมูลด้วย Index

Index ของ List เริ่มต้นที่ `0`

| ข้อมูล         | apple | banana | orange |
| -------------- | ----: | -----: | -----: |
| Index          |   `0` |    `1` |    `2` |
| Negative Index |  `-3` |   `-2` |   `-1` |

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

ผลลัพธ์:

```text
apple
banana
orange
```

### Negative Index

Index ติดลบจะเริ่มนับจากข้อมูลตัวสุดท้าย:

```python
fruits = ["apple", "banana", "orange"]

print(fruits[-1])
print(fruits[-2])
```

ผลลัพธ์:

```text
orange
banana
```

---

## 5. การเลือกข้อมูลหลายค่า — Slicing

รูปแบบ:

```python
list[start:stop]
```

- เริ่มตั้งแต่ `start`
- หยุดก่อนถึง `stop`

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

ผลลัพธ์:

```text
[20, 30, 40]
```

ตัวอย่างเพิ่มเติม:

```python
print(numbers[:3])   # ตั้งแต่ต้นถึงก่อน index 3
print(numbers[2:])   # ตั้งแต่ index 2 ถึงตัวสุดท้าย
print(numbers[-3:])  # สามตัวสุดท้าย
```

### การกำหนด Step

รูปแบบ:

```python
list[start:stop:step]
```

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])
```

ผลลัพธ์:

```text
[10, 30, 50]
```

กลับลำดับ List:

```python
print(numbers[::-1])
```

---

## 6. ตรวจสอบข้อมูลใน List

ใช้ Operator `in`:

```python
fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("พบ banana")
```

ใช้ `not in`:

```python
if "mango" not in fruits:
    print("ไม่พบ mango")
```

---

## 7. การแก้ไขข้อมูล

ระบุ Index ของข้อมูลที่ต้องการแก้ไข:

```python
fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'mango', 'orange']
```

### แก้ไขข้อมูลหลายค่า

```python
fruits = ["apple", "banana", "orange", "grape"]

fruits[1:3] = ["mango", "watermelon"]

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'mango', 'watermelon', 'grape']
```

---

## 8. การเพิ่มข้อมูล

### `append()` — เพิ่มข้อมูลต่อท้าย

```python
fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'banana', 'orange']
```

### `insert()` — เพิ่มในตำแหน่งที่กำหนด

```python
fruits = ["apple", "orange"]

fruits.insert(1, "banana")

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'banana', 'orange']
```

### `extend()` — เพิ่มข้อมูลจาก List อื่น

```python
fruits = ["apple", "banana"]
more_fruits = ["orange", "mango"]

fruits.extend(more_fruits)

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'banana', 'orange', 'mango']
```

> อ่านเพิ่มเติม: [Add List Items — W3Schools](https://www.w3schools.com/python/python_lists_add.asp)

---

## 9. การลบข้อมูล

### `remove()` — ลบด้วยค่า

```python
fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'orange']
```

> หากมีค่าซ้ำกัน `remove()` จะลบค่าที่พบตัวแรก

### `pop()` — ลบด้วย Index

```python
fruits = ["apple", "banana", "orange"]

fruits.pop(1)

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'orange']
```

หากไม่กำหนด Index จะลบตัวสุดท้าย:

```python
fruits.pop()
```

### `del` — ลบด้วย Index

```python
fruits = ["apple", "banana", "orange"]

del fruits[1]

print(fruits)
```

ลบตัวแปร List ทั้งหมด:

```python
del fruits
```

### `clear()` — ลบข้อมูลทั้งหมด

```python
fruits = ["apple", "banana", "orange"]

fruits.clear()

print(fruits)
```

ผลลัพธ์:

```text
[]
```

---

## 10. การวนลูป List

### ใช้ `for`

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

### วนลูปด้วย Index

```python
fruits = ["apple", "banana", "orange"]

for index in range(len(fruits)):
    print(index, fruits[index])
```

### ใช้ `enumerate()`

```python
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

ผลลัพธ์:

```text
0 apple
1 banana
2 orange
```

### ใช้ `while`

```python
fruits = ["apple", "banana", "orange"]

index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1
```

---

## 11. การเรียงลำดับ List

### `sort()` — เรียงจากน้อยไปมาก

```python
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)
```

ผลลัพธ์:

```text
[10, 20, 30, 40, 50]
```

เรียงข้อความตามตัวอักษร:

```python
fruits = ["orange", "apple", "banana"]

fruits.sort()

print(fruits)
```

ผลลัพธ์:

```text
['apple', 'banana', 'orange']
```

### เรียงจากมากไปน้อย

```python
numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)
```

ผลลัพธ์:

```text
[50, 40, 30, 20, 10]
```

### `reverse()` — กลับลำดับข้อมูล

```python
numbers = [10, 20, 30]

numbers.reverse()

print(numbers)
```

ผลลัพธ์:

```text
[30, 20, 10]
```

> `sort()` เรียงข้อมูลตามค่า แต่ `reverse()` กลับลำดับปัจจุบัน

---

## 12. การคัดลอก List

ไม่ควรคัดลอกด้วยการกำหนดตัวแปรโดยตรง:

```python
list1 = ["apple", "banana"]
list2 = list1
```

เพราะทั้งสองตัวแปรจะอ้างถึง List เดียวกัน

### ใช้ `copy()`

```python
list1 = ["apple", "banana"]
list2 = list1.copy()

list2.append("orange")

print(list1)
print(list2)
```

ผลลัพธ์:

```text
['apple', 'banana']
['apple', 'banana', 'orange']
```

### ใช้ `list()`

```python
list2 = list(list1)
```

### ใช้ Slicing

```python
list2 = list1[:]
```

> อ่านเพิ่มเติม: [Python List copy() — W3Schools](https://www.w3schools.com/python/ref_list_copy.asp)

---

## 13. การรวม List

### ใช้เครื่องหมาย `+`

```python
list1 = ["apple", "banana"]
list2 = ["orange", "mango"]

result = list1 + list2

print(result)
```

ผลลัพธ์:

```text
['apple', 'banana', 'orange', 'mango']
```

### ใช้ `extend()`

```python
list1 = ["apple", "banana"]
list2 = ["orange", "mango"]

list1.extend(list2)

print(list1)
```

### ความแตกต่างระหว่าง `append()` และ `extend()`

ใช้ `append()`:

```python
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
```

ผลลัพธ์เป็น Nested List:

```text
[1, 2, [3, 4]]
```

ใช้ `extend()`:

```python
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
```

ผลลัพธ์:

```text
[1, 2, 3, 4]
```

---

## 14. List Comprehension

List Comprehension เป็นวิธีสร้าง List ใหม่แบบสั้น

รูปแบบ:

```python
new_list = [expression for item in iterable]
```

ตัวอย่าง:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

ผลลัพธ์:

```text
[1, 4, 9, 16, 25]
```

### ใช้ร่วมกับเงื่อนไข

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

ผลลัพธ์:

```text
[2, 4, 6]
```

> อ่านเพิ่มเติม: [List Comprehension — W3Schools](https://www.w3schools.com/python/python_lists_comprehension.asp)

---

## 15. Nested List

Nested List คือ List ที่มี List อยู่ข้างใน:

```python
students = [
    ["Alice", 85],
    ["Bob", 90],
    ["Charlie", 78]
]
```

เข้าถึง List ชั้นใน:

```python
print(students[0])
```

ผลลัพธ์:

```text
['Alice', 85]
```

เข้าถึงข้อมูลภายใน Nested List:

```python
print(students[0][0])
print(students[0][1])
```

ผลลัพธ์:

```text
Alice
85
```

---

## 16. List Methods ที่ควรรู้

| Method                 | หน้าที่                      |
| ---------------------- | ---------------------------- |
| `append(value)`        | เพิ่มข้อมูลหนึ่งค่าต่อท้าย   |
| `insert(index, value)` | เพิ่มข้อมูลในตำแหน่งที่กำหนด |
| `extend(iterable)`     | เพิ่มข้อมูลหลายค่า           |
| `remove(value)`        | ลบค่าที่พบเป็นตัวแรก         |
| `pop(index)`           | ลบและคืนค่าตาม Index         |
| `clear()`              | ลบข้อมูลทั้งหมด              |
| `index(value)`         | หา Index ของค่า              |
| `count(value)`         | นับจำนวนครั้งที่ค่าปรากฏ     |
| `sort()`               | เรียงลำดับข้อมูล             |
| `reverse()`            | กลับลำดับข้อมูล              |
| `copy()`               | คัดลอก List                  |

ตัวอย่าง:

```python
numbers = [10, 20, 20, 30]

print(numbers.index(20))
print(numbers.count(20))
```

ผลลัพธ์:

```text
1
2
```

---

## สรุปคำสั่งสำคัญ

```python
fruits = ["apple", "banana"]

# เพิ่มข้อมูล
fruits.append("orange")
fruits.insert(1, "mango")
fruits.extend(["grape", "watermelon"])

# แก้ไขข้อมูล
fruits[0] = "cherry"

# ลบข้อมูล
fruits.remove("banana")
fruits.pop()
del fruits[0]

# นับจำนวน
number_of_items = len(fruits)

# วนลูป
for fruit in fruits:
    print(fruit)
```

## สิ่งที่ควรจำ

- List เขียนด้วย `[]`
- Index เริ่มต้นที่ `0`
- Negative Index เริ่มนับจากด้านหลัง
- List แก้ไขได้
- List เก็บค่าซ้ำได้
- `append()` เพิ่มหนึ่งค่าต่อท้าย
- `insert()` เพิ่มค่าตามตำแหน่ง
- `extend()` เพิ่มหลายค่า
- `remove()` ลบด้วยค่า
- `pop()` ลบด้วย Index
- `len()` นับจำนวนสมาชิก
- `sort()` เรียงลำดับข้อมูล
