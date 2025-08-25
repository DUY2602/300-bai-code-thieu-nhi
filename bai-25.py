# Bài 25: Nhập vào hai số nguyên dương a, b. Tính ước số chung lớn nhất và bội số
# chung nhỏ nhất của a, b.

a = int(input("Nhập vào số nguyên a: "))
b= int(input("Nhập vào số nguyên b: "))

def uocSoChung(a, b):
  uocSoA = []
  uocSoB = []
  uocSoChung = []

  for i in range (1, a + 1):
    if a % i == 0:
      uocSoA.append(i)

  for i in range (1, b + 1):
    if b % i == 0:
      uocSoB.append(i)

  for i in uocSoA:
    for j in uocSoB:
      if i == j:
        uocSoChung.append(i)

  return max(uocSoChung)

ucln = uocSoChung(a, b)
bcnn = a * b / ucln

print("Ước chung lớn nhất là: ", ucln)
print("Bội chung nhỏ nhất là: ", bcnn)
