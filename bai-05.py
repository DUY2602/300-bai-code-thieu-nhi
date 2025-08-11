# Bài 5: Viết chương trình nhập vào tọa độ các đỉnh của tam giác ABC và của điểm M.
# xác định điểm M nằm trong, nằm trên cạnh hay nằm ngoài tam giác ABC.

import math

xA, yA = input("A (xA, yA) ?: ").split()
xA = float(xA)
yA = float(yA)
xB, yB = input("B (xB, yB) ?: ").split()
xB = float(xB)
yB = float(yB)
xC, yC = input("C (xC, yC) ?: ").split()
xC = float(xC)
yC = float(yC)
xM, yM = input("M (xM, yM) ?: ").split()
xM = float(xM)
yM = float(yM)

AM = math.sqrt((xM - xA)**2 + (yM - yA)**2)
MB = math.sqrt((xM - xA)**2 + (yM - yA)**2)
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
AC = math.sqrt((xC - xA)**2 + (yC - yA)**2)
MC = math.sqrt((xC - xM)**2 + (yC - yM)**2)
BC = math.sqrt((xC - xB)**2 + (yC - yB)**2)

pAMB = (AM + MB + AB) / 2
pAMC = (AM + MC + AC) / 2
pBMC = (MB + MC + BC) / 2
pABC = (AB + AC + BC) / 2

sAMB = math.sqrt(abs(pAMB * (pAMB - AM) * (pAMB - AB) * (pAMB - MB)))
sAMC = math.sqrt(abs(pAMC * (pAMC - AM) * (pAMC - AC) * (pAMC - MC)))
sABC = math.sqrt(abs(pABC * (pABC - AC) * (pABC - AB) * (pABC - BC)))
sBMC = math.sqrt(abs(pBMC * (pBMC - MB) * (pAMB - BC) * (pAMB - MC)))


def MsovoiABC(sAMB, sAMC, sBMC, sABC):

  if ((sAMB == 0) or (sAMC == 0) or (sBMC == 0)):
    return "M nằm trên cạnh của ABC"
  elif (sAMB + sAMC + sBMC == sABC):
    return "M nằm trong ABC"
  else:
    return "M nằm ngoài ABC"

MsovoiABC(sAMB, sAMC, sBMC, sABC)
