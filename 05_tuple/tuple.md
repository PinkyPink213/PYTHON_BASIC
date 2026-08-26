# Python Tuples สำหรับเด็ก

Tuple ใช้เก็บข้อมูลหลายค่าเหมือน List แต่เมื่อสร้างแล้วจะเปลี่ยน เพิ่ม หรือลบสมาชิกโดยตรงไม่ได้

```python
animals = ("cat", "dog", "rabbit")
```

## คุณสมบัติของ Tuple

- มีลำดับแน่นอน
- เก็บค่าซ้ำได้
- เข้าถึงด้วย Index ได้
- เปลี่ยนสมาชิกโดยตรงไม่ได้ (`unchangeable`)
- เขียนด้วยวงเล็บ `()`

## หัวข้อในบทนี้

1. Python Tuples
2. Access Tuples
3. Update Tuples
4. Unpack Tuples
5. Loop Tuples
6. Join Tuples
7. Tuple Methods
8. Tuple Exercises
9. Code Challenge

## คำสั่งสำคัญ

```python
colors = ("red", "green", "blue")

print(colors[0])
print(colors[-1])
print(len(colors))
print("red" in colors)

first, second, third = colors
joined = colors + ("yellow",)
```

## สิ่งที่ควรจำ

- Tuple หนึ่งสมาชิกต้องมี comma: `("cat",)`
- Index เริ่มจาก `0`
- ใช้ Slicing ได้
- ถ้าจำเป็นต้องแก้ไข ให้แปลงเป็น List แล้วแปลงกลับ
- `count()` นับจำนวนค่าที่ซ้ำ
- `index()` หาตำแหน่งแรกของค่า

