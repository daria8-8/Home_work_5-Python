# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
from random import randint
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
count1 = 0 
count2 = 0
while value > 28:
    if flag:
        k = int(input(f"{player1}, введите количество конфет, которое возьмете от 1 до 28: "))
        count1 += k
        value -= k
        flag = False
        print(f"Ходил {player1}, он взял {k}, теперь у него {count1}. Осталось на столе {value}.")
    else:
        k = int(input(f"{player2}, введите количество конфет, которое возьмете от 1 до 28: "))
        count2 += k
        value -= k
        flag = True
        print(f"Ходил {player2}, он взял {k}, теперь у него {count2}. Осталось на столе {value}.")
if flag:
    print(f"Поздравляю, {player1}, ты победил!")
else:
    print(f"Поздравляю, {player2}, ты победил!")