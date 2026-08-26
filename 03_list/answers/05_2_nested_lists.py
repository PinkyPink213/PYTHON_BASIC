"""เฉลยบทที่ 5.2: Nested List"""

students = [
    ["Mali", 85],
    ["Ton", 72],
    ["Nida", 90]
]

treasure_map = [
    ["tree", "rock"],
    ["river", "treasure"]
]

print(treasure_map[1][0])
print(treasure_map[1][1])

students[1][1] = 80
print(students)

