"""เฉลยบทที่ 7: Type Conversion / Casting"""

# Casting คือการเปลี่ยนข้อมูลให้เป็นชนิดที่เราต้องการ

coins_text = "20"
coins = int(coins_text)
print(coins + 5)

temperature = 32.5
print("Temperature: " + str(temperature))

age = int(input("How old are you? "))
print("Next year, you will be " + str(age + 1) + ".")

print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))
