"""ตัวอย่างเฉลย: Lucky Treasure"""
import random

def random_treasure():
    return random.choice(["coin", "gem", "trap"])

def play_round(player):
    treasure = random_treasure()
    print(player + " found " + treasure)
    if treasure == "gem":
        return 3
    if treasure == "coin":
        return 1
    return 0

try:
    name = input("Player name: ").strip()
    rounds = int(input("Rounds: "))
    score = 0
    for number in range(rounds):
        score += play_round(name)
    print("Score: " + str(score))
except ValueError:
    print("Rounds must be a whole number.")
