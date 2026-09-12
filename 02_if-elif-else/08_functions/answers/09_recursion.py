"""เฉลยบทที่ 9"""
def sum_to(number):
    if number == 1:
        return 1
    return number + sum_to(number - 1)

print(sum_to(5))
