# Bài 23: Viết chương trình tìm các số hoàn hảo (perfect number) nhỏ hơn một số nguyên dương n cho trước.
# Biết số hoàn hảo là số nguyên dương, bằng tổng các ước số thực sự của nó (ví dụ: 28 = 14 + 7 + 4 + 2 + 1).

n = int(input("Nhập n: "))

def uocSo(so):
  tong_uoc_so = 0
  for i in range (1, so):
    if (so % i == 0):
      tong_uoc_so += i

  return tong_uoc_so

def soHoanHao(n):
  str_so_hoan_hao = ""
  for i in range (2, n):
    tong = uocSo(i)
    if (i == tong):
      str_so_hoan_hao += str(i) + " "

  return f"Các số hoàn hảo nhỏ hơn {n}: {str_so_hoan_hao}"

ketqua = soHoanHao(n)
print(ketqua)
