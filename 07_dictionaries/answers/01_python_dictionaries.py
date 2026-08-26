"""เฉลยบทที่ 1"""
book = {"title": "Magic Door", "author": "Mali", "pages": 100}
print(book["title"])
print(book.get("pages"))
if "author" in book:
    print("Author found!")
