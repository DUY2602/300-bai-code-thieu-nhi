# Bài 3: Viết chương trình nhập vào tọa độ (xC, yC) là tâm của một đường tròn, và R là bán kính của đường tròn đó.
#Nhập vào tọa độ (xM, yM) của điểm M. Xác định điểm M nằm trong, nằm trên hay nằm ngoài đường tròn.

import math

xC, yC = input("Nhập tọa độ tâm đường tròn (xC, yC): ").split()
xC = float(xC)
yC = float(yC)
R = float(input("Nhập bán kính R: "))

xM, yM = input("Nhập tọa độ điểm M: ").split()
xM = float(xM)
yM = float(yM)

khoangcach = math.sqrt((xM - xC)**2 + (yM - yC)** 2)
if (khoangcach <= R):
  print("M nằm trong đường tròn")
else:
  print("M nằm ngoài đường tròn")