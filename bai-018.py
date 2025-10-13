# Bài 18: Viết chương trình nhập vào số giờ, xuất ra số tương đương tính theo tuần, theo ngày và theo giờ.

hour = int(input("Nhập số giờ: "))

week = hour // (7 * 24)
day = (hour - (week * 7 * 24)) // 24
hour = hour - (week * 7 * 24) - (day * 24)

print(f"{week} tuẩn, {day} ngày, {hour} giờ")
