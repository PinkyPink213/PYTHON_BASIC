"""เฉลยบทที่ 7"""
names = ["Mali", "Ton", "Mali", "Nida", "Ton"]
print(set(names))

player_1 = {"key", "map", "water"}
player_2 = {"torch", "map", "water"}
print(player_1 | player_2)
print(player_1 & player_2)
print(player_1 - player_2)

required_skills = {"swim", "run"}
my_skills = {"run", "jump", "swim"}
print(required_skills.issubset(my_skills))
