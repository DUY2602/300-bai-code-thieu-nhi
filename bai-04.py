# Bài 4: Viết chương trình nhập vào ba số thực là ba cạnh của một tam giác. Kiểm tra ba cạnh được nhập có hợp lệ hay không.
# Nếu hợp lệ, hãy cho biết loại tam giác và tính diện tích tam giác đó.

import math

a, b, c = input("Nhập vào 3 cạnh tam giác: ").split()
a = int(a)
b = int(b)
c = int(c)
nuachuvi = (a + b + c) / 2
dientich = math.sqrt(nuachuvi * (nuachuvi - a) * (nuachuvi - b) * (nuachuvi - c))

def tamgiacABC(a, b, c):
  if ((a <= 0) or (b <= 0) or (c <= 0) or (a + b <= c) or (a + c <= b) or (b + c <= a)):
    return"Tam giác ABC không hợp lệ"
  else:
    if ((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2)):
      print("ABC là tam giác vuông")
    elif ((a == b) or (b == c) or (a == c)):
      print("ABC là tam giac cân")
    elif ((a == b) and (a == c)):
      print("ABC là tam giác đều")
    else:
      print("ABC là tam giác nhọn")
    print(f"Diện tích ABC = {dientich}")

tamgiacABC(a, b, c)