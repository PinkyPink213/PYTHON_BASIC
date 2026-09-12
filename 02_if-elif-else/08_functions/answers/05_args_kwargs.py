"""เฉลยบทที่ 5"""
def largest(*numbers):
    return max(numbers)

def describe_pet(**pet):
    for key, value in pet.items():
        print(key, value)

print(largest(3, 9, 5))
describe_pet(name="Milo", animal="cat")
