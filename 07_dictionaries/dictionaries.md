# Python Dictionaries สำหรับเด็ก

Dictionary เก็บข้อมูลเป็นคู่ `key: value`

```python
player = {"name": "Mali", "score": 10}
```

- Key ใช้เป็นชื่อสำหรับค้นหาข้อมูล
- Key ห้ามซ้ำกัน
- Value ซ้ำกันได้และเปลี่ยนได้
- เข้าถึงด้วย Key ไม่ใช่ตำแหน่ง Index

```python
print(player["name"])
player["score"] = 20
player["level"] = 2
```

Methods สำคัญ: `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `clear()`, `copy()`

