# Bài 6: Viết chương trình nhập vào ba số nguyên. Hãy in ba số này ra màn hình theo
# thứ tự tăng dần và chỉ dùng tối đa một biến phụ.

def sapxep():
  a, b, c = input("Nhập vào 3 số nguyên: ").split()
  a = int(a)
  b = int(b)
  c = int(c)

  chuoiso = [a, b, c]

  for i in range (len(chuoiso)):
    for j in range (len(chuoiso) - 1):
        if (chuoiso[i] < chuoiso[j]):
          chuoiso[j], chuoiso[i] = chuoiso[i], chuoiso[j]

  return chuoiso


ketqua = sapxep()
print(ketqua)
