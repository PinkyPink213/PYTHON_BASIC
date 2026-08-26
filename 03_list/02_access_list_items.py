"""บทที่ 2: หยิบของจาก List ด้วย Index และ Slicing"""

# Index คือตำแหน่งของข้อมูล และเริ่มนับจาก 0
#            index:    0        1         2        3
animals = ["cat", "rabbit", "panda", "tiger"]

print("--- Example 1: Index starts at 0 ---")
print(animals[0])
print(animals[2])


print("\n--- Example 2: Negative index ---")
# -1 หมายถึงตัวสุดท้าย และ -2 หมายถึงตัวรองสุดท้าย
print(animals[-1])
print(animals[-2])


print("\n--- Example 3: Slicing ---")
# [start:stop] เลือกตั้งแต่ start แต่หยุดก่อน stop
print(animals[1:3])
print(animals[:2])
print(animals[2:])


print("\n--- Your turn 1 ---")
planets = ["Mercury", "Venus", "Earth", "Mars"]
# TODO 1: แสดง "Earth" โดยใช้ Index


print("\n--- Your turn 2 ---")
# TODO 2: แสดงดาวดวงสุดท้ายโดยใช้ Negative Index


print("\n--- Your turn 3 ---")
# TODO 3: ใช้ Slicing แสดง ["Venus", "Earth"]


print("\n--- Your turn 4: First and last ---")
players = ["Mali", "Nida", "Ploy", "Ton"]
# TODO 4: แสดงผู้เล่นคนแรกด้วย Index 0
# จากนั้นแสดงผู้เล่นคนสุดท้ายด้วย Index -1


print("\n--- Your turn 5: Slice from each side ---")
# TODO 5: ใช้ Slicing แสดงผู้เล่น 2 คนแรก
# จากนั้นใช้ Slicing แสดงผู้เล่นตั้งแต่ Index 2 ถึงตัวสุดท้าย


# === คำถามเช็กความเข้าใจ ===
# 1. ข้อมูลตัวแรกมี Index เท่าไร?
# 2. Index -1 หมายถึงข้อมูลตำแหน่งใด?
# 3. animals[1:3] มีข้อมูลที่ Index 3 รวมอยู่ด้วยหรือไม่?
