# Bài 24: Nhập vào một số tự nhiên n (n khai báo kiểu unsigned long)
# a. Số tự nhiên n có bao nhiêu chữ số.
# b. Hãy tìm chữ số cuối cùng của n.
# c. Hãy tìm chữ số đầu tiên của n.
# d. Tính tổng các chữ số của n.
# e. Hãy tìm số đảo ngược của n.

chuoiso = input("Nhập vào 1 số tự nhiên: ")

def xulychuoiso(string, array):
  for kytu in string:
    n = int(kytu)
    array.append(n)
  return array

MyArray = []
xulychuoiso(chuoiso, MyArray)
print(MyArray)

a = len(MyArray)

b = MyArray[a-1]

c = MyArray[0]

d = 0
for so in MyArray:
  d += so

def daoNguocSo(array):
  reversestr = ""
  for i in range (a):
    reversestr += str(MyArray[a - i - 1])
  return reversestr

e = daoNguocSo(MyArray)




print("a. Số vừa nhập có " + str(a) + " chữ số")
print("b. Chữ số cuối cùng là: ", b)
print("c. Chữ số đầu tiên là: ", c)
print("d. Tổng các chữ số là: ", d)
print("e. Số đảo ngược là: ", e)
