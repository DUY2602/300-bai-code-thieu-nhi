# Bài 26: Nhập vào tử số, mẫu số (đều khác 0) của một phân số. Hãy rút gọn phân số
# này. Chọn dạng xuất thích hợp trong trường hợp mẫu số bằng 1 và phân số có dấu.

tuSo = int(input("Nhập vào tử số: "))
mauSo = int(input("Nhập vào mẫu số: "))

def uocSoChung(a, b):
  a = abs(a)
  b = abs(b)

  uocSoA = []
  uocSoB = []
  uocSoChung = []

  for i in range(1, a + 1):
    if a % i == 0:
      uocSoA.append(i)

  for i in range(1, b + 1):
    if b % i == 0:
      uocSoB.append(i)

  for i in uocSoA:
    if i in uocSoB:
      uocSoChung.append(i)

  return max(uocSoChung)

if mauSo < 0:
  tuSo = -tuSo
  mauSo = -mauSo

  soRutGon = uocSoChung(tuSo, mauSo)
  ts = tuSo // soRutGon
  ms = mauSo // soRutGon

  if ms == 1:
    print("Phân số rút gọn là:", ts)
  else:
    print(f"Phân số rút gọn là: {ts}/{ms}")
