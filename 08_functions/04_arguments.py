"""บทที่ 4: Python Arguments"""

print("--- Example 1: Parameters and arguments ---")
def greet(name):
    print("Hello, " + name + "!")

greet("Mali")


print("\n--- Example 2: Keyword and default arguments ---")
def create_pet(name, animal="cat"):
    print(name + " is a " + animal + ".")

create_pet("Milo")
create_pet(animal="dog", name="Lucky")


print("\n--- Your turn ---")
# TODO 1: สร้าง introduce(name, age) แล้วแสดงข้อมูล
# TODO 2: สร้าง power(base, exponent=2) แล้ว return ผลยกกำลัง

# คำถาม: Parameter, positional argument, keyword argument และ default ต่างกันอย่างไร?

