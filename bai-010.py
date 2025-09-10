# Bài 10: Số bảo hiểm xã hội của Canada (SIN - Canadian Social Insurance Number) là một số có 9 chữ số, được kiểm tra tính hợp lệ như sau:
# - Số phải nhất (vị trí là 1, tính từ phải sang), là số kiểm tra (check digit).
# - Trọng số được tính từ phải qua trái (không tính check digit), bằng s1 + s2:
# + s1 là tổng các số có vị trí lẻ.
# + Các số có vị trí chẵn nhân đôi. Nếu kết quả nhân đôi có hai chữ số thì kết quả là tổng của hai chữ số này. s2 là tổng các kết quả.
# SIN hợp lệ có tổng trọng số với số kiểm tra chia hết cho 10.
# Ví dụ: SIN 193456787
# - Số kiểm tra là 7 (màu xanh tô đậm).
# - Trọng số là tổng của s1 và s2, với:
# + s1 = 1 + 3 + 5 + 7 = 16
# + Các số có vị trí chẵn nhân đôi: (9 * 2) (4 * 2) (6 * 2) (8 * 2)  18 8 12 16
# s2 = (1 + 8) + 8 + (1 + 2) + (1 + 6) = 27
# Trọng số bằng s1 + s2 = 16 + 27 = 43.
# Vì tổng trọng số với số kiểm tra 43 + 7 = 50 chia hết cho 10 nên số SIN hợp lệ.
# Viết chương trình nhập một số SIN. Kiểm tra xem số SIN đó có hợp lệ hay không.
# Nhập 0 để thoát.

def xulychuoiinput(string, array):
  for kytu in string:
    intkytu = int(kytu)
    array.append(intkytu)
  return array

def dieukien(array):
  if (len(array) != 9):
    return "SIN không hợp lệ"

  sokiemtra = array[8]  # Số phải nhất có vị trì index là 8 (check digit)
  s1 = 0
  s2 = 0
  str_s2 = ""
  arr_s2 = []

  for i in range (0, len(array) - 2, 2):     # s1: là tổng các số vị trí lẻ
    s1 += array[i]

  for i in range (1, len(array), 2):
    arr_component_s2 = array[i] * 2
    str_s2 += str(arr_component_s2)

  xulychuoiinput(str_s2, arr_s2)

  for i in range (0, len(arr_s2)):
    int_i = arr_s2[int(i)]
    s2 += int_i

  trongso = s1 + s2

  if ((trongso + sokiemtra) % 10 == 0):
    return "SIN hợp lệ"
  else:
    return "SIN không hợp lệ"


SIN = input("Sin: (0 để thoát)")
SINarr = []
xulychuoiinput(SIN, SINarr)
output = dieukien(SINarr)
print(output)
