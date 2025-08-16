# Bài 12: Viết chương trình giải hệ phương trình 2 ẩn:
# Các hệ số a1, a2, b1, b2, c1, c2 nhập từ bàn phím. Xét tất cả các trường hợp cụ thể.

a1, b1, c1 = input("Nhập a1, b1, c1: ").split()
a1 = float(a1)
b1 = float(b1)
c1 = float(c1)
a2, b2, c2 = input("Nhập a2, b2, c2: ").split()
a2 = float(a2)
b2 = float(b2)
c2 = float(c2)

D = (a1 * b2) - (a2 * b1)
Dx = (c1 * b2) - (c2 * b1)
Dy = (a1 * c2) - (a2 * c1)

if (D == 0):
  print("Không thể giải")
else:
  x = Dx / D
  y = Dy / D
  print(f"x = {x}\ny = {y}")
