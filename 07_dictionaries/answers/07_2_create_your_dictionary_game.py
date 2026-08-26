"""ตัวอย่างเฉลย: Magic Shop"""
items = {
    "wand": {"price": 100, "power": "light", "stock": 2},
    "potion": {"price": 50, "power": "heal", "stock": 3},
    "cloak": {"price": 80, "power": "hide", "stock": 1}
}
for name, information in items.items():
    print(name, information["price"])

choice = input("Choose an item: ").lower()
if choice not in items:
    print("Item not found.")
else:
    chosen = items[choice]
    if chosen["stock"] > 0:
        chosen["stock"] -= 1
        chosen["status"] = "sold"
        print("You bought " + choice + "!")
    else:
        chosen["status"] = "out of stock"
        print("Out of stock.")
    print(chosen)
