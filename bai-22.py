# Bài 22: Viết chương trình liệt kê, đếm và tính tổng các ước số của số nguyên dương n (n nhập từ bàn phím).

n = int(input("Nhập n: "))

def uocSo(n):
  dem = 0
  tong_uoc_so = 0
  str_uoc_so = ""
  for i in range (1, n + 1):
    if (n % i == 0):
      str_uoc_so += str(i) + " "
      tong_uoc_so += i
      dem += 1

  return f"Các ước số: {str_uoc_so}\nCó {dem} ước số, tổng là: {tong_uoc_so}"

ketqua = uocSo(n)
print(ketqua)
