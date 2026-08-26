"""เฉลยบทที่ 4"""
scores = {40, 55, 70, 90}
for score in scores:
    if score >= 50:
        print(score)

items = {"coin", "key", "map"}
for item in items:
    if item == "key":
        print("Key found!")
    else:
        print("Checking " + item)
