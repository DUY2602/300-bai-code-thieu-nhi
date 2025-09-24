# Bài 14: Viết chương trình nhập vào ngày, tháng, năm (giả sử nhập đúng, không cần kiểm tra hợp lệ).
# Tìm ngày, tháng, năm của ngày tiếp theo.

day, month, year = input("Nhập ngày tháng năm: ").split()
day = int(day)
month = int(month)
year = int(year)

def nextDate(day, month, year):
  if (((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)) and (day == 31)):
    day = 1
    if (month == 12):
      month = 1
      year += 1
    else:
      month += 1
  elif (((month == 4) or (month == 6) or (month == 9) or (month == 11)) and (day == 30)):
    day = 1
    month += 1
  elif (month == 2):
    if ((((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) and (day == 29)):
      day = 1
      month += 1
    elif (not(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) and (day == 28)):
      day = 1
      month += 1
  else:
    day += 1

  return f"Ngày mai là: {day} {month} {year}"

ngaymai = nextDate(day, month, year)
print(ngaymai)
