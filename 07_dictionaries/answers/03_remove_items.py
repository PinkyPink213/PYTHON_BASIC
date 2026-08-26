"""เฉลยบทที่ 3"""
book = {"title": "Magic Door", "pages": 100, "price": 250}
removed_price = book.pop("price")
del book["pages"]
print(removed_price)
print(book)
