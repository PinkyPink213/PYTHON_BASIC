"""เฉลยบทที่ 4.1: return กับ print"""

print("--- Your turn 1: Answer ---")
def add(a, b):
    return a + b

total = add(5, 3)
print(total)


print("\n--- Your turn 2: Answer ---")
def create_title(name):
    return "*** " + name + " ***"

title = create_title("Dragon Cave")
print(title + " Welcome!")


print("\n--- Your turn 3: Answer ---")
def show_triple(number):
    print(number * 3)

def get_triple(number):
    return number * 3

result_from_print = show_triple(4)
result_from_return = get_triple(4)

print(result_from_print)   # None
print(result_from_return)  # 12

