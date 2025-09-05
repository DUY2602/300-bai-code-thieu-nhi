# Bài 7: Viết chương trình giải phương trình bậc 1: ax + b = 0 (a, b nhập từ bàn phím).
# Xét tất cả các trường hợp có thể.

def ptbacnhat():
  a, b = input("Nhập a, b: ").split()
  a = float(a)
  b = float(b)

  if ((a == 0) and (b != 0)):
    return "Phương trình vô nghiệm"
  elif ((a != 0) and (b == 0)):
    return f"x = 0"
  elif ((a == 0) and (b == 0)):
    return "Phương trình có vô số nghiệm"
  else:
    return f"x = {-b/a}"

ketqua = ptbacnhat()
print(ketqua)
