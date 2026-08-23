"""เฉลยบทที่ 4: Unpack Tuples"""

point = (5, 8)
x, y = point
print("X: " + str(x))
print("Y: " + str(y))

pet = ("Milo", "cat", 3)
pet_name, animal_type, pet_age = pet
print(pet_name)
print(animal_type)
print(pet_age)

medals = ("gold", "silver", "bronze", "special")
first_medal, *other_medals = medals
print(first_medal)
print(other_medals)

