# Python Sets สำหรับเด็ก

Set ใช้เก็บข้อมูลหลายค่าที่ไม่ซ้ำกัน และไม่มีลำดับตำแหน่งแน่นอน

```python
animals = {"cat", "dog", "rabbit"}
```

## คุณสมบัติสำคัญ

- สมาชิกไม่ซ้ำกัน
- ไม่มี Index
- ลำดับที่แสดงอาจเปลี่ยนได้
- เพิ่มและลบสมาชิกได้
- ตรวจสมาชิกด้วย `in` และ `not in`

## คำสั่งสำคัญ

```python
items = {"key", "map"}

items.add("torch")
items.update({"water", "food"})
items.remove("map")
items.discard("rope")

print("key" in items)
```

## การรวมและเปรียบเทียบ Set

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
print(a ^ b)  # symmetric difference
```

## สิ่งที่ควรจำ

- Set ว่างต้องใช้ `set()` ไม่ใช่ `{}`
- `{}` คือ Dictionary ว่าง
- `remove()` เกิด Error ถ้าไม่มีค่านั้น
- `discard()` ไม่เกิด Error เมื่อไม่มีค่านั้น
- `frozenset` คือ Set ที่เพิ่มหรือลบสมาชิกไม่ได้

