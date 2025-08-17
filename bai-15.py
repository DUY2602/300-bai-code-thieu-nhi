# Bài 15: Viết chương trình nhập vào ngày, tháng, năm (giả sử nhập đúng, không cần
# kiểm tra hợp lệ). Tìm xem ngày đó là ngày thứ bao nhiêu trong năm.

day, month, year = input("Nhập ngày tháng năm: ").split()
day = int(day)
month = int(month)
year = int(year)

def countDate(day, month, year):
  count = day
  for i in range (0, month):
    if ((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12)):
      count += 31
    elif ((i == 4) or (i == 6) or (i == 9) or (i == 11)):
      count += 30
    elif (i == 2):
      if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        count += 29
      else:
        count += 28

  return f"Ngày thứ {count}"

ketqua = countDate(day, month, year)
print(ketqua)
