"""เฉลยบทที่ 2"""
game = {"title": "Dragon Cave", "players": 1}
game["players"] = 2
game["difficulty"] = "easy"
game.update({"difficulty": "hard", "lives": 3})
print(game)
