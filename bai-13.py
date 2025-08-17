# Bài 13: Viết chương trình nhập vào ngày, tháng, năm. Kiểm tra ngày và tháng nhập
# có hợp lệ hay không. Tính thứ trong tuần của ngày đó.
# dayofweek = (d + y + y / 4 - y / 100 + y / 400 + (31 * m) / 12) % 7 với:
# a = (14 - month) / 12
# y = year - a
# m = month + 12 * a - 2
# dayofweek: 0 (Chúa nhật), 1 (thứ hai), 2 (thứ ba), ...

day, month, year = input("Nhập vào ngày tháng năm: ").split()
day = int(day)
month = int(month)
year = int(year)

a = (14 - month) // 12
y = year - a
m = month + 12 * a - 2
dayofweek = (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7

approve_msg = "Hợp lệ"
error_msg = "Không hợp lệ"

def checkDate(day, month, year):
  if (month == 2):
    isLeap = False
    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
      isLeap = True

    match isLeap:
      case True:
        if ((month == 2) and (day > 29)):
          return error_msg
      case False:
        if ((month == 2) and (day > 28)):
          return error_msg

  if ((day <= 0) or (month <= 0) or (year <= 0) or (month > 12)):
    return error_msg
  elif ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
    if (day > 31):
      return error_msg
  elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
    if (day > 30):
      return error_msg

  return approve_msg

ketqua = checkDate(day, month, year)
print(ketqua)

if (ketqua == approve_msg):
  match dayofweek:
    case 0:
      print("Chủ Nhật")
    case 1:
      print("Thứ Hai")
    case 2:
      print("Thứ Ba")
    case 3:
      print("Thứ Tư")
    case 4:
      print("Thứ Năm")
    case 5:
      print("Thứ Sáu")
    case 6:
      print("Thứ Bảy")
