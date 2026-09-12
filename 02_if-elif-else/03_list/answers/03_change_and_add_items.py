"""เฉลยบทที่ 3: เปลี่ยนและเพิ่มของใน List"""

fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"
fruits.append("watermelon")
fruits.insert(1, "grape")
fruits.extend(["cherry", "lemon"])
print(fruits)

backpack = ["book", "pencil", "snack"]
backpack[1] = "pen"
backpack.append("water")
backpack.insert(0, "map")
print(backpack)

more_items = ["hat", "camera"]
backpack.extend(more_items)
print(backpack)

levels = ["easy", "easy", "hard", "hard"]
levels[1:3] = ["medium", "medium"]
print(levels)
