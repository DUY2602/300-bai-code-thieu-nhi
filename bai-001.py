# Bài 1: Nhập vào diện tích S của 1 mặt cầu. Tính thể tích V của mặt cầu đó

import math

dientich = float(input("Nhập diện tích S: "))
Pi = 3.141593
bankinh = math.sqrt(dientich / (4*Pi))

thetich = 4/3 * Pi * bankinh**3

print(f"Thể tích V của mặt cầu là: {thetich}")
