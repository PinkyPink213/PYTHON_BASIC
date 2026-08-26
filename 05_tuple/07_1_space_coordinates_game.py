"""บทที่ 7.1: เกมตัวอย่าง — Space Coordinates Mission"""

# ผู้เล่นต้องเลือกพิกัดดาวจาก Tuple ที่เปลี่ยนไม่ได้
# เกมใช้ Index, in, unpacking, count(), if-elif-else และ for

print("==================================")
print("     SPACE COORDINATES MISSION")
print("==================================")

destinations = (
    ("moon", 2, 4),
    ("mars", 5, 8),
    ("saturn", 9, 3)
)

print("Available destinations:")
for destination in destinations:
    planet, x, y = destination
    print("- " + planet + " at (" + str(x) + ", " + str(y) + ")")

planet_choice = input("Choose moon, mars, or saturn: ").lower()

planet_names = ("moon", "mars", "saturn")

if planet_choice not in planet_names:
    print("That destination is not available.")
else:
    destination_index = planet_names.index(planet_choice)
    chosen_destination = destinations[destination_index]
    planet, correct_x, correct_y = chosen_destination

    guess_x = int(input("Enter coordinate X: "))
    guess_y = int(input("Enter coordinate Y: "))

    if guess_x == correct_x and guess_y == correct_y:
        print("Coordinates locked!")
        print("*** YOU LANDED ON " + planet.upper() + "! ***")
    elif guess_x == correct_x or guess_y == correct_y:
        print("One coordinate is correct. The spaceship misses the planet!")
    else:
        print("Both coordinates are incorrect. Mission failed!")


# === คำถามเช็กความเข้าใจ ===
# 1. destinations เป็น Tuple ธรรมดาหรือ Nested Tuple?
# 2. Unpacking ถูกใช้ตรงไหน?
# 3. index() ช่วยหา chosen_destination อย่างไร?
# 4. ต้องใช้เงื่อนไขใดจึงจะลงจอดสำเร็จ?

