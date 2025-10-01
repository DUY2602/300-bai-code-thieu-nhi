# Bài 17: Viết chương trình tạo lịch trực cho 5 bạn: A, B, C, D, E.
# Nhập năm và thứ (0 - 6, 0 là Chúa Nhật, 1 là thứ Hai, ...) cho ngày đầu năm.
# Sau đó nhập một tháng trong năm và in lịch trực của tháng đó.
# Lưu ý 5 bạn trực lần lượt theo thứ tự trên, ngày Chúa nhật không ai trực và bạn A sẽ trực ngày đầu tiên của năm.

danh_sach_truc_nhat = ["A", "B", "C", "D", "E"]
year = int(input("Nhập năm: "))
first_date_of_year = int(input("Nhập thứ cho ngày đầu tiên của năm: "))
month = int(input("Nhập tháng: "))

def isLeapYear(year):
  return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

def daysInMonth(month, year):
  if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
    return 31
  elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
    return 30
  else:
    if ((month == 2) and (isLeapYear(year))):
      return 29
    else:
      return 28

def Calendar(year):
  print(f"\n\nLịch trực nhật tháng {month} năm {year}")
  print("CN      T2      T3      T4      T5      T6      T7")

  start_index = firstDayOfWeek(month, year)
  print("       " * start_index, end="")
  count = start_index

  for day in range (1, daysInMonth(month, year) + 1):
    if (count == 7):
      print("\n")
      count = 0
    if (count == 0):

      print(f"{day:2d}", end="     ")
      count += 1
    else:
      index_truc_nhat = (day + 1) % 5
      print(f"{day:2d}[{danh_sach_truc_nhat[index_truc_nhat]}]", end="   ")
      count += 1

Calendar(year)
