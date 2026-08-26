"""ตัวอย่างเฉลย: Magic Team"""
heroes = {"fire", "water", "wind", "earth"}
choice_1 = input("Hero 1: ").lower()
choice_2 = input("Hero 2: ").lower()
choice_3 = input("Hero 3: ").lower()
team = {choice_1, choice_2, choice_3}

if not team.issubset(heroes):
    print("Unknown hero.")
elif len(team) < 3:
    print("Choose different heroes.")
else:
    skill_map = {
        "fire": {"light", "heat"}, "water": {"swim", "heal"},
        "wind": {"fly", "speed"}, "earth": {"strength", "shield"}
    }
    team_skills = set()
    for hero in team:
        team_skills.update(skill_map[hero])
    required = {"fly", "heal"}
    if required.issubset(team_skills):
        print("Mission complete!")
    else:
        print("Missing: " + str(required - team_skills))
