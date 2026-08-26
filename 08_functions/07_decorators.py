"""บทที่ 7: Python Decorators — ห่อ Function"""

# Decorator เพิ่มพฤติกรรมก่อนหรือหลัง Function เดิม
def add_stars(function):
    def wrapper():
        print("**********")
        function()
        print("**********")
    return wrapper

@add_stars
def show_winner():
    print("YOU WIN!")

show_winner()


print("\n--- Your turn ---")
# TODO: สร้าง decorator ชื่อ add_box
# ให้แสดงเส้น ===== ก่อนและหลัง function ที่ถูกตกแต่ง

# คำถาม: wrapper เรียก Function เดิมตรงไหน?

