"""เฉลยบทที่ 7"""
def add_box(function):
    def wrapper():
        print("==========")
        function()
        print("==========")
    return wrapper

@add_box
def show_message():
    print("Hello!")

show_message()
