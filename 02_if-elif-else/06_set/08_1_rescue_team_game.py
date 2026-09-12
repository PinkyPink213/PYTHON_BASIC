"""บทที่ 8.1: เกมตัวอย่าง — Rescue Team Builder"""

# เลือกสมาชิกทีมกู้ภัยโดยใช้ Set ป้องกันชื่อซ้ำ
# จากนั้นตรวจว่าทีมมีทักษะที่ภารกิจต้องใช้ครบหรือไม่

print("==================================")
print("       RESCUE TEAM BUILDER")
print("==================================")

available_heroes = {"aqua", "flash", "rock", "sky"}
print("Heroes: " + str(available_heroes))

hero_1 = input("Choose hero 1: ").lower()
hero_2 = input("Choose hero 2: ").lower()
hero_3 = input("Choose hero 3: ").lower()

team = {hero_1, hero_2, hero_3}

if not team.issubset(available_heroes):
    print("A hero name is incorrect.")
elif len(team) < 3:
    print("Choose 3 different heroes.")
else:
    aqua_skills = {"swim", "heal"}
    flash_skills = {"run", "electricity"}
    rock_skills = {"strength", "shield"}
    sky_skills = {"fly", "see far"}
    team_skills = set()

    for hero in team:
        if hero == "aqua":
            team_skills.update(aqua_skills)
        elif hero == "flash":
            team_skills.update(flash_skills)
        elif hero == "rock":
            team_skills.update(rock_skills)
        else:
            team_skills.update(sky_skills)

    print("Team: " + str(team))
    print("Team skills: " + str(team_skills))

    mission = input("Choose flood, mountain, or city: ").lower()

    if mission == "flood":
        required_skills = {"swim", "heal"}
    elif mission == "mountain":
        required_skills = {"fly", "strength"}
    elif mission == "city":
        required_skills = {"run", "shield"}
    else:
        required_skills = set()

    if len(required_skills) == 0:
        print("That mission does not exist.")
    elif required_skills.issubset(team_skills):
        print("*** YOUR TEAM COMPLETED THE RESCUE! ***")
    else:
        missing_skills = required_skills - team_skills
        print("Mission failed. Missing skills: " + str(missing_skills))

