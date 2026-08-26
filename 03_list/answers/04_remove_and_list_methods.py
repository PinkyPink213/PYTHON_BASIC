"""เฉลยบทที่ 4: ลบ ค้นหา นับ และเรียงข้อมูล"""

pets = ["cat", "dog", "rabbit", "dog"]
pets.remove("dog")
print(pets)
removed_pet = pets.pop(1)
print("Removed: " + removed_pet)
print(pets)

scores = [30, 10, 20, 20]
print(scores.count(20))
print(scores.index(20))
scores.sort()
print(scores)

shopping = ["milk", "bread", "eggs", "juice"]
shopping.remove("bread")
shopping.pop()
print(shopping)

numbers = [5, 2, 9, 2]
print(numbers.count(2))
numbers.sort()
print(numbers)

queue = ["Mali", "Nida", "Ton"]
first_person = queue.pop(0)
print(first_person)
print(queue)

missions = ["find key", "open door", "get treasure"]
missions.clear()
print(missions)
