"""เฉลยบทที่ 2: Access Tuples"""

scores = (10, 20, 30, 40, 50)
print(scores[0])
print(scores[-1])
print(scores[1:4])

if 30 in scores:
    print("Score found!")

if 100 not in scores:
    print("Score not found.")

