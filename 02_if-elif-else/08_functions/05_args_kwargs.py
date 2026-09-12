"""บทที่ 5: *args และ **kwargs"""

print("--- Example 1: *args ---")
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all(2, 4, 6))


print("\n--- Example 2: **kwargs ---")
def show_profile(**information):
    for key, value in information.items():
        print(key, value)

show_profile(name="Mali", role="wizard", level=3)


print("\n--- Your turn ---")
# TODO 1: สร้าง largest(*numbers) return ค่ามากที่สุดด้วย max()
# TODO 2: สร้าง describe_pet(**pet) แสดงทุก key และ value

# คำถาม: *args เก็บเป็น Tuple และ **kwargs เก็บเป็น Dictionary อย่างไร?

