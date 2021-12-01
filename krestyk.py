print("*" * 90)
print(" " * 30, " Игра Крестики-нолики")
print("По традиции первым ходит Х")
print("Что-бы сделать ход нужно  ввести размеченную ячейку,цифру от 0-9 для выбора места")
print("*" * 90)
print()
board = list(range(1, 10))

def pole (board):
   print ("-" * 13)
   for i in range(3):
      print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print ("-" * 13)

def take_input (player_token):
   valid = False
   while not valid:
      player_answer = input("Ходит " + player_token+", ведите номер ячейки: ")
      try:
         player_answer = int(player_answer)
      except:
         print("Введите число!!!")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if (str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Введите число от 1 до 9.")

def checkwin (board):
   win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main (board):
    counter = 0
    win = False
    while not win:
        pole(board)
        if counter % 2 == 0:
           take_input ("X")
        else:
           take_input ("O")
        counter += 1
        if counter > 4:
           tmp = checkwin(board)
           if tmp:
              print (tmp, " выиграл!")
              win = True
              break
        if counter == 9:
            print ("Ничья!")
            break
    pole(board)
main (board)

input("Нажмите Enter для выхода!")