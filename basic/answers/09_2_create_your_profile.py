"""ตัวอย่างเฉลยบทที่ 9.2: Space Hero Profile"""

print("==================================")
print("       SPACE HERO PROFILE")
print("==================================")

name = input("What is your name? ").strip()
planet = input("Choose a home planet: ").strip().title()
power = input("Choose a superpower: ").strip().lower()
age = int(input("How old are you? "))
stars = int(input("How many stars did you collect? "))

hero_name = "Captain " + name
age_next_year = age + 1
bonus_stars = stars * 2

print("\n--- HERO CARD ---")
print(f"Hero: {hero_name}")
print(f"Home planet: {planet}")
print(f"Superpower: {power}")
print(f"Age next year: {age_next_year}")
print(f"Bonus stars: {bonus_stars}")

