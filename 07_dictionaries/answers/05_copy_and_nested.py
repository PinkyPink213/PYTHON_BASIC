"""เฉลยบทที่ 5"""
students = {
    "student_1": {"name": "Mali", "score": 80},
    "student_2": {"name": "Ton", "score": 70}
}
copied = students["student_1"].copy()
copied["score"] = 100
print(students["student_1"], copied)
students["student_3"] = {"name": "Nida", "score": 90}
print(students["student_3"]["name"])
