"""เฉลยบทที่ 5.1: คัดลอกและรวม List"""

wish_list = ["book", "robot"]
birthday_list = wish_list.copy()
birthday_list.append("cake")
print(wish_list)
print(birthday_list)

land_animals = ["cat", "dog"]
sea_animals = ["fish", "whale"]
all_animals = land_animals + sea_animals
print(all_animals)

morning_tasks = ["brush teeth", "eat breakfast"]
school_tasks = ["study", "read"]
morning_tasks.extend(school_tasks)
print(morning_tasks)

