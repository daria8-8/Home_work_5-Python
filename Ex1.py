# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt = input("Введите текст через пробел:\n")
find = "абв"
print(list(filter(lambda x: find not in x, txt.split())))


# txt = ['ываабв', 'лповап', 'абвцукв', 'алоабвабв', 'ываываы']
# find = "абв"
# print(list(filter(lambda x: find not in x, txt)))