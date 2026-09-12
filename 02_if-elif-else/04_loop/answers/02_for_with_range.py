"""เฉลยบทที่ 2: for loop กับ range()"""

print("--- Example 1: Count from 0 ---")
for number in range(5):
    print(number)


print("\n--- Example 2: Choose start and stop ---")
for number in range(1, 6):
    print(number)


print("\n--- Example 3: Count by 2 ---")
for number in range(2, 11, 2):
    print(number)


print("\n--- Your turn 1: Answer ---")
for number in range(1, 11):
    print(number)


print("\n--- Your turn 2: Answer ---")
for number in range(5, 21, 5):
    print(number)


print("\n--- Your turn 3: Answer ---")
for count in range(3):
    print("Jump!")


print("\n--- Your turn 4: Answer ---")
for number in range(5, 0, -1):
    print(number)
print("Blast off!")


print("\n--- Your turn 5: Answer ---")
for number in range(1, 6):
    print("3 x " + str(number) + " = " + str(3 * number))


print("\n--- Your turn 6: Answer ---")
for number in range(1, 7):
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")
