"""เฉลยบทที่ 10"""
def even_numbers(limit):
    number = 2
    while number <= limit:
        yield number
        number += 2

for number in even_numbers(10):
    print(number)
