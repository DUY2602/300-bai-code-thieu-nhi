# Bài 20: Viết chương trình nhập số kW điện đã tiêu thụ. Tính tiền điện phải trả, biết rằng khung giá tiền điện như sau:
# 0kW         100kW       250kW       350kW
# 500đ/kW    800đ/kW     1000đ/kW   1500đ/kW

so_KW = int(input("Nhập số KW đã tiêu thụ: "))

def tien_dien(so_KW):
  tien_dien = 0
  if (so_KW <= 0):
    return "Số KW điện phải lớn hơn 0"
  elif (so_KW < 100):
    tien_dien = 500 * so_KW
  elif (so_KW < 250):
    tien_dien = 500 * 100 + (so_KW - 100) * 800
  elif (so_KW < 350):
    tien_dien = 500 * 100 + 150 * 800 + (so_KW - 250) * 1000
  else:
    tien_dien = 500 * 100 + 150 * 800 + 100 * 1000 + (so_KW - 350) * 1500

  return f"Chi phí: {tien_dien}"

ketqua = tien_dien(so_KW)
print(ketqua)
