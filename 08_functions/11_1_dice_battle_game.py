"""บทที่ 11.1: Code Challenge — Dice Battle"""

import random

def roll_dice():
    return random.randint(1, 6)

def battle(player_name, monster_name="Dragon"):
    player_roll = roll_dice()
    monster_roll = roll_dice()
    print(player_name + " rolled " + str(player_roll))
    print(monster_name + " rolled " + str(monster_roll))

    if player_roll > monster_roll:
        return "win"
    elif player_roll < monster_roll:
        return "lose"
    return "draw"

try:
    player_name = input("Hero name: ").strip()
    rounds = int(input("How many rounds? "))

    wins = 0
    for round_number in range(1, rounds + 1):
        print("\nRound " + str(round_number))
        result = battle(player_name)
        print(result.upper())
        if result == "win":
            wins += 1

    print("\nWins: " + str(wins))
except ValueError:
    print("Rounds must be a whole number.")

