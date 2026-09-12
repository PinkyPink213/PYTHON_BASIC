"""เฉลยบทที่ 6"""
inventory = {"potion": 3, "key": 1, "coin": 10}
inventory["potion"] += 2
inventory["torch"] = 1
inventory.pop("key")
print(inventory)

student = {"name": "Nida", "math": 80, "science": 90}
student["average"] = (student["math"] + student["science"]) / 2
print(student)
print(student.get("english", "No score"))
