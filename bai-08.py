# Bài 8: Viết chương trình giải phương trình bậc 2: ax2 + bx + c = 0 (a, b, c nhập từ bàn phím).
# Xét tất cả các trường hợp có thể.

import math

def ptbachai():
  a, b, c = input("Nhập a, b, c: ").split()
  a = float(a)
  b = float(b)
  c = float(c)
  delta = (b**2) - (4*a*c)

  if ((a == 0) and (b == 0) and (c == 0)):
    return "Phương trình có vô số nghiệm"
  if (delta < 0):
    return "Phương trình vô nghiệm"
  elif (delta == 0):
    x = (-b) / (2*a)
    return f"Phương trình có nghiệm kép x = {x}"
  else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return f"Phương trình có 2 nghiệm x1 = {x1} và x2 = {x2}"

ketqua = ptbachai()
print(ketqua)
