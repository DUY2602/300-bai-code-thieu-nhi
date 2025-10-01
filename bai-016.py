# Bài 16: Viết chương trình nhập vào một năm (> 1582), in lịch của năm đó.
# Tính thứ cho ngày đầu năm bằng công thức Zeller (bài 14, trang 6).

year = int(input("Nhập vào 1 năm: "))

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

def firstDayOfWeek(month, year):
  a = (14 - month) // 12
  y = year - a
  m = month + 12 * a - 2
  dayofweek = (1 + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7

  return dayofweek

def Calendar(year):
  print(f"Lịch của năm {year}\n")

  for month in range (1, 13):
    print(f"\n\nTháng {month}")
    print("CN  T2  T3  T4  T5  T6  T7")
    start_index = firstDayOfWeek(month, year)
    print("    " * start_index, end="")
    count = start_index

    for day in range (1, daysInMonth(month, year) + 1):
      print(f"{day:2d}", end="  ")
      count += 1
      if (count == 7):
        print("\n")
        count = 0

Calendar(year)
