# Bài 2: Nhập vào 2 tọa độ xA, yA và xB, yB. Tính khoảng cách AB

import math

xA, yA = input("A (xA, yA) ?").split()
xA = float(xA)
yA = float(yA)
xB, yB = input("B (xB, yB) ?").split()
xB = float(xB)
yB = float(yB)

AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
print(f"|AB| = {AB}")
