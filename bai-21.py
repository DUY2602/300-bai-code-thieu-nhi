# Trong kỳ thi tuyển, một thí sinh sẽ trúng truyển nếu có điểm tổng kết lớn hơn hoặc bằng điểm chuẩn và không có môn nào điểm 0.
# - Điểm tổng kết là tổng điểm của 3 môn thi và điểm ưu tiên.
# - Điểm ưu tiên bao gồm điểm ưu tiên theo khu vực và điểm ưu tiên theo đối tượng.

# Khu vực Đối tượng
# A   B   C         1     2     3
# 2   1   0.5       2.5   1.5   1
# Viết chương trình nhập: điểm chuẩn của hội đồng, điểm 3 môn thi của thí sinh, khu vực
# (nhập X nếu không thuộc khu vực ưu tiên) và đối tượng dự thi (nhập 0 nếu không thuộc đối tượng ưu tiên).
# Cho biết thí sinh đó đậu hay rớt và tổng số điểm đạt được.

diemchuan = float(input("Nhập điểm chuẩn: "))
diem1, diem2, diem3 = input("Nhập điểm 3 môn: ").split()
diem1 = float(diem1)
diem2 = float(diem2)
diem3 = float(diem3)

def diemThi(diemchuan, diem1, diem2, diem3):
  diem_tong = diem1 + diem2 + diem3
  khu_vuc = input("Nhập khu vực (A, B, C): ")
  match khu_vuc:
    case "A":
      diem_tong += 2
    case "B":
      diem_tong += 1
    case "C":
      diem_tong += 0.5
    case _:
      diem_tong += 0

  doi_tuong = int(input("Nhập khu vực (1, 2, 3): "))
  match doi_tuong:
    case 1:
      diem_tong += 2.5
    case 2:
      diem_tong += 1.5
    case 3:
      diem_tong += 1
    case _:
      diem_tong += 0

  if (diem_tong >= diemchuan):
    return f"Đậu [{diem_tong}]"
  else:
    return f"Rớt [{diem_tong}]"

ketqua = diemThi(diemchuan, diem1, diem2, diem3)
print(ketqua)
