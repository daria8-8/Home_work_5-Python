# b) Подумайте как наделить бота ""интеллектом""
from random import randint
player1 = input("Введите своё имя: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
count1 = 0 
count2 = 0
min_s = 1
max_s = 28
while value > max_s:
    if flag:
        k = int(input(f"{player1}, введите количество конфет, которое возьмете от {min_s} до {max_s}: "))
        count1 += k
        value -= k
        flag = False
        print(f"Ходил {player1}, он взял {k}, теперь у него {count1}. Осталось на столе {value}.")
    else:
        if value>(max_s*2):
          k = randint(1,max_s+1)
        else:
          k = value-(max_s+1)
        count2 += k
        value -= k
        flag = True
        print(f"Ходил {player2}, он взял {k}, теперь у него {count2}. Осталось на столе {value}.")
if flag:
    print(f"Поздравляю, {player1}, ты победил!")
else:
    print(f"Увы, победил {player2}:(")