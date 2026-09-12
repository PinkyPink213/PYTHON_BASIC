"""เฉลยบทที่ 4"""
scores = {"Mali": 80, "Ton": 45, "Nida": 90}
for name, score in scores.items():
    print(name, score)
    if score >= 50:
        print("passed")
