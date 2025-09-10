# Bài 9: Viết chương trình nhập vào số x chỉ số đo của một góc, tính bằng phút.
# Cho biết nó thuộc góc vuông thứ bao nhiêu của vòng tròn lượng giác.
# Tính cos(x), dùng hàm do math.h cung cấp.

import math

def sodogoc():
  phut = int(input("Nhập vào số đo x của góc (phút): "))
  do = phut / 60
  if (do <= 90):
    print("x thuộc góc vuông thứ nhất")
  elif (do <= 180):
    print("x thuộc góc vuông thứ hai")
  elif (do <= 270):
    print("x thuộc góc vuông thứ ba")
  else:
    print("x thuộc góc vuông thứ tư")
  rad = do * math.pi / 180
  return f"cos(x) = {math.cos(rad)}"

ketqua = sodogoc()
print(ketqua)
