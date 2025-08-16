# Bài 11: Viết trò chơi bao - đá - kéo với luật chơi: bao thắng đá, đá thắng kéo, kéo thắng bao.
# Người dùng nhập vào một trong ba ký tự b (bao), d (đá), k (kéo); máy tính sinh ngẫu nhiên một trong ba ký tự trên, thông báo kết quả chơi.

import random

player_score = 0
computer_score = 0
while True:
  selection = ["bao", "da", "keo"]
  computer = random.choice(selection)
  player = input("Nhập vào ký tự (b - d - k), ký tự khác để thoát: ")
  if ((player != "b") and (player != "d") and (player != "k")):
    break
  print(computer)
  match player:
    case "b":
      if (computer == "da"):
        player_score += 1
      elif (computer == "keo"):
        computer_score += 1
    case "d":
      if (computer == "keo"):
        player_score += 1
      elif (computer == "bao"):
        computer_score += 1
    case "k":
      if (computer == "bao"):
        player_score += 1
      elif (computer == "da"):
        computer_score += 1
  print(f"Tỉ số human - computer: {player_score} - {computer_score}")
