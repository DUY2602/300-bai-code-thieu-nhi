# Bài 19: Nhập vào thời điểm 1 và thời điểm 2. Tìm thời gian trải qua giữa hai thời điểm này tính bằng giờ, phút, giây.

hour1, minute1, second1 = input("Nhập giờ phút giây [1]: ").split()
hour1 = int(hour1)
minute1 = int(minute1)
second1 = int(second1)

hour2, minute2, second2 = input("Nhập giờ phút giây [2]: ").split()
hour2= int(hour2)
minute2 = int(minute2)
second2 = int(second2)

def timeBetween(hour1, minute1, second1, hour2, minute2, second2):
  second_Between = second2 - second1
  minute_Between = minute2 - minute1
  hour_Between = hour2 - hour1

  if (second_Between < 0):
    second_Between += 60
    minute_Between -= 1

  if (minute_Between < 0):
    minute_Between += 60
    hour_Between -= 1

  return f"Hieu thoi gian: {hour_Between} giờ {minute_Between} phút {second_Between} giây"

ketqua = timeBetween(hour1, minute1, second1, hour2, minute2, second2)
print(ketqua)
