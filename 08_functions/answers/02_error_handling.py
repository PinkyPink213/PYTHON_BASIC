"""เฉลยบทที่ 2"""
try:
    first = int(input("First number: "))
    second = int(input("Second number: "))
    print(first / second)
except ValueError:
    print("Please enter whole numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
